# Troubleshooting

## El tap no emite nada

Revisá el rango. Si `start_date` es posterior al último período publicado, la
API devuelve `data: []` y el tap no emite filas. Probá sin `start_date` o con una
fecha anterior.

```bash
tap-indec --config config.json --discover
```

Si el catálogo sale vacío, el problema es de configuración, no de la API.

## `IndecAPIError: API returned 400 ... Serie inexistente`

El ID del catálogo no existe o la API lo dio de baja. Verificalo:

```bash
curl -s "https://apis.datos.gob.ar/series/api/series/?ids=TU_ID&limit=1&format=json"
```

Si el ID murió, sacalo de `tap_indec/catalog.json` o marcalo con
`"active": false`. Si querés que el sync siga con las demás series mientras
tanto:

```json
{"fail_on_series_error": false}
```

El tap registra un warning con el ID y continúa. Al final no vas a tener filas
de esa serie.

## `API returned 429`

La API está limitando los requests. Subí `max_retries` o espaciá las corridas.
El tap reintenta solo ante 429 y 5xx, con backoff exponencial.

## `API returned 502` o `503`

Error transitorio de la API. El tap reintenta `max_retries` veces. Si persiste,
probá de nuevo en unos minutos. El estado no avanza si no se emiten registros.

## Las tasas de `mercado_trabajo` son chicas

La EPH publica proporciones, no porcentajes. `0.079` es 7,9 %. Multiplicá por
100 en el destino o en el modelo de dbt. El campo `unit` dice
`Proporción (0-1)`. El total del stream es de 31 aglomerados urbanos, no
nacional.

## El estado no avanza

Mirá el último mensaje `STATE`:

```json
{"bookmarks": {"ipc": {"series_last_dates": {"145.3_INGNACNAL_DICI_M_15": "2026-10-01"}}}}
```

Si la fecha es la misma que la última corrida, la API no publicó un período
nuevo. Si la fecha es vieja y hay datos nuevos, revisá que el target esté
procesando los mensajes y que `start_date` no esté filtrando de más.

## Cambió el esquema después de actualizar el tap

Volvé a correr el discovery y actualizá el catálogo del target:

```bash
tap-indec --config config.json --discover > catalog.json
```

Meltano lo hace solo cuando corre `meltano run`.

## Una serie nueva no aparece

El tap no descubre series por su cuenta. Solo emite las que están en
`tap_indec/catalog.json`. Agregala y corré los tests de integración:

```bash
uv run pytest -m integration -k TU_ID
```

## El sync falla en la primera corrida y no en la segunda

Puede ser un problema de estado, no de fechas. La API recorta un `start_date`
anterior al inicio de la serie y devuelve `data: []` si el rango queda después
del último período. Ninguno de los dos casos da error.

Si el tap falla, mirá el ID y el código HTTP del mensaje. Un 400 suele ser una
serie inexistente; un 5xx es transitorio y se reintenta.
