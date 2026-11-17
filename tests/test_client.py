"""Tests del cliente HTTP."""

from __future__ import annotations

from typing import Any
from urllib.parse import parse_qs, urlsplit

import pytest
import requests
import requests_mock

from tap_indec.client import IndecAPIError, IndecClient

API_URL = "https://api.test/series/api"


def test_fetch_series_returns_points(
    requests_mock: requests_mock.Mocker, load_fixture: Any
) -> None:
    requests_mock.get(f"{API_URL}/series/", json=load_fixture("ipc_nivel_general.json"))
    client = IndecClient(api_url=API_URL)

    result = client.fetch_series("145.3_INGNACNAL_DICI_M_15")

    assert result.count == 119
    assert len(result.points) == 119
    assert result.points[0].date == "2016-12-01"
    assert result.points[0].value == pytest.approx(100.0)
    assert result.last_date == "2026-10-01"
    assert result.meta["field"]["id"] == "145.3_INGNACNAL_DICI_M_15"


def test_fetch_series_sends_date_filters(
    requests_mock: requests_mock.Mocker, load_fixture: Any
) -> None:
    matcher = requests_mock.get(f"{API_URL}/series/", json=load_fixture("ipc_nivel_general.json"))
    client = IndecClient(api_url=API_URL)

    client.fetch_series("145.3_INGNACNAL_DICI_M_15", start_date="2026-01-01", end_date="2026-10-01")

    query = parse_qs(urlsplit(matcher.last_request.url).query)
    assert query["start_date"] == ["2026-01-01"]
    assert query["end_date"] == ["2026-10-01"]
    assert query["ids"] == ["145.3_INGNACNAL_DICI_M_15"]
    assert query["start"] == ["0"]


def test_fetch_series_paginates(requests_mock: requests_mock.Mocker, load_fixture: Any) -> None:
    payload = load_fixture("ipc_nivel_general.json")
    rows: list[list[Any]] = payload["data"]

    def callback(request: Any, context: Any) -> dict[str, Any]:
        start = int(request.qs["start"][0])
        limit = int(request.qs["limit"][0])
        return {
            "data": rows[start : start + limit],
            "count": len(rows),
            "meta": payload["meta"],
        }

    requests_mock.get(f"{API_URL}/series/", json=callback)
    client = IndecClient(api_url=API_URL, page_size=50)

    result = client.fetch_series("145.3_INGNACNAL_DICI_M_15")

    assert len(result.points) == len(rows)
    assert requests_mock.call_count == 3


def test_fetch_series_handles_nulls(requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get(
        f"{API_URL}/series/",
        json={"data": [["2026-01-01", None], ["2026-02-01", 1.5]], "count": 2},
    )
    client = IndecClient(api_url=API_URL)

    result = client.fetch_series("serie")

    assert result.points[0].value is None
    assert result.points[1].value == 1.5
    assert result.last_date == "2026-02-01"


def test_fetch_series_raises_on_api_error(
    requests_mock: requests_mock.Mocker, load_fixture: Any
) -> None:
    requests_mock.get(
        f"{API_URL}/series/",
        status_code=400,
        json=load_fixture("error_serie_inexistente.json"),
    )
    client = IndecClient(api_url=API_URL)

    with pytest.raises(IndecAPIError, match="Serie inexistente"):
        client.fetch_series("NO_EXISTE")


def test_fetch_series_raises_on_unexpected_shape(
    requests_mock: requests_mock.Mocker,
) -> None:
    requests_mock.get(f"{API_URL}/series/", json={"count": 1, "data": "nope"})
    client = IndecClient(api_url=API_URL)

    with pytest.raises(IndecAPIError, match="has no 'data' list"):
        client.fetch_series("serie")


def test_fetch_series_raises_on_non_numeric_value(
    requests_mock: requests_mock.Mocker,
) -> None:
    requests_mock.get(
        f"{API_URL}/series/",
        json={"data": [["2026-01-01", "no-es-un-numero"]], "count": 1},
    )
    client = IndecClient(api_url=API_URL)

    with pytest.raises(IndecAPIError, match="Non-numeric value"):
        client.fetch_series("serie")


def test_fetch_series_wraps_network_errors(requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get(f"{API_URL}/series/", exc=requests.ConnectionError("boom"))
    client = IndecClient(api_url=API_URL, max_retries=0)

    with pytest.raises(IndecAPIError, match="Network error"):
        client.fetch_series("serie")


def test_client_is_a_context_manager() -> None:
    with IndecClient(api_url=API_URL) as client:
        assert isinstance(client, IndecClient)


def test_retry_policy_covers_transient_errors() -> None:
    client = IndecClient(api_url=API_URL, max_retries=3)
    adapter = client._session.get_adapter("https://api.test")

    assert adapter.max_retries.total == 3
    assert 429 in adapter.max_retries.status_forcelist
    assert 503 in adapter.max_retries.status_forcelist


def test_fetch_series_clamps_page_size(
    requests_mock: requests_mock.Mocker, load_fixture: Any
) -> None:
    matcher = requests_mock.get(f"{API_URL}/series/", json=load_fixture("ipc_nivel_general.json"))
    client = IndecClient(api_url=API_URL, page_size=5000)

    client.fetch_series("145.3_INGNACNAL_DICI_M_15")

    assert matcher.last_request.qs["limit"] == ["1000"]
