#!/usr/bin/env python3
"""Regenera las tablas de series de docs/streams a partir del catálogo."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "tap_indec" / "catalog.json"
DOCS = ROOT / "docs" / "streams"
FREQUENCY_LABELS = {
    "daily": "diaria",
    "monthly": "mensual",
    "quarterly": "trimestral",
    "annual": "anual",
}

START = "<!-- series-table:start -->"
END = "<!-- series-table:end -->"


def dimensions_label(series: dict[str, Any]) -> str:
    parts = [f"{key}: {value}" for key, value in series["dimensions"].items() if value]
    return ", ".join(parts) if parts else "—"


def render_table(stream: dict[str, Any]) -> str:
    lines = [
        "| ID | Serie | Frecuencia | Desde | Hasta | Dimensiones |",
        "|---|---|---|---|---|---|",
    ]
    for series in stream["series"]:
        lines.append(
            "| `{id}` | {name} | {frequency} | {start} | {end} | {dims} |".format(
                id=series["id"],
                name=series["name"],
                frequency=FREQUENCY_LABELS.get(series["frequency"], series["frequency"]),
                start=series["start_date"],
                end=series["end_date"],
                dims=dimensions_label(series),
            )
        )
    return "\n".join(lines)


def replace_block(text: str, table: str, path: Path) -> str:
    if START not in text or END not in text:
        raise SystemExit(f"Faltan los marcadores de tabla en {path}")
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    return f"{before}{START}\n{table}\n{END}{after}"


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    for name, stream in catalog["streams"].items():
        path = DOCS / f"{name}.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(replace_block(text, render_table(stream), path), encoding="utf-8")
        print(f"{name}: {len(stream['series'])} series")


if __name__ == "__main__":
    main()
