# Fixtures

Respuestas reales de la API de series de datos.gob.ar, recortadas al rango que
necesitan los tests. Se usan para que los tests unitarios no dependan de la red.

| Archivo | Serie | Fecha de captura |
|---|---|---|
| `ipc_nivel_general.json` | `145.3_INGNACNAL_DICI_M_15` | 2026-11-17 |
| `emae_construccion.json` | `11.3_VMATC_2004_M_12` | 2026-11-17 |
| `eph_desocupacion.json` | `45.2_ECTDT_0_T_33` | 2026-11-17 |
| `ipc_empty_range.json` | `145.3_INGNACNAL_DICI_M_15` con `start_date=2030-01-01` | 2026-11-17 |
| `error_serie_inexistente.json` | ID inexistente | 2026-11-17 |

Para regenerarlos:

```bash
curl -s "https://apis.datos.gob.ar/series/api/series/?ids=145.3_INGNACNAL_DICI_M_15&limit=1000&format=json" \
  | python3 -m json.tool > tests/fixtures/ipc_nivel_general.json
```

Los fixtures conservan la forma completa de la respuesta (`data`, `count`,
`meta`) para que el cliente se pruebe contra el contrato real, no contra una
versión simplificada.
