"""Tests de los streams y de la lógica incremental."""

from __future__ import annotations

from typing import Any

import jsonschema
import pytest

from tap_indec.client import IndecAPIError, SeriesPoint, SeriesResult
from tap_indec.streams import SeriesSpec
from tap_indec.tap import TapIndec


def _bind(stream: Any, client: Any) -> Any:
    stream._client = client
    return stream


def test_ipc_emits_records_and_skips_nulls(tap: TapIndec, fake_client: Any) -> None:
    stream = _bind(tap.streams["ipc"], fake_client)

    records = list(stream.get_records({}))

    assert len(records) == 2
    assert records[0]["series_id"] == "145.3_INGNACNAL_DICI_M_15"
    assert records[0]["date"] == "2026-08-01"
    assert records[0]["value"] == 100.0
    assert records[0]["region"] == "Nacional"
    assert records[0]["category"] == "Nivel general"
    assert records[0]["measure"] == "Índice"
    assert records[0]["base"] == "Diciembre 2016=100"


def test_records_validate_against_schema(tap: TapIndec, fake_client: Any) -> None:
    stream = _bind(tap.streams["ipc"], fake_client)

    for record in stream.get_records({}):
        jsonschema.validate(record, stream.schema)


def test_primary_keys_and_replication_key(tap: TapIndec) -> None:
    stream = tap.streams["emae"]

    assert stream.primary_keys == ["series_id", "date"]
    assert stream.replication_key == "date"


def test_state_advances_per_series(tap: TapIndec, fake_client: Any) -> None:
    stream = _bind(tap.streams["ipc"], fake_client)

    list(stream.get_records({}))

    state = stream.stream_state["series_last_dates"]
    assert state["145.3_INGNACNAL_DICI_M_15"] == "2026-09-01"


def test_incremental_start_uses_state(config: dict[str, Any], fake_client: Any) -> None:
    tap = TapIndec(
        config=config,
        state={
            "bookmarks": {"ipc": {"series_last_dates": {"145.3_INGNACNAL_DICI_M_15": "2026-09-01"}}}
        },
        parse_env_config=False,
    )
    stream = _bind(tap.streams["ipc"], fake_client)

    list(stream.get_records({}))

    assert fake_client.calls[0] == (
        "145.3_INGNACNAL_DICI_M_15",
        "2026-09-01",
        None,
    )


def test_start_date_is_used_without_state(config: dict[str, Any], fake_client: Any) -> None:
    tap = TapIndec(config=config, parse_env_config=False)
    stream = _bind(tap.streams["ipc"], fake_client)

    list(stream.get_records({}))

    assert fake_client.calls[0][1] == "2026-01-01"


def test_empty_range_emits_nothing_and_keeps_state(
    config: dict[str, Any],
) -> None:
    class EmptyClient:
        def fetch_series(self, series_id: str, **kwargs: Any) -> SeriesResult:
            return SeriesResult(series_id=series_id, points=[], count=0)

    tap = TapIndec(config=config, parse_env_config=False)
    stream = _bind(tap.streams["ipc"], EmptyClient())

    assert list(stream.get_records({})) == []
    assert stream.stream_state["series_last_dates"] == {}


def test_series_filter(config: dict[str, Any]) -> None:
    config = {**config, "series": {"ipc": ["145.3_INGNACNAL_DICI_M_15"]}}
    tap = TapIndec(config=config, parse_env_config=False)

    stream = tap.streams["ipc"]

    assert [spec.id for spec in stream.series] == ["145.3_INGNACNAL_DICI_M_15"]


def test_series_filter_with_unknown_id(config: dict[str, Any]) -> None:
    config = {**config, "series": {"ipc": ["NO_EXISTE"]}}
    tap = TapIndec(config=config, parse_env_config=False)

    assert tap.streams["ipc"].series == []


def test_discontinued_series_are_excluded_by_default(
    config: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    catalog = {
        "streams": {
            "ipc": {
                "series": [
                    {
                        "id": "ACTIVA",
                        "name": "Activa",
                        "frequency": "monthly",
                        "units": "Índice",
                        "start_date": "2020-01-01",
                        "end_date": "2026-01-01",
                        "dataset": "Test",
                        "dimensions": {"region": "Nacional"},
                        "active": True,
                    },
                    {
                        "id": "VIEJA",
                        "name": "Vieja",
                        "frequency": "monthly",
                        "units": "Índice",
                        "start_date": "2000-01-01",
                        "end_date": "2010-01-01",
                        "dataset": "Test",
                        "dimensions": {"region": "Nacional"},
                        "active": False,
                    },
                ]
            }
        }
    }
    monkeypatch.setattr("tap_indec.streams.load_catalog", lambda: catalog)

    tap = TapIndec(config=config, parse_env_config=False)
    assert [spec.id for spec in tap.streams["ipc"].series] == ["ACTIVA"]

    config = {**config, "include_discontinued": True}
    tap = TapIndec(config=config, parse_env_config=False)
    assert [spec.id for spec in tap.streams["ipc"].series] == ["ACTIVA", "VIEJA"]


def test_series_error_can_be_skipped(config: dict[str, Any]) -> None:
    class BrokenClient:
        def fetch_series(self, series_id: str, **kwargs: Any) -> SeriesResult:
            raise IndecAPIError("boom")

    config = {**config, "fail_on_series_error": False}
    tap = TapIndec(config=config, parse_env_config=False)
    stream = _bind(tap.streams["ipc"], BrokenClient())

    assert list(stream.get_records({})) == []


def test_series_error_fails_by_default(config: dict[str, Any]) -> None:
    class BrokenClient:
        def fetch_series(self, series_id: str, **kwargs: Any) -> SeriesResult:
            raise IndecAPIError("boom")

    tap = TapIndec(config=config, parse_env_config=False)
    stream = _bind(tap.streams["ipc"], BrokenClient())

    with pytest.raises(IndecAPIError):
        list(stream.get_records({}))


def test_dimensions_are_stream_specific(tap: TapIndec) -> None:
    assert tap.streams["ipc"].dimensions == {"region", "category", "measure", "base"}
    assert tap.streams["emae"].dimensions == {"sector", "measure", "base"}
    assert tap.streams["mercado_trabajo"].dimensions == {
        "aglomerado",
        "measure",
        "geography_type",
    }


def test_series_spec_defaults() -> None:
    spec = SeriesSpec.from_dict({"id": "X", "name": "Serie X"})

    assert spec.id == "X"
    assert spec.frequency == "unknown"
    assert spec.active is True
    assert spec.dimensions == {}


def test_records_include_null_dimensions(tap: TapIndec) -> None:
    class OneSeriesClient:
        def fetch_series(self, series_id: str, **kwargs: Any) -> SeriesResult:
            return SeriesResult(
                series_id=series_id,
                points=[SeriesPoint("2026-01-01", 1.0)],
                count=1,
            )

    stream = _bind(tap.streams["emae"], OneSeriesClient())
    record = next(iter(stream.get_records({})))

    assert record["sector"] == "Nivel general"
    assert record["measure"] == "Serie original"
    assert record["base"] == "2004=100"
    assert "region" not in record


def test_client_uses_configured_user_agent(config: dict[str, Any], requests_mock: Any) -> None:
    from tap_indec.client import IndecClient

    requests_mock.get(
        "https://api.test/series/api/series/",
        json={"data": [["2026-01-01", 1.0]], "count": 1},
    )
    tap = TapIndec(config={**config, "user_agent": "tap-indec-test/9"}, parse_env_config=False)
    stream = tap.streams["ipc"]
    stream._client = IndecClient(api_url=config["api_url"], user_agent=tap.config["user_agent"])

    list(stream.get_records({}))

    assert requests_mock.last_request.headers["User-Agent"] == "tap-indec-test/9"
