# Streams

| Stream | Frecuencia | Series | Qué emite |
|---|---|---:|---|
| [`ipc`](ipc.md) | mensual | 98 | Índice de Precios al Consumidor |
| [`emae`](emae.md) | mensual | 22 | Estimador Mensual de Actividad Económica |
| [`mercado_trabajo`](mercado_trabajo.md) | trimestral | 123 | Tasas de la Encuesta Permanente de Hogares |

Los tres comparten la clave primaria `series_id` + `date`. La diferencia está
en las columnas de apertura:

| Stream | Dimensiones |
|---|---|
| `ipc` | `region`, `category`, `measure`, `base` |
| `emae` | `sector`, `measure`, `base` |
| `mercado_trabajo` | `aglomerado`, `measure`, `geography_type` |

El total de `mercado_trabajo` es el total de 31 aglomerados urbanos, no el total
nacional.
