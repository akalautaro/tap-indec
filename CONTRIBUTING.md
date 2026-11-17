# Cómo contribuir

Gracias por tomarte el tiempo. Este tap se mantiene en español y con un
objetivo acotado: ingerir series del INDEC sin inventar datos ni esconder
problemas de la fuente.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/)
- Git

## Puesta en marcha

```bash
git clone git@github.com:akalautaro/tap-indec.git
cd tap-indec
uv sync --extra dev
uv run pytest
```

## Comandos útiles

```bash
make lint          # ruff check + format check
make format        # corrige formato e imports
make typecheck     # mypy
make test          # tests unitarios
make test-integration  # pega contra la API real de datos.gob.ar
```

## Agregar una serie al catálogo

1. Verificá que el ID exista y devuelva datos:

   ```bash
   curl -s "https://apis.datos.gob.ar/series/api/series/?ids=TU_ID&limit=2&format=json" | python3 -m json.tool
   ```

2. Agregá la serie en `tap_indec/catalog.json`, dentro del stream que
   corresponda (`ipc`, `emae` o `mercado_trabajo`).
3. Completá `frequency`, `units`, `start_date`, `end_date`, `dataset` y
   `dimensions`. Las dimensiones permitidas están en
   `tap_indec/streams.py`.
4. Corré `uv run pytest` y `uv run pytest -m integration -k TU_ID`.

Los IDs no se inventan. Si una serie no existe, no entra.

## Estilo

- Código, nombres de variables y mensajes de log en inglés.
- README, docs y mensajes de usuario en español.
- Docstrings cortos, en español, sin repetir el nombre de la función.
- Nada de comentarios que expliquen lo obvio.

## Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(ipc): agrega apertura por regiones
fix(client): reintenta ante 429
docs(readme): aclara el estado incremental
test(emae): cubre series sin datos
chore(deps): actualiza singer-sdk
```

Un commit por cambio lógico. El título en tercera persona y en español.

## Pull requests

- Un PR por tema.
- Describí qué cambia y cómo lo probaste.
- Si agregás una serie, pegá el ID y la salida de la verificación.
- El CI tiene que pasar en todas las versiones de Python.
- Si el cambio afecta el esquema o el estado, actualizá `CHANGELOG.md`.

## Reportar problemas

Abrí un issue con:

- versión del tap (`tap-indec --version`),
- comando que ejecutaste,
- configuración relevante (sin secretos),
- salida de error completa.
