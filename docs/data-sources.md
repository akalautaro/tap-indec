# Fuente de datos

El tap lee la API de series de `datos.gob.ar`, que publica la Subsecretaría de
Programación Macroeconómica con datos del INDEC. La API entrega JSON y acepta
filtros por fecha, así que sirve para replicación incremental.

## Endpoint

```
GET https://apis.datos.gob.ar/series/api/series/
```

Parámetros que usa el tap:

| Parámetro | Valor | Para qué |
|---|---|---|
| `ids` | ID de la serie | Elige la serie |
| `start_date` | `YYYY-MM-DD` | Primer período, inclusive |
| `end_date` | `YYYY-MM-DD` | Último período, inclusive |
| `limit` | entero hasta 1000 | Puntos por página |
| `start` | entero desde 0 | Offset de paginación |
| `format` | `json` | Formato de respuesta |

El tap pide una serie por request. Si manda varias y una no existe, la API
responde 400 y no devuelve ninguna. Con una por request, el error queda
acotado a la serie que falla.

## Respuesta

```json
{
  "data": [
    ["2016-12-01", 100.0],
    ["2017-01-01", 101.5859]
  ],
  "count": 119,
  "meta": [
    {"frequency": "month", "start_date": "2016-12-01", "end_date": "2017-01-01"},
    {
      "dataset": {"title": "Índice de Precios al Consumidor Nacional (IPC). Base diciembre 2016."},
      "distribution": {"downloadURL": "https://infra.datos.gob.ar/..."},
      "field": {"id": "145.3_INGNACNAL_DICI_M_15", "units": "Índice"}
    }
  ]
}
```

`data` viene ordenado por fecha ascendente. El primer elemento de cada fila es
la fecha y el segundo el valor. Un valor `null` significa que la fuente no
publicó ese período; el tap no emite la fila.

`count` es el total de puntos del rango, no la cantidad devuelta en la página.
El tap usa ese número para saber cuándo terminar de paginar.

## Fechas

La API usa el inicio del período:

| Frecuencia | Ejemplo | Significado |
|---|---|---|
| mensual | `2026-10-01` | Octubre de 2026 |
| trimestral | `2026-04-01` | Segundo trimestre de 2026 |
| anual | `2026-01-01` | Año 2026 |

No es la fecha de publicación. El IPC de octubre puede aparecer en la API a
mediados de noviembre.

## Verificar una serie

```bash
curl -s "https://apis.datos.gob.ar/series/api/series/?ids=145.3_INGNACNAL_DICI_M_15&limit=2&format=json" \
  | python3 -m json.tool
```

Si la serie no existe, la respuesta es:

```json
{"errors": [{"error": "Serie inexistente: NO_EXISTE"}], "failed_series": ["NO_EXISTE"]}
```

con HTTP 400.

## Búsqueda

La API tiene un endpoint de búsqueda para encontrar IDs:

```bash
curl -s "https://apis.datos.gob.ar/series/api/search/?q=EMAE&limit=20" \
  | python3 -m json.tool
```

Cada resultado trae `field.id`, `field.description`, `field.frequency` y el
dataset. El ID es lo que va en el catálogo.

La búsqueda pagina con `start` y acepta hasta 1000 resultados por request. El
dump de metadatos que publica datos.gob.ar puede estar atrasado; las fechas del
catálogo salen de `/series/`, no de ese dump.

## Descargas completas

Cada serie pertenece a una distribución con un CSV descargable. El catálogo
guarda esa URL en `download_url` para auditar los datos. El tap no descarga los
CSV: usa la API para poder filtrar por fecha.

## Límites y supuestos

- La API acepta hasta 40 IDs por request. El tap pide una serie por request, así
  que no depende de ese límite.
- Mezclar frecuencias en un mismo request colapsa la respuesta a la frecuencia
  más baja. El tap no mezcla: cada stream tiene una sola frecuencia.
- La API no documenta un rate limit explícito. El tap hace un request por serie,
  en serie, con reintentos ante 429 y 5xx.
- El máximo de puntos por página que usa el tap es 1000.
- Los valores se copian sin transformar. Las tasas de la EPH y las variaciones
  llegan como fracciones entre 0 y 1.
- Las revisiones de períodos viejos no se detectan en una corrida incremental.
  El tap vuelve a pedir el último punto de cada serie. Con `full_refresh: true`
  recarga desde `start_date` o desde la primera fecha disponible.
- Algunas series de la EPH están registradas y responden `available=true`, pero
  `/series/` devuelve cero filas. El catálogo excluye esas combinaciones.
- Si una serie se discontinúa, la API puede seguir devolviendo historia. El
  catálogo la marca con `active: false` y el tap la omite por defecto.
