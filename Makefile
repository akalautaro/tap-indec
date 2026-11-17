.PHONY: install lint format typecheck test test-integration coverage build docs clean

install:
	uv sync --extra dev

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

typecheck:
	uv run mypy tap_indec

test:
	uv run pytest

test-integration:
	uv run pytest -m integration -v

coverage:
	uv run pytest --cov=tap_indec --cov-report=term-missing

build:
	uv build

docs:
	uv run python scripts/render_docs.py

clean:
	rm -rf dist build .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov coverage.xml
