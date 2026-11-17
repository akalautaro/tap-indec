# Stream `ipc`

Índice de Precios al Consumidor. El stream emite 26 series mensuales: nivel
general nacional, nivel general por las seis regiones, las 12 divisiones de la
canasta, bienes y servicios, las categorías núcleo/regulados/estacionales y dos
series de variación.

## Granularidad y clave

Una fila por serie y período. La clave primaria es `series_id` + `date` y la
replicación es incremental por `date`.

`date` es el primer día del mes del período. El valor de octubre de 2026 se
emite como `2026-10-01`. No es la fecha de publicación.

Las aperturas van en las columnas `region`, `category`, `measure` y `base`:

| Columna | Valores |
|---|---|
| `region` | `Nacional`, `GBA`, `Región Pampeana`, `Región Noreste`, `Región Noroeste`, `Región Cuyo`, `Región Patagonia` |
| `category` | `Nivel general`, divisiones de la canasta, `Bienes`, `Servicios`, `Núcleo`, `Regulados`, `Estacionales` |
| `measure` | `Índice`, `Variación mensual`, `Variación acumulada anual` |
| `base` | `Diciembre 2016=100` en las series de índice; nulo en las de variación |

`category` usa la etiqueta de la fuente. `Bienes` y `Servicios` son agregados,
no divisiones de la canasta. No armes una jerarquía con esos valores.

## Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `series_id` | string | ID de la serie en la API |
| `date` | date | Primer día del mes |
| `value` | number \| null | Índice o variación, según `measure` |
| `series_name` | string | Nombre legible de la serie |
| `unit` | string \| null | Unidad del valor |
| `frequency` | string | `monthly` |
| `dataset` | string \| null | Dataset de origen |
| `source` | string | `INDEC` |
| `region` | string \| null | Región estadística |
| `category` | string \| null | Categoría o división |
| `measure` | string \| null | Índice o tipo de variación |
| `base` | string \| null | Base del índice |

## Series

<!-- series-table:start -->
| ID | Serie | Frecuencia | Desde | Hasta | Dimensiones |
|---|---|---|---|---|---|
| `145.3_INGNACNAL_DICI_M_15` | IPC Nivel General Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGNACUAL_DICI_M_38` | IPC Nivel General Nacional - variación mensual | mensual | 2017-01-01 | 2026-10-01 | region: Nacional, category: Nivel general, measure: Variación mensual |
| `145.3_INGNACIOR_DICI_M_57` | IPC Nivel General Nacional - variación acumulada anual | mensual | 2017-01-01 | 2026-10-01 | region: Nacional, category: Nivel general, measure: Variación acumulada anual |
| `145.3_INGGBAGBA_DICI_M_10` | IPC Nivel General GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGPAMANA_DICI_M_15` | IPC Nivel General Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGNEANEA_DICI_M_10` | IPC Nivel General Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGNOANOA_DICI_M_10` | IPC Nivel General Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGCUYUYO_DICI_M_11` | IPC Nivel General Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `145.3_INGPATNIA_DICI_M_16` | IPC Nivel General Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Nivel general, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENNAL_DICI_M_45` | IPC Alimentos y bebidas no alcohólicas - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDANAL_DICI_M_39` | IPC Bebidas alcohólicas y tabaco - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDANAL_DICI_M_35` | IPC Prendas de vestir y calzado - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENNAL_DICI_M_52` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPANAL_DICI_M_46` | IPC Equipamiento y mantenimiento del hogar - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDNAL_DICI_M_18` | IPC Salud - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPNAL_DICI_M_23` | IPC Transporte - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNINAL_DICI_M_27` | IPC Comunicaciones - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREANAL_DICI_M_31` | IPC Recreación y cultura - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACNAL_DICI_M_22` | IPC Educación - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUNAL_DICI_M_33` | IPC Restaurantes y hoteles - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESNAL_DICI_M_36` | IPC Bienes y servicios varios - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `147.3_IBIENESNAL_DICI_T_19` | IPC Bienes - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Bienes, measure: Índice, base: Diciembre 2016=100 |
| `147.3_ISERVICNAL_DICI_T_22` | IPC Servicios - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Servicios, measure: Índice, base: Diciembre 2016=100 |
| `148.3_INUCLEONAL_DICI_M_19` | IPC Núcleo - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Núcleo, measure: Índice, base: Diciembre 2016=100 |
| `148.3_IREGULANAL_DICI_M_22` | IPC Regulados - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Regulados, measure: Índice, base: Diciembre 2016=100 |
| `148.3_IESTACINAL_DICI_M_25` | IPC Estacionales - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Estacionales, measure: Índice, base: Diciembre 2016=100 |
<!-- series-table:end -->

## Unidades

Las series de índice se publican con base diciembre 2016=100. Las de variación
vienen como fracción entre -1 y 1: `0.025` es 2,5 %. El campo `unit` distingue
cada caso. Si necesitás porcentaje, multiplicá por 100 en el modelo de dbt.

## Nulos y demoras

`value` es nulo cuando la API devuelve un punto sin dato. El tap no emite esa
fila. Si INDEC todavía no publicó el mes, el stream termina en el último
período publicado.

El tap vuelve a pedir el último punto de cada serie en cada corrida. Si INDEC
revisa ese valor, la próxima extracción trae el valor corregido. Las revisiones
de períodos más viejos no se detectan salvo que muevas `start_date` hacia atrás.

## Ejemplo

```json
{
  "series_id": "145.3_INGNACNAL_DICI_M_15",
  "date": "2026-10-01",
  "value": 12785.9321,
  "series_name": "IPC Nivel General Nacional",
  "unit": "Índice",
  "frequency": "monthly",
  "dataset": "Índice de Precios al Consumidor Nacional (IPC). Base diciembre 2016.",
  "source": "INDEC",
  "region": "Nacional",
  "category": "Nivel general",
  "measure": "Índice",
  "base": "Diciembre 2016=100"
}
```
