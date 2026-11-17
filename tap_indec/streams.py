"""Streams del tap.

Cada stream agrupa series de la misma frecuencia y comparte el mismo esquema.
Las aperturas (región, categoría, sector, aglomerado) van como columnas, no
como streams separados.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from functools import cache, cached_property
from importlib import resources
from typing import Any, ClassVar

from singer_sdk import Stream

from tap_indec.client import (
    DEFAULT_API_URL,
    USER_AGENT,
    IndecAPIError,
    IndecClient,
)

LOGGER = logging.getLogger(__name__)

BASE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "series_id": {"type": ["string"]},
        "date": {"type": ["string"], "format": "date"},
        "value": {"type": ["number", "null"]},
        "series_name": {"type": ["string"]},
        "unit": {"type": ["string", "null"]},
        "frequency": {"type": ["string"]},
        "dataset": {"type": ["string", "null"]},
        "source": {"type": ["string"]},
    },
}

DIMENSION_TYPES: dict[str, dict[str, Any]] = {
    "region": {"type": ["string", "null"]},
    "category": {"type": ["string", "null"]},
    "sector": {"type": ["string", "null"]},
    "aglomerado": {"type": ["string", "null"]},
    "measure": {"type": ["string", "null"]},
    "geography_type": {"type": ["string", "null"]},
    "base": {"type": ["string", "null"]},
}


@dataclass(frozen=True)
class SeriesSpec:
    """Definición de una serie del catálogo."""

    id: str
    name: str
    description: str
    frequency: str
    units: str
    start_date: str
    end_date: str
    dataset: str
    download_url: str
    dimensions: dict[str, str]
    active: bool = True

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SeriesSpec:
        return cls(
            id=data["id"],
            name=data.get("name") or data["id"],
            description=data.get("description") or "",
            frequency=data.get("frequency") or "unknown",
            units=data.get("units") or "",
            start_date=data.get("start_date") or "",
            end_date=data.get("end_date") or "",
            dataset=data.get("dataset") or "",
            download_url=data.get("download_url") or "",
            dimensions=dict(data.get("dimensions") or {}),
            active=bool(data.get("active", True)),
        )


@cache
def load_catalog() -> dict[str, Any]:
    """Lee el catálogo empaquetado."""
    with (
        resources.files("tap_indec").joinpath("catalog.json").open("r", encoding="utf-8") as handle
    ):
        return json.load(handle)


class IndecSeriesStream(Stream):
    """Stream base para series de la API de datos.gob.ar."""

    primary_keys: ClassVar[list[str]] = ["series_id", "date"]
    replication_key = "date"
    stream_catalog_key = ""

    def __init__(self, tap: Any, name: str | None = None) -> None:
        super().__init__(tap, name)
        self._client: IndecClient | None = None

    @cached_property
    def series(self) -> list[SeriesSpec]:
        """Series habilitadas para este stream."""
        catalog = load_catalog()["streams"].get(self.stream_catalog_key, {})
        specs = [SeriesSpec.from_dict(item) for item in catalog.get("series", [])]
        if not self.config.get("include_discontinued", False):
            specs = [spec for spec in specs if spec.active]
        selected = (self.config.get("series") or {}).get(self.name)
        if selected:
            wanted = set(selected)
            specs = [spec for spec in specs if spec.id in wanted]
        return specs

    @property
    def client(self) -> IndecClient:
        """Cliente HTTP compartido por el tap."""
        if self._client is None:
            self._client = IndecClient(
                api_url=self.config.get("api_url") or DEFAULT_API_URL,
                timeout=int(self.config.get("timeout") or 30),
                max_retries=int(self.config.get("max_retries") or 5),
                page_size=int(self.config.get("page_size") or 1000),
                user_agent=self.config.get("user_agent") or USER_AGENT,
            )
        return self._client

    @property
    def schema(self) -> dict[str, Any]:
        properties = dict(BASE_SCHEMA["properties"])
        for dim in sorted(self.dimensions):
            properties[dim] = DIMENSION_TYPES[dim]
        return {"type": "object", "properties": properties}

    @cached_property
    def dimensions(self) -> set[str]:
        """Dimensiones presentes en alguna serie del stream."""
        dims: set[str] = set()
        for spec in self.series:
            dims.update(spec.dimensions)
        return dims

    def get_records(self, context: Mapping[str, Any] | None = None) -> Iterable[dict[str, Any]]:
        """Emite un registro por punto de cada serie."""
        state = self.stream_state.setdefault("series_last_dates", {})
        start_override = self.config.get("start_date")
        end_date = self.config.get("end_date")
        full_refresh = bool(self.config.get("full_refresh", False))

        for spec in self.series:
            start_date = None if full_refresh else state.get(spec.id)
            start_date = start_date or start_override or spec.start_date or None
            try:
                result = self.client.fetch_series(spec.id, start_date=start_date, end_date=end_date)
            except IndecAPIError as exc:
                if self.config.get("fail_on_series_error", True):
                    raise
                LOGGER.warning("Skipping series %s: %s", spec.id, exc)
                continue
            last_date = None
            emitted = 0
            for point in result.points:
                if point.value is None:
                    continue
                record = {
                    "series_id": spec.id,
                    "date": point.date,
                    "value": point.value,
                    "series_name": spec.name,
                    "unit": spec.units or None,
                    "frequency": spec.frequency,
                    "dataset": spec.dataset or None,
                    "source": "INDEC",
                }
                for dim in sorted(self.dimensions):
                    record[dim] = spec.dimensions.get(dim)
                yield record
                last_date = point.date
                emitted += 1

            if last_date:
                state[spec.id] = last_date
                self.stream_state["series_last_dates"] = state
            LOGGER.debug(
                "Stream %s serie %s: %s registros desde %s",
                self.name,
                spec.id,
                emitted,
                start_date,
            )


class IPCStream(IndecSeriesStream):
    """Índice de Precios al Consumidor."""

    name = "ipc"
    stream_catalog_key = "ipc"


class EMAEStream(IndecSeriesStream):
    """Estimador Mensual de Actividad Económica."""

    name = "emae"
    stream_catalog_key = "emae"


class MercadoTrabajoStream(IndecSeriesStream):
    """Tasas del mercado de trabajo de la EPH."""

    name = "mercado_trabajo"
    stream_catalog_key = "mercado_trabajo"
