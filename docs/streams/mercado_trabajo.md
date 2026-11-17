# Stream `mercado_trabajo`

Tasas del mercado de trabajo de la Encuesta Permanente de Hogares (EPH). El
stream emite 28 series trimestrales: actividad, empleo, desempleo y
subocupación para el total de 31 aglomerados urbanos y seis aglomerados.

## Granularidad y clave

Una fila por serie y período. La clave primaria es `series_id` + `date` y la
replicación es incremental por `date`.

La EPH es trimestral. `date` es el primer día del trimestre: el primer
trimestre de 2026 se emite como `2026-01-01`.

Las aperturas van en `aglomerado`, `measure` y `geography_type`:

| Columna | Valores |
|---|---|
| `aglomerado` | `Total 31 aglomerados urbanos`, `CABA`, `Partidos de GBA`, `Gran Mendoza`, `Gran Paraná`, `Gran Resistencia`, `Gran San Juan` |
| `measure` | `Actividad`, `Empleo`, `Desempleo`, `Subocupación` |
| `geography_type` | `Total` o `Aglomerado` |

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
| `geography_type` | string \| null | Total o aglomerado |

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
| `43.2_ECTATC_0_T_38` | EPH Tasa de actividad - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETC_0_T_35` | EPH Tasa de empleo - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTC_0_T_38` | EPH Tasa de desempleo - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTC_0_T_41` | EPH Tasa de subocupación - CABA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: CABA, measure: Subocupación, geography_type: Aglomerado |
| `43.2_ECTATPG_0_T_46` | EPH Tasa de actividad - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETPG_0_T_43` | EPH Tasa de empleo - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTPG_0_T_46` | EPH Tasa de desempleo - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTPG_0_T_49` | EPH Tasa de subocupación - Partidos de GBA | trimestral | 2003-01-01 | 2026-04-01 | aglomerado: Partidos de GBA, measure: Subocupación, geography_type: Aglomerado |
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
| `43.2_ECTATGSJ_0_T_47` | EPH Tasa de actividad - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Actividad, geography_type: Aglomerado |
| `44.2_ECTETGSJ_0_T_44` | EPH Tasa de empleo - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Empleo, geography_type: Aglomerado |
| `45.2_ECTDTGSJ_0_T_47` | EPH Tasa de desempleo - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Desempleo, geography_type: Aglomerado |
| `46.2_ECTSTGSJ_0_T_50` | EPH Tasa de subocupación - Gran San Juan | trimestral | 2003-07-01 | 2026-04-01 | aglomerado: Gran San Juan, measure: Subocupación, geography_type: Aglomerado |
<!-- series-table:end -->

## Cobertura

La API tiene 39 geografías para la EPH continua. 22 tienen al menos una tasa
vacía en `/series/`, aunque estén registradas. La 0.1.0 incluye el total y seis
aglomerados con las cuatro tasas completas. Las demás geografías quedan para
una versión siguiente.

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
