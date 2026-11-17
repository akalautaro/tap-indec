"""Tests de descubrimiento, configuración y catálogo."""

from __future__ import annotations

import json

import pytest

from tap_indec.streams import DIMENSION_TYPES, load_catalog
from tap_indec.tap import TapIndec

ALLOWED_FREQUENCIES = {"daily", "monthly", "quarterly", "annual", "unknown"}
REQUIRED_SERIES_FIELDS = {
    "id",
    "name",
    "frequency",
    "units",
    "start_date",
    "end_date",
    "dataset",
    "dimensions",
    "active",
}


def test_tap_discovers_three_streams(tap: TapIndec) -> None:
    assert set(tap.streams) == {"ipc", "emae", "mercado_trabajo"}


def test_discovery_is_valid_json(tap: TapIndec) -> None:
    payload = json.loads(tap.catalog_json_text)

    assert {stream["stream"] for stream in payload["streams"]} == {
        "ipc",
        "emae",
        "mercado_trabajo",
    }


def test_streams_are_incremental(tap: TapIndec) -> None:
    for stream in tap.streams.values():
        assert stream.replication_method == "INCREMENTAL"
        assert stream.replication_key == "date"


def test_config_schema_has_expected_properties(tap: TapIndec) -> None:
    properties = tap.config_jsonschema["properties"]

    assert {
        "start_date",
        "end_date",
        "api_url",
        "timeout",
        "max_retries",
        "page_size",
        "user_agent",
        "include_discontinued",
        "fail_on_series_error",
        "series",
    } <= set(properties)


def test_catalog_has_three_streams() -> None:
    catalog = load_catalog()

    assert set(catalog["streams"]) == {"ipc", "emae", "mercado_trabajo"}
    for name, stream in catalog["streams"].items():
        assert stream["series"], f"El stream {name} no tiene series"


def test_catalog_series_are_well_formed() -> None:
    catalog = load_catalog()
    seen: set[str] = set()

    for stream_name, stream in catalog["streams"].items():
        for series in stream["series"]:
            missing = REQUIRED_SERIES_FIELDS - set(series)
            assert not missing, f"{series.get('id')} no tiene {missing}"
            assert series["id"] not in seen, f"Serie duplicada: {series['id']}"
            seen.add(series["id"])
            assert series["frequency"] in ALLOWED_FREQUENCIES, (
                f"Frecuencia inválida en {series['id']}: {series['frequency']}"
            )
            assert series["start_date"] <= series["end_date"], f"Rango inválido en {series['id']}"
            unknown_dims = set(series["dimensions"]) - set(DIMENSION_TYPES)
            assert not unknown_dims, f"Dimensiones desconocidas en {series['id']}: {unknown_dims}"
            assert stream_name in {"ipc", "emae", "mercado_trabajo"}


def test_catalog_ids_are_unique() -> None:
    catalog = load_catalog()
    ids = [series["id"] for stream in catalog["streams"].values() for series in stream["series"]]

    assert len(ids) == len(set(ids))


def test_schema_contains_dimension_columns(tap: TapIndec) -> None:
    ipc_props = tap.streams["ipc"].schema["properties"]
    emae_props = tap.streams["emae"].schema["properties"]
    mt_props = tap.streams["mercado_trabajo"].schema["properties"]

    assert {"region", "category", "measure", "base"} <= set(ipc_props)
    assert {"sector", "measure", "base"} <= set(emae_props)
    assert {"aglomerado", "measure", "geography_type"} <= set(mt_props)


@pytest.mark.integration
def test_catalog_series_exist_in_the_api() -> None:
    from tap_indec.client import IndecClient

    catalog = load_catalog()
    client = IndecClient(timeout=30)

    failures: list[str] = []
    for stream in catalog["streams"].values():
        for series in stream["series"]:
            try:
                result = client.fetch_series(series["id"], page_size=1000)
            except Exception as exc:
                failures.append(f"{series['id']}: {exc}")
                continue
            if result.count == 0:
                failures.append(f"{series['id']}: sin datos")

    assert not failures, "Series con problemas:\n" + "\n".join(failures)
