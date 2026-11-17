"""Definición del tap y su esquema de configuración."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_indec.client import (
    DEFAULT_API_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_PAGE_SIZE,
    DEFAULT_TIMEOUT,
    USER_AGENT,
)
from tap_indec.streams import EMAEStream, IPCStream, MercadoTrabajoStream


class TapIndec(Tap):
    """Tap para series estadísticas del INDEC."""

    name = "tap-indec"
    package_name = "tap_indec"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateType,
            description=(
                "Fecha inicial de la carga, en formato ISO 8601 (YYYY-MM-DD). "
                "Si se omite, cada serie arranca en su primera fecha disponible."
            ),
        ),
        th.Property(
            "end_date",
            th.DateType,
            description="Fecha final inclusive, en formato ISO 8601 (YYYY-MM-DD).",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default=DEFAULT_API_URL,
            description="URL base de la API de series de datos.gob.ar.",
        ),
        th.Property(
            "timeout",
            th.IntegerType,
            default=DEFAULT_TIMEOUT,
            description="Timeout por request, en segundos.",
        ),
        th.Property(
            "max_retries",
            th.IntegerType,
            default=DEFAULT_MAX_RETRIES,
            description="Reintentos ante errores transitorios (429 y 5xx).",
        ),
        th.Property(
            "page_size",
            th.IntegerType,
            default=DEFAULT_PAGE_SIZE,
            description="Puntos por página al paginar una serie (máximo 1000).",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            default=USER_AGENT,
            description="Header User-Agent enviado a la API.",
        ),
        th.Property(
            "include_discontinued",
            th.BooleanType,
            default=False,
            description=(
                "Si es true, incluye series marcadas como discontinuadas en el "
                "catálogo. Por defecto se omiten."
            ),
        ),
        th.Property(
            "fail_on_series_error",
            th.BooleanType,
            default=True,
            description=(
                "Si es true, un error de la API corta el sync. Si es false, se "
                "registra el error y se continúa con la próxima serie."
            ),
        ),
        th.Property(
            "series",
            th.ObjectType(
                additional_properties=th.ArrayType(th.StringType),
            ),
            description=(
                "Filtro opcional por stream. Ejemplo: "
                '{"ipc": ["148.3_INIVELNAL_DICI_M_26"]}. Si un stream no '
                "aparece, se sincronizan todas sus series."
            ),
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Devuelve los streams disponibles."""
        return [
            IPCStream(self),
            EMAEStream(self),
            MercadoTrabajoStream(self),
        ]


if __name__ == "__main__":
    TapIndec.cli()
