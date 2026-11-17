# Stream `mercado_trabajo`

Tasas del mercado de trabajo de la Encuesta Permanente de Hogares (EPH). El
stream emite 123 series trimestrales: actividad, empleo, desempleo y
subocupación para el total de 31 aglomerados urbanos, 33 aglomerados y cinco
regiones, en las combinaciones que la API devuelve con datos.

## Granularidad y clave

Una fila por serie y período. La clave primaria es `series_id` + `date` y la
replicación es incremental por `date`.

La EPH es trimestral. `date` es el primer día del trimestre: el primer
trimestre de 2026 se emite como `2026-01-01`.

Las aperturas van en `aglomerado`, `measure` y `geography_type`:

| Columna | Valores |
|---|---|
| `aglomerado` | `Total 31 aglomerados urbanos`, aglomerados y regiones |
| `measure` | `Actividad`, `Empleo`, `Desempleo`, `Subocupación` |
| `geography_type` | `Total`, `Aglomerado` o `Región` |

El total es urbano: cubre 31 aglomerados, no el país completo. No lo uses como
total nacional.

## Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `series_id` | string | ID de la serie en la API |
| `date` | date | Primer día del trimestre |
| `value` | number \| null | Tasa publicada |
| `series_name` | string | Nombre legible de la serie |
| `unit` | string \| null | Unidad de la tasa |
| `frequency` | string | `quarterly` |
| `dataset` | string \| null | Dataset de origen |
| `source` | string | `INDEC` |
| `aglomerado` | string \| null | Total urbano o aglomerado |
| `measure` | string \| null | Actividad, empleo, desempleo o subocupación |
| `geography_type` | string \| null | Total, aglomerado o región |

## Unidad

Las tasas se emiten como proporciones entre 0 y 1, igual que en el CSV de
origen. Una desocupación de 7,9 % llega como `0.079`. El campo `unit` dice
`Proporción (0-1)`. Si necesitás porcentaje, multiplicá por 100 en el modelo de
dbt o en el destino.

## Series

<!-- series-table:start -->
| ID | Serie | Frecuencia | Desde | Hasta | Dimensiones |
|---|---|---|---|---|---|
| `43.2_ECTAT_0_T_33` | EPH Tasa de actividad - Total 31 aglomerados urbanos | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Total 31 aglomerados urbanos, measure: Actividad, geography_type: Total |
| `44.2_ECTET_0_T_30` | EPH Tasa de empleo - Total 31 aglomerados urbanos | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Total 31 aglomerados urbanos, measure: Empleo, geography_type: Total |
| `45.2_ECTDT_0_T_33` | EPH Tasa de desempleo - Total 31 aglomerados urbanos | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Total 31 aglomerados urbanos, measure: Desempleo, geography_type: Total |
| `46.2_ECTST_0_T_36` | EPH Tasa de subocupación - Total 31 aglomerados urbanos | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Total 31 aglomerados urbanos, measure: Subocupación, geography_type: Total |
| `43.2_ECTATBB_0_T_46` | EPH Tasa de actividad - Bahía Blanca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Bahía Blanca, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETBB_0_T_43` | EPH Tasa de empleo - Bahía Blanca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Bahía Blanca, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTBB_0_T_46` | EPH Tasa de desempleo - Bahía Blanca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Bahía Blanca, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTBB_0_T_49` | EPH Tasa de subocupación - Bahía Blanca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Bahía Blanca, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATC_0_T_38` | EPH Tasa de actividad - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETC_0_T_35` | EPH Tasa de empleo - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTC_0_T_38` | EPH Tasa de desempleo - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTC_0_T_41` | EPH Tasa de subocupación - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATCR_0_T_52` | EPH Tasa de actividad - Comodoro Rivadavia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Comodoro Rivadavia, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETCR_0_T_49` | EPH Tasa de empleo - Comodoro Rivadavia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Comodoro Rivadavia, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTCR_0_T_52` | EPH Tasa de desempleo - Comodoro Rivadavia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Comodoro Rivadavia, measure: Desempleo, geography_type: Aglomerado |
| `43.2_ECTATC_0_T_43` | EPH Tasa de actividad - Concordia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Concordia, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETC_0_T_40` | EPH Tasa de empleo - Concordia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Concordia, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTC_0_T_43` | EPH Tasa de desempleo - Concordia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Concordia, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTC_0_T_46` | EPH Tasa de subocupación - Concordia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Concordia, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATC_0_T_44` | EPH Tasa de actividad - Corrientes | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Corrientes, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTC_0_T_44` | EPH Tasa de desempleo - Corrientes | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Corrientes, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTC_0_T_47` | EPH Tasa de subocupación - Corrientes | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Corrientes, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATF_0_T_41` | EPH Tasa de actividad - Formosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Formosa, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETF_0_T_38` | EPH Tasa de empleo - Formosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Formosa, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTF_0_T_41` | EPH Tasa de desempleo - Formosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Formosa, measure: Desempleo, geography_type: Aglomerado |
| `44.2_ECTETG_0_T_34` | EPH Tasa de empleo - GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: GBA, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTG_0_T_40` | EPH Tasa de subocupación - GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: GBA, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGC_0_T_48` | EPH Tasa de actividad - Gran Catamarca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Catamarca, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTGC_0_T_48` | EPH Tasa de desempleo - Gran Catamarca | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Catamarca, measure: Desempleo, geography_type: Aglomerado |
| `43.2_ECTATGC_0_T_46` | EPH Tasa de actividad - Gran Córdoba | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Córdoba, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGC_0_T_43` | EPH Tasa de empleo - Gran Córdoba | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Córdoba, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTGC_0_T_49` | EPH Tasa de subocupación - Gran Córdoba | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Córdoba, measure: Subocupación, geography_type: Aglomerado |
| `44.2_ECTETGLP_0_T_44` | EPH Tasa de empleo - Gran La Plata | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran La Plata, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTGLP_0_T_50` | EPH Tasa de subocupación - Gran La Plata | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran La Plata, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGM_0_T_46` | EPH Tasa de actividad - Gran Mendoza | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Mendoza, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGM_0_T_43` | EPH Tasa de empleo - Gran Mendoza | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Mendoza, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTGM_0_T_46` | EPH Tasa de desempleo - Gran Mendoza | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Mendoza, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGM_0_T_49` | EPH Tasa de subocupación - Gran Mendoza | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Mendoza, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGP_0_T_45` | EPH Tasa de actividad - Gran Paraná | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Paraná, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGP_0_T_42` | EPH Tasa de empleo - Gran Paraná | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Paraná, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTGP_0_T_45` | EPH Tasa de desempleo - Gran Paraná | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Paraná, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGP_0_T_48` | EPH Tasa de subocupación - Gran Paraná | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Paraná, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGR_0_T_50` | EPH Tasa de actividad - Gran Resistencia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Resistencia, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGR_0_T_47` | EPH Tasa de empleo - Gran Resistencia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Resistencia, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTGR_0_T_50` | EPH Tasa de desempleo - Gran Resistencia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Resistencia, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGR_0_T_53` | EPH Tasa de subocupación - Gran Resistencia | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Resistencia, measure: Subocupación, geography_type: Aglomerado |
| `44.2_ECTETGR_0_T_43` | EPH Tasa de empleo - Gran Rosario | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Rosario, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTGR_0_T_49` | EPH Tasa de subocupación - Gran Rosario | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Rosario, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGSJ_0_T_47` | EPH Tasa de actividad - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGSJ_0_T_44` | EPH Tasa de empleo - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTGSJ_0_T_47` | EPH Tasa de desempleo - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGSJ_0_T_50` | EPH Tasa de subocupación - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGSF_0_T_47` | EPH Tasa de actividad - Gran Santa Fe | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Santa Fe, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTGSF_0_T_47` | EPH Tasa de desempleo - Gran Santa Fe | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Santa Fe, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGSF_0_T_50` | EPH Tasa de subocupación - Gran Santa Fe | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran Santa Fe, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATGT_0_T_46` | EPH Tasa de actividad - Gran Tucumán | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Tucumán, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTGT_0_T_46` | EPH Tasa de desempleo - Gran Tucumán | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Tucumán, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGT_0_T_49` | EPH Tasa de subocupación - Gran Tucumán | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Gran Tucumán, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATJ_0_T_39` | EPH Tasa de actividad - Jujuy | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Jujuy, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETJ_0_T_36` | EPH Tasa de empleo - Jujuy | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Jujuy, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTJ_0_T_39` | EPH Tasa de desempleo - Jujuy | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Jujuy, measure: Desempleo, geography_type: Aglomerado |
| `43.2_ECTATLR_0_T_42` | EPH Tasa de actividad - La Rioja | trimestral | 2003-07-01 | 2024-04-01 | aglomerado: La Rioja, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETLR_0_T_39` | EPH Tasa de empleo - La Rioja | trimestral | 2024-07-01 | 2026-04-01 | aglomerado: La Rioja, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTLR_0_T_42` | EPH Tasa de desempleo - La Rioja | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: La Rioja, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTLR_0_T_45` | EPH Tasa de subocupación - La Rioja | trimestral | 2024-07-01 | 2026-04-01 | aglomerado: La Rioja, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATMDP_0_T_47` | EPH Tasa de actividad - Mar del Plata | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Mar del Plata, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETMDP_0_T_44` | EPH Tasa de empleo - Mar del Plata | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Mar del Plata, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTMDP_0_T_50` | EPH Tasa de subocupación - Mar del Plata | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Mar del Plata, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATN_0_T_41` | EPH Tasa de actividad - Neuquén | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Neuquén, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETN_0_T_38` | EPH Tasa de empleo - Neuquén | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Neuquén, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTN_0_T_41` | EPH Tasa de desempleo - Neuquén | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Neuquén, measure: Desempleo, geography_type: Aglomerado |
| `43.2_ECTATPG_0_T_46` | EPH Tasa de actividad - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETPG_0_T_43` | EPH Tasa de empleo - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTPG_0_T_46` | EPH Tasa de desempleo - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTPG_0_T_49` | EPH Tasa de subocupación - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATP_0_T_41` | EPH Tasa de actividad - Posadas | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Posadas, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTP_0_T_41` | EPH Tasa de desempleo - Posadas | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Posadas, measure: Desempleo, geography_type: Aglomerado |
| `43.2_ECTATRT_0_T_47` | EPH Tasa de actividad - Rawson-Trelew | trimestral | 2006-10-01 | 2026-04-01 | aglomerado: Rawson-Trelew, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETCU_0_T_35` | EPH Tasa de empleo - Región Cuyo | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Cuyo, measure: Empleo, geography_type: Región |
| `45.2_ECTDTCU_0_T_38` | EPH Tasa de desempleo - Región Cuyo | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Cuyo, measure: Desempleo, geography_type: Región |
| `46.2_ECTSTCU_0_T_41` | EPH Tasa de subocupación - Región Cuyo | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Cuyo, measure: Subocupación, geography_type: Región |
| `43.2_ECTATNE_0_T_42` | EPH Tasa de actividad - Región Noreste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noreste, measure: Actividad, geography_type: Región |
| `44.2_ECTETNO_0_T_39` | EPH Tasa de empleo - Región Noreste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noreste, measure: Empleo, geography_type: Región |
| `45.2_ECTDTNE_0_T_42` | EPH Tasa de desempleo - Región Noreste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noreste, measure: Desempleo, geography_type: Región |
| `46.2_ECTSTNE_0_T_45` | EPH Tasa de subocupación - Región Noreste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noreste, measure: Subocupación, geography_type: Región |
| `44.2_ECTETNE_0_T_39` | EPH Tasa de empleo - Región Noroeste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noroeste, measure: Empleo, geography_type: Región |
| `46.2_ECTSTNO_0_T_45` | EPH Tasa de subocupación - Región Noroeste | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Noroeste, measure: Subocupación, geography_type: Región |
| `44.2_ECTETRP_0_T_46` | EPH Tasa de empleo - Región Pampeana | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Pampeana, measure: Empleo, geography_type: Región |
| `46.2_ECTSTRP_0_T_52` | EPH Tasa de subocupación - Región Pampeana | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Pampeana, measure: Subocupación, geography_type: Región |
| `43.2_ECTATP_0_T_43` | EPH Tasa de actividad - Región Patagonia | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Patagonia, measure: Actividad, geography_type: Región |
| `44.2_ECTETP_0_T_40` | EPH Tasa de empleo - Región Patagonia | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Patagonia, measure: Empleo, geography_type: Región |
| `45.2_ECTDTP_0_T_43` | EPH Tasa de desempleo - Región Patagonia | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Patagonia, measure: Desempleo, geography_type: Región |
| `46.2_ECTSTP_0_T_46` | EPH Tasa de subocupación - Región Patagonia | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Región Patagonia, measure: Subocupación, geography_type: Región |
| `43.2_ECTATRC_0_T_44` | EPH Tasa de actividad - Río Cuarto | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Cuarto, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETRC_0_T_41` | EPH Tasa de empleo - Río Cuarto | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Cuarto, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTRC_0_T_44` | EPH Tasa de desempleo - Río Cuarto | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Cuarto, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTRC_0_T_47` | EPH Tasa de subocupación - Río Cuarto | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Cuarto, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATRG_0_T_46` | EPH Tasa de actividad - Río Gallegos | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Gallegos, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETRG_0_T_43` | EPH Tasa de empleo - Río Gallegos | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Gallegos, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTRG_0_T_46` | EPH Tasa de desempleo - Río Gallegos | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Río Gallegos, measure: Desempleo, geography_type: Aglomerado |
| `44.2_ECTETS_0_T_36` | EPH Tasa de empleo - Salta | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Salta, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTS_0_T_42` | EPH Tasa de subocupación - Salta | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Salta, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATSL_0_T_42` | EPH Tasa de actividad - San Luis | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: San Luis, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETSL_0_T_39` | EPH Tasa de empleo - San Luis | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: San Luis, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTSL_0_T_42` | EPH Tasa de desempleo - San Luis | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: San Luis, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTSL_0_T_45` | EPH Tasa de subocupación - San Luis | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: San Luis, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATSN_0_T_45` | EPH Tasa de actividad - San Nicolás | trimestral | 2006-10-01 | 2026-04-01 | aglomerado: San Nicolás, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETSN_0_T_42` | EPH Tasa de empleo - San Nicolás | trimestral | 2006-10-01 | 2026-04-01 | aglomerado: San Nicolás, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTSN_0_T_45` | EPH Tasa de desempleo - San Nicolás | trimestral | 2006-10-01 | 2026-04-01 | aglomerado: San Nicolás, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTSN_0_T_48` | EPH Tasa de subocupación - San Nicolás | trimestral | 2006-10-01 | 2026-04-01 | aglomerado: San Nicolás, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATSR_0_T_44` | EPH Tasa de actividad - Santa Rosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santa Rosa, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETSR_0_T_41` | EPH Tasa de empleo - Santa Rosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santa Rosa, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTSR_0_T_44` | EPH Tasa de desempleo - Santa Rosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santa Rosa, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTSR_0_T_47` | EPH Tasa de subocupación - Santa Rosa | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santa Rosa, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATSDE_0_T_53` | EPH Tasa de actividad - Santiago del Estero | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santiago del Estero, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETSDE_0_T_50` | EPH Tasa de empleo - Santiago del Estero | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santiago del Estero, measure: Empleo, geography_type: Aglomerado |
| `46.2_ECTSTSDE_0_T_56` | EPH Tasa de subocupación - Santiago del Estero | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Santiago del Estero, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATURG_0_T_52` | EPH Tasa de actividad - Ushuaia-Río Grande | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Ushuaia-Río Grande, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETURG_0_T_49` | EPH Tasa de empleo - Ushuaia-Río Grande | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Ushuaia-Río Grande, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTURG_0_T_52` | EPH Tasa de desempleo - Ushuaia-Río Grande | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Ushuaia-Río Grande, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTURG_0_T_55` | EPH Tasa de subocupación - Ushuaia-Río Grande | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Ushuaia-Río Grande, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATVCP_0_T_57` | EPH Tasa de actividad - Viedma-Carmen de Patagones | trimestral | 2006-10-01 | 2022-01-01 | aglomerado: Viedma-Carmen de Patagones, measure: Actividad, geography_type: Aglomerado |
| `45.2_ECTDTVCP_0_T_57` | EPH Tasa de desempleo - Viedma-Carmen de Patagones | trimestral | 2022-04-01 | 2026-04-01 | aglomerado: Viedma-Carmen de Patagones, measure: Desempleo, geography_type: Aglomerado |
<!-- series-table:end -->

## Cobertura

La EPH continua tiene 39 geografías: el total de 31 aglomerados urbanos, 33
aglomerados y cinco regiones. Cada geografía tiene cuatro tasas, así que hay 156
combinaciones posibles. La API devuelve datos para 123; las otras 33 están
registradas y responden `available=true`, pero `/series/` devuelve cero filas.
El catálogo incluye solo las 123 con datos. La lista completa de IDs y
disponibilidad por tasa está en el `catalog.json` empaquetado y en la tabla de
series de esta página.

## Nulos y demoras

La EPH se publica por trimestre. Si el trimestre todavía no está en la API, el
stream termina en el anterior.

Hay nulos estructurales. El total no tiene dato en 2015-10 ni en 2016-01. El
tap no emite esas filas y no interpola.

La serie continua arranca en 2003. El tap no ajusta empalmes metodológicos ni
cambios de ponderación. Cualquier comparación entre períodos lejanos queda a
cargo de quien modela los datos.

## Ejemplo

```json
{
  "series_id": "45.2_ECTDT_0_T_33",
  "date": "2026-04-01",
  "value": 0.079,
  "series_name": "EPH Tasa de desempleo - Total 31 aglomerados urbanos",
  "unit": "Proporción (0-1)",
  "frequency": "quarterly",
  "dataset": "Principales variables ocupacionales. EPH continua. Desempleo",
  "source": "INDEC",
  "aglomerado": "Total 31 aglomerados urbanos",
  "measure": "Desempleo",
  "geography_type": "Total"
}
```
