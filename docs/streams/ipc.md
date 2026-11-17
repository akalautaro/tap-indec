# Stream `ipc`

Índice de Precios al Consumidor. El stream emite 98 series mensuales: nivel
general nacional, nivel general por las seis regiones, las 12 divisiones de la
canasta por cada una de las siete regiones, bienes y servicios, las categorías
núcleo/regulados/estacionales y dos series de variación.

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

Las 12 divisiones se publican para las siete regiones. Eso da 84 series de
índice, además del nivel general y los agregados. La combinación
`region` + `category` identifica la apertura; `series_id` sigue siendo la clave
estable.

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
| `146.3_IALIMENGBA_DICI_M_40` | IPC Alimentos y bebidas no alcohólicas - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENANA_DICI_M_45` | IPC Alimentos y bebidas no alcohólicas - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENNEA_DICI_M_40` | IPC Alimentos y bebidas no alcohólicas - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENNOA_DICI_M_40` | IPC Alimentos y bebidas no alcohólicas - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENUYO_DICI_M_41` | IPC Alimentos y bebidas no alcohólicas - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IALIMENNIA_DICI_M_46` | IPC Alimentos y bebidas no alcohólicas - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Alimentos y bebidas no alcohólicas, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDANAL_DICI_M_39` | IPC Bebidas alcohólicas y tabaco - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDAGBA_DICI_M_34` | IPC Bebidas alcohólicas y tabaco - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDAANA_DICI_M_39` | IPC Bebidas alcohólicas y tabaco - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDANEA_DICI_M_34` | IPC Bebidas alcohólicas y tabaco - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDANOA_DICI_M_34` | IPC Bebidas alcohólicas y tabaco - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDAUYO_DICI_M_35` | IPC Bebidas alcohólicas y tabaco - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBEBIDANIA_DICI_M_40` | IPC Bebidas alcohólicas y tabaco - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Bebidas alcohólicas y tabaco, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDANAL_DICI_M_35` | IPC Prendas de vestir y calzado - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDAGBA_DICI_M_30` | IPC Prendas de vestir y calzado - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDAANA_DICI_M_35` | IPC Prendas de vestir y calzado - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDANEA_DICI_M_30` | IPC Prendas de vestir y calzado - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDANOA_DICI_M_30` | IPC Prendas de vestir y calzado - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDAUYO_DICI_M_31` | IPC Prendas de vestir y calzado - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IPRENDANIA_DICI_M_36` | IPC Prendas de vestir y calzado - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Prendas de vestir y calzado, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENNAL_DICI_M_52` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENGBA_DICI_M_47` | IPC Vivienda, agua, electricidad, gas y otros combustibles - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENANA_DICI_M_52` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENNEA_DICI_M_47` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENNOA_DICI_M_47` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENUYO_DICI_M_48` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IVIVIENNIA_DICI_M_53` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Vivienda, agua, electricidad, gas y otros combustibles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPANAL_DICI_M_46` | IPC Equipamiento y mantenimiento del hogar - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPAGBA_DICI_M_41` | IPC Equipamiento y mantenimiento del hogar - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPAANA_DICI_M_46` | IPC Equipamiento y mantenimiento del hogar - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPANEA_DICI_M_41` | IPC Equipamiento y mantenimiento del hogar - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPANOA_DICI_M_41` | IPC Equipamiento y mantenimiento del hogar - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPAUYO_DICI_M_42` | IPC Equipamiento y mantenimiento del hogar - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEQUIPANIA_DICI_M_47` | IPC Equipamiento y mantenimiento del hogar - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Equipamiento y mantenimiento del hogar, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDNAL_DICI_M_18` | IPC Salud - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDGBA_DICI_M_13` | IPC Salud - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDANA_DICI_M_18` | IPC Salud - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDNEA_DICI_M_13` | IPC Salud - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDNOA_DICI_M_13` | IPC Salud - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDUYO_DICI_M_14` | IPC Salud - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ISALUDNIA_DICI_M_19` | IPC Salud - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Salud, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPNAL_DICI_M_23` | IPC Transporte - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPGBA_DICI_M_18` | IPC Transporte - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPANA_DICI_M_23` | IPC Transporte - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPNEA_DICI_M_18` | IPC Transporte - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPNOA_DICI_M_18` | IPC Transporte - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPUYO_DICI_M_19` | IPC Transporte - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ITRANSPNIA_DICI_M_24` | IPC Transporte - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Transporte, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNINAL_DICI_M_27` | IPC Comunicaciones - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNIGBA_DICI_M_22` | IPC Comunicaciones - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNIANA_DICI_M_27` | IPC Comunicaciones - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNINEA_DICI_M_22` | IPC Comunicaciones - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNINOA_DICI_M_22` | IPC Comunicaciones - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNIUYO_DICI_M_23` | IPC Comunicaciones - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_ICOMUNINIA_DICI_M_28` | IPC Comunicaciones - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Comunicaciones, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREANAL_DICI_M_31` | IPC Recreación y cultura - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREAGBA_DICI_M_26` | IPC Recreación y cultura - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREAANA_DICI_M_31` | IPC Recreación y cultura - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREANEA_DICI_M_26` | IPC Recreación y cultura - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREANOA_DICI_M_26` | IPC Recreación y cultura - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREAUYO_DICI_M_27` | IPC Recreación y cultura - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRECREANIA_DICI_M_32` | IPC Recreación y cultura - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Recreación y cultura, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACNAL_DICI_M_22` | IPC Educación - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACGBA_DICI_M_17` | IPC Educación - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACANA_DICI_M_22` | IPC Educación - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACNEA_DICI_M_17` | IPC Educación - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACNOA_DICI_M_17` | IPC Educación - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACUYO_DICI_M_18` | IPC Educación - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IEDUCACNIA_DICI_M_23` | IPC Educación - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Educación, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUNAL_DICI_M_33` | IPC Restaurantes y hoteles - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUGBA_DICI_M_28` | IPC Restaurantes y hoteles - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUANA_DICI_M_33` | IPC Restaurantes y hoteles - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUNEA_DICI_M_28` | IPC Restaurantes y hoteles - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUNOA_DICI_M_28` | IPC Restaurantes y hoteles - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUUYO_DICI_M_29` | IPC Restaurantes y hoteles - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IRESTAUNIA_DICI_M_34` | IPC Restaurantes y hoteles - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Restaurantes y hoteles, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESNAL_DICI_M_36` | IPC Bienes y servicios varios - Nacional | mensual | 2016-12-01 | 2026-10-01 | region: Nacional, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESGBA_DICI_M_31` | IPC Bienes y servicios varios - GBA | mensual | 2016-12-01 | 2026-10-01 | region: GBA, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESANA_DICI_M_36` | IPC Bienes y servicios varios - Región Pampeana | mensual | 2016-12-01 | 2026-10-01 | region: Región Pampeana, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESNEA_DICI_M_31` | IPC Bienes y servicios varios - Región Noreste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noreste, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESNOA_DICI_M_31` | IPC Bienes y servicios varios - Región Noroeste | mensual | 2016-12-01 | 2026-10-01 | region: Región Noroeste, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESUYO_DICI_M_32` | IPC Bienes y servicios varios - Región Cuyo | mensual | 2016-12-01 | 2026-10-01 | region: Región Cuyo, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
| `146.3_IBIENESNIA_DICI_M_37` | IPC Bienes y servicios varios - Región Patagonia | mensual | 2016-12-01 | 2026-10-01 | region: Región Patagonia, category: Bienes y servicios varios, measure: Índice, base: Diciembre 2016=100 |
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
de períodos más viejos no se detectan en una corrida incremental. Con
`full_refresh: true` el tap ignora el estado y recarga desde `start_date` o
desde la primera fecha de cada serie.

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
