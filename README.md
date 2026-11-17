# tap-indec

[![CI](https://github.com/akalautaro/tap-indec/actions/workflows/ci.yml/badge.svg)](https://github.com/akalautaro/tap-indec/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/akalautaro/tap-indec)](https://github.com/akalautaro/tap-indec/releases)

tap-indec extrae series estadísticas del INDEC desde la API de series de
datos.gob.ar y las emite como mensajes de [Singer](https://www.singer.io/).
Funciona como extractor de [Meltano](https://meltano.com/) y también se puede
correr suelto.

Emite tres streams con 76 series: `ipc`, `emae` y `mercado_trabajo`. La
replicación es incremental y el estado se guarda por serie.

## Requisitos

- Python 3.10 o superior
- Meltano 3.x (opcional, para usarlo como extractor)

## Instalación

Con Meltano:

```bash
meltano add --custom extractor tap-indec
```

Los valores del alta son:

| Campo | Valor |
|---|---|
| name | `tap-indec` |
| namespace | `tap_indec` |
| pip_url | `git+https://github.com/akalautaro/tap-indec.git@v0.1.0` |
| capabilities | `state`, `catalog`, `discover` |

También podés declararlo en `meltano.yml`:

```yaml
plugins:
  extractors:
    - name: tap-indec
      namespace: tap_indec
      pip_url: git+https://github.com/akalautaro/tap-indec.git@v0.1.0
      capabilities: [state, catalog, discover]
```

Sin Meltano, con [uv](https://docs.astral.sh/uv/):

```bash
uvx --from git+https://github.com/akalautaro/tap-indec.git@v0.1.0 tap-indec --help
```

O con pip:

```bash
pip install git+https://github.com/akalautaro/tap-indec.git@v0.1.0
```

## Configuración

| Setting | Tipo | Default | Obligatorio |
|---|---|---|---|
| `start_date` | fecha ISO 8601 | primera fecha de cada serie | no |
| `end_date` | fecha ISO 8601 | última fecha publicada | no |
| `api_url` | string | `https://apis.datos.gob.ar/series/api` | no |
| `timeout` | entero | `30` | no |
| `max_retries` | entero | `5` | no |
| `page_size` | entero | `1000` | no |
| `user_agent` | string | `tap-indec/0.1.0 ...` | no |
| `include_discontinued` | booleano | `false` | no |
| `fail_on_series_error` | booleano | `true` | no |
| `series` | objeto | todas las series | no |

`start_date` y `end_date` son inclusivos. Si no hay estado previo, cada serie
arranca en `start_date` o, si no se configuró, en su primera fecha disponible.

`series` limita las series por stream. Las claves son nombres de stream y los
valores, listas de IDs:

```json
{
  "start_date": "2016-01-01",
  "series": {
    "ipc": ["145.3_INGNACNAL_DICI_M_15"],
    "emae": ["11.3_VMATC_2004_M_12"]
  }
}
```

`fail_on_series_error` en `false` registra el error de una serie y sigue con la
próxima. El default corta el sync para no dejar huecos silenciosos.

## Uso

```bash
tap-indec --config config.json > records.jsonl
```

La salida es JSONL de Singer:

```json
{"type":"RECORD","stream":"ipc","record":{"series_id":"145.3_INGNACNAL_DICI_M_15","date":"2026-10-01","value":12785.9321,"series_name":"IPC Nivel General Nacional","unit":"Índice","frequency":"monthly","dataset":"Índice de Precios al Consumidor Nacional (IPC). Base diciembre 2016.","source":"INDEC","region":"Nacional","category":"Nivel general","measure":"Índice","base":"Diciembre 2016=100"},"time_extracted":"2026-11-17T02:57:47.829743+00:00"}
```

Para ver el catálogo:

```bash
tap-indec --config config.json --discover > catalog.json
```

Con Meltano:

```bash
meltano run tap-indec target-jsonl
meltano run tap-indec:ipc target-jsonl
```

## Streams

| Stream | Series | Qué mide | Frecuencia | Clave primaria |
|---|---:|---|---|---|
| `ipc` | 26 | Índice de Precios al Consumidor, nivel general y aperturas | mensual | `series_id`, `date` |
| `emae` | 22 | Estimador Mensual de Actividad Económica, nivel general y sectores | mensual | `series_id`, `date` |
| `mercado_trabajo` | 28 | Tasas de actividad, empleo, desempleo y subocupación de la EPH | trimestral | `series_id`, `date` |

Cada fila es un punto de una serie. `date` es el inicio del período, no la fecha
de publicación. `series_id` es el ID de la API y `series_name` el nombre legible.
Las aperturas van como columnas (`region`, `category`, `sector`, `aglomerado`,
`measure`, `geography_type`, `base`), no como streams separados.

El detalle de cada stream está en [`docs/streams/`](docs/streams/).

## Estado incremental

El tap pide cada serie desde su última fecha con valor y vuelve a pedir ese
último punto. Así corrige revisiones del dato más reciente sin recorrer la serie
completa. El estado queda en:

```json
{
  "bookmarks": {
    "ipc": {
      "series_last_dates": {
        "145.3_INGNACNAL_DICI_M_15": "2026-10-01"
      }
    }
  }
}
```

Si agregás una serie al catálogo, arranca desde su primera fecha o desde
`start_date`. Si una serie deja de publicarse, conserva su última fecha.

## Limitaciones

- El tap pide de a 1000 puntos por serie y pagina si la serie es más larga.
- La primera carga hace un request por serie. En la 0.1.0 son 76 requests.
- Los valores se copian tal como los publica la fuente. El tap no calcula
  variaciones, no desestacionaliza y no convierte unidades.
- Las series de variación del IPC y del EMAE se emiten como fracciones 0-1.
  `measure` y `unit` distinguen una variación de un índice.
- Las tasas de la EPH vienen como proporciones entre 0 y 1, aunque la fuente las
  rotule como porcentaje. El campo `unit` lo aclara.
- El total de `mercado_trabajo` es el total de 31 aglomerados urbanos, no el
  total nacional.
- La 0.1.0 incluye el total y seis aglomerados de la EPH. Las otras geografías
  de la API no están en el catálogo.
- Las revisiones de INDEC sobre períodos viejos no se detectan si quedan fuera
  del último punto. Para recargar historia, borrá el estado o mové `start_date`
  hacia atrás.
- No ingiere microdatos de la EPH ni archivos Excel del sitio de INDEC.
- Si una serie del catálogo deja de existir, el sync falla. Con
  `fail_on_series_error: false` se saltea y sigue.
- La API puede demorar la publicación del último período. El tap no inventa el
  dato faltante: no emite la fila.

## Desarrollo

```bash
uv sync --extra dev
make test          # tests unitarios con fixtures
make lint          # ruff
make typecheck     # mypy
make test-integration  # pega contra la API real
```

Los tests unitarios no usan red. Los de integración verifican que cada ID del
catálogo exista y devuelva datos.

Para agregar una serie, seguí [`CONTRIBUTING.md`](CONTRIBUTING.md). Los cambios
por versión están en [`CHANGELOG.md`](CHANGELOG.md) y el criterio de versionado
en [`docs/versionado.md`](docs/versionado.md).

## Licencia

El código se publica bajo Apache-2.0. Ver [`LICENSE`](LICENSE). Los datos son
del INDEC y se distribuyen desde datos.gob.ar; la licencia del código no cambia
los términos de la fuente.
