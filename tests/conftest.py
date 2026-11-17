"""Fixtures compartidas por los tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from tap_indec.client import SeriesPoint, SeriesResult
from tap_indec.tap import TapIndec

FIXTURES = Path(__file__).parent / "fixtures"


def _read_fixture(name: str) -> dict[str, Any]:
    with (FIXTURES / name).open(encoding="utf-8") as handle:
        return json.load(handle)


@pytest.fixture
def load_fixture() -> Any:
    """Devuelve una función para cargar fixtures JSON de la API."""
    return _read_fixture


@pytest.fixture
def config() -> dict[str, Any]:
    return {
        "start_date": "2026-01-01",
        "api_url": "https://api.test/series/api",
        "timeout": 5,
        "max_retries": 0,
        "page_size": 1000,
    }


@pytest.fixture
def tap(config: dict[str, Any]) -> TapIndec:
    return TapIndec(config=config, parse_env_config=False)


class FakeClient:
    """Cliente falso para tests de streams, sin HTTP."""

    def __init__(self, points_by_id: dict[str, list[SeriesPoint]]) -> None:
        self.points_by_id = points_by_id
        self.calls: list[tuple[str, str | None, str | None]] = []

    def fetch_series(
        self,
        series_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        page_size: int | None = None,
    ) -> SeriesResult:
        self.calls.append((series_id, start_date, end_date))
        points = [
            point
            for point in self.points_by_id.get(series_id, [])
            if start_date is None or point.date >= start_date
        ]
        return SeriesResult(
            series_id=series_id,
            points=points,
            meta={"field": {"id": series_id}},
            count=len(points),
        )


@pytest.fixture
def fake_client() -> FakeClient:
    return FakeClient(
        {
            "145.3_INGNACNAL_DICI_M_15": [
                SeriesPoint("2026-08-01", 100.0),
                SeriesPoint("2026-09-01", 101.0),
                SeriesPoint("2026-10-01", None),
            ],
            "11.3_VMATC_2004_M_12": [
                SeriesPoint("2026-07-01", 90.0),
                SeriesPoint("2026-08-01", 91.0),
            ],
            "45.2_ECTDT_0_T_33": [
                SeriesPoint("2026-01-01", 0.08),
                SeriesPoint("2026-04-01", 0.09),
            ],
        }
    )
