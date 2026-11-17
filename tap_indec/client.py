"""Cliente HTTP para la API de series de datos.gob.ar.

La API devuelve, para cada serie, una lista de pares ``[fecha, valor]``. El
cliente se encarga de la paginación, los reintentos y de traducir los errores
de la API a excepciones con contexto.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import date
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from tap_indec import __version__

LOGGER = logging.getLogger(__name__)

DEFAULT_API_URL = "https://apis.datos.gob.ar/series/api"
DEFAULT_TIMEOUT = 30
DEFAULT_PAGE_SIZE = 1000
MAX_PAGE_SIZE = 1000
DEFAULT_MAX_RETRIES = 5
USER_AGENT = f"tap-indec/{__version__} (+https://github.com/akalautaro/tap-indec)"

RETRY_STATUS_CODES = (429, 500, 502, 503, 504)


class IndecAPIError(RuntimeError):
    """Error devuelto por la API de series o por una respuesta inesperada."""


@dataclass(frozen=True)
class SeriesPoint:
    """Un punto de una serie: fecha ISO y valor (puede ser nulo)."""

    date: str
    value: float | None


@dataclass
class SeriesResult:
    """Puntos y metadatos de una serie."""

    series_id: str
    points: list[SeriesPoint] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)
    count: int = 0

    @property
    def last_date(self) -> str | None:
        """Última fecha con valor no nulo, o ``None`` si no hay datos."""
        for point in reversed(self.points):
            if point.value is not None:
                return point.date
        return None


def _iso(value: str | date | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value.isoformat()
    return value


class IndecClient:
    """Cliente de la API de series de datos.gob.ar.

    Args:
        api_url: URL base de la API.
        timeout: timeout por request, en segundos.
        max_retries: reintentos para errores transitorios (429, 5xx).
        page_size: cantidad de puntos por página. La API acepta hasta 1000.
        user_agent: identificador enviado en el header ``User-Agent``.
        session: sesión de ``requests`` opcional (útil en tests).
    """

    def __init__(
        self,
        api_url: str = DEFAULT_API_URL,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        page_size: int = DEFAULT_PAGE_SIZE,
        user_agent: str = USER_AGENT,
        session: requests.Session | None = None,
    ) -> None:
        self.api_url = api_url.rstrip("/")
        self.timeout = timeout
        self.page_size = page_size
        self._session = session or requests.Session()
        self._session.headers.update(
            {
                "User-Agent": user_agent,
                "Accept": "application/json",
            }
        )
        retry = Retry(
            total=max_retries,
            connect=max_retries,
            read=max_retries,
            status=max_retries,
            backoff_factor=0.5,
            status_forcelist=RETRY_STATUS_CODES,
            allowed_methods=frozenset({"GET"}),
            respect_retry_after_header=True,
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)

    def close(self) -> None:
        """Cierra la sesión HTTP."""
        self._session.close()

    def __enter__(self) -> IndecClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def fetch_series(
        self,
        series_id: str,
        start_date: str | date | None = None,
        end_date: str | date | None = None,
        page_size: int | None = None,
    ) -> SeriesResult:
        """Trae todos los puntos de una serie en el rango pedido.

        La paginación es explícita: se pide de a ``page_size`` puntos hasta
        cubrir ``count``. El rango es inclusivo en ambos extremos.

        Raises:
            IndecAPIError: si la serie no existe o la respuesta no tiene el
                formato esperado.
        """
        result = SeriesResult(series_id=series_id)
        offset = 0
        size = min(page_size or self.page_size, MAX_PAGE_SIZE)

        while True:
            payload = self._request(
                series_id=series_id,
                start_date=_iso(start_date),
                end_date=_iso(end_date),
                limit=size,
                offset=offset,
            )
            data = payload.get("data")
            if not isinstance(data, list):
                raise IndecAPIError(
                    f"Response for series {series_id!r} has no 'data' list: {payload!r}"
                )

            result.count = int(payload.get("count") or 0)
            meta = payload.get("meta")
            if isinstance(meta, list):
                for item in meta:
                    if isinstance(item, dict):
                        result.meta.update(item)
            elif isinstance(meta, dict):
                result.meta = meta

            for row in data:
                if not isinstance(row, list) or len(row) < 2:
                    raise IndecAPIError(
                        f"Unexpected point format for series {series_id!r}: {row!r}"
                    )
                raw_date, raw_value = row[0], row[1]
                if not isinstance(raw_date, str):
                    raise IndecAPIError(
                        f"Unexpected date format for series {series_id!r}: {raw_date!r}"
                    )
                value: float | None
                if raw_value is None:
                    value = None
                else:
                    try:
                        value = float(raw_value)
                    except (TypeError, ValueError) as exc:
                        raise IndecAPIError(
                            f"Non-numeric value for series {series_id!r} ({raw_date}): {raw_value!r}"
                        ) from exc
                result.points.append(SeriesPoint(date=raw_date, value=value))

            offset += len(data)
            if not data or offset >= result.count:
                break

        LOGGER.debug("Serie %s: %s puntos (count=%s)", series_id, len(result.points), result.count)
        return result

    def _request(
        self,
        series_id: str,
        start_date: str | None,
        end_date: str | None,
        limit: int,
        offset: int,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {
            "ids": series_id,
            "format": "json",
            "limit": limit,
            "start": offset,
        }
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date

        url = f"{self.api_url}/series/"
        LOGGER.debug("GET %s params=%s", url, params)
        try:
            response = self._session.get(url, params=params, timeout=self.timeout)
        except requests.RequestException as exc:
            raise IndecAPIError(
                f"Network error while fetching series {series_id!r}: {exc}"
            ) from exc

        if response.status_code >= 400:
            detail = _error_detail(response)
            raise IndecAPIError(
                f"API returned {response.status_code} for series {series_id!r}: {detail}"
            )

        try:
            payload = response.json()
        except ValueError as exc:
            raise IndecAPIError(
                f"Non-JSON response for series {series_id!r} (HTTP {response.status_code})"
            ) from exc

        if not isinstance(payload, dict):
            raise IndecAPIError(f"Unexpected response for series {series_id!r}: {payload!r}")
        if payload.get("errors"):
            raise IndecAPIError(f"API rejected series {series_id!r}: {_error_detail(response)}")
        return payload


def _error_detail(response: requests.Response) -> str:
    try:
        payload = response.json()
    except ValueError:
        return response.text[:300] or f"HTTP {response.status_code}"
    errors = payload.get("errors") if isinstance(payload, dict) else None
    if errors:
        return "; ".join(str(error.get("error", error)) for error in errors)
    return str(payload)[:300]
