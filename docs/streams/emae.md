# Stream `emae`

Estimador Mensual de Actividad Económica. El stream emite 22 series mensuales:
seis conceptos de nivel general y la apertura por 16 sectores.

## Granularidad y clave

Una fila por serie y período. La clave primaria es `series_id` + `date` y la
replicación es incremental por `date`.

`date` es el primer día del mes. El EMAE de agosto de 2026 se emite como
`2026-08-01`.

Las aperturas van en `sector`, `measure` y `base`:

| Columna | Valores |
|---|---|
| `sector` | `Nivel general` o uno de los 16 sectores |
| `measure` | `Serie original`, `Desestacionalizado`, `Tendencia-ciclo`, `Variación interanual`, `Variación mensual desestacionalizada`, `Variación mensual tendencia-ciclo`, `Índice` |
| `base` | `2004=100` en las series de índice; nulo en las de variación |

Los 16 sectores usan `measure = "Índice"`. Las seis series de nivel general se
distinguen por `measure`.

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
| `sector` | string \| null | Nivel general o sector de actividad |
| `measure` | string \| null | Concepto o tipo de variación |
| `base` | string \| null | Base del índice |

## Series

<!-- series-table:start -->
| ID | Serie | Frecuencia | Desde | Hasta | Dimensiones |
|---|---|---|---|---|---|
| `143.3_NO_PR_2004_A_21` | EMAE Nivel General - serie original | mensual | 2004-01-01 | 2026-08-01 | sector: Nivel general, measure: Serie original, base: 2004=100 |
| `143.3_NO_PR_2004_A_31` | EMAE Nivel General - desestacionalizado | mensual | 2004-01-01 | 2026-08-01 | sector: Nivel general, measure: Desestacionalizado, base: 2004=100 |
| `143.3_NO_PR_2004_A_28` | EMAE Nivel General - tendencia-ciclo | mensual | 2004-01-01 | 2026-08-01 | sector: Nivel general, measure: Tendencia-ciclo, base: 2004=100 |
| `143.3_ICE_SERVIA_2004_A_25` | EMAE Nivel General - variación interanual | mensual | 2005-01-01 | 2026-08-01 | sector: Nivel general, measure: Variación interanual |
| `143.3_ICE_SER_VM_2004_A_34` | EMAE Nivel General - variación mensual desestacionalizada | mensual | 2004-12-01 | 2026-08-01 | sector: Nivel general, measure: Variación mensual desestacionalizada |
| `143.3_ICE_SER_VM_2004_A_31` | EMAE Nivel General - variación mensual tendencia-ciclo | mensual | 2004-12-01 | 2026-08-01 | sector: Nivel general, measure: Variación mensual tendencia-ciclo |
| `11.3_ISOM_2004_M_39` | EMAE Agricultura, ganadería, caza y silvicultura | mensual | 2004-01-01 | 2026-08-01 | sector: Agricultura, ganadería, caza y silvicultura, measure: Índice, base: 2004=100 |
| `11.3_VIPAA_2004_M_5` | EMAE Pesca | mensual | 2004-01-01 | 2026-08-01 | sector: Pesca, measure: Índice, base: 2004=100 |
| `11.3_ISD_2004_M_26` | EMAE Explotación de minas y canteras | mensual | 2004-01-01 | 2026-08-01 | sector: Explotación de minas y canteras, measure: Índice, base: 2004=100 |
| `11.3_VMASD_2004_M_23` | EMAE Industria manufacturera | mensual | 2004-01-01 | 2026-08-01 | sector: Industria manufacturera, measure: Índice, base: 2004=100 |
| `11.3_ITC_2004_M_21` | EMAE Electricidad, gas y agua | mensual | 2004-01-01 | 2026-08-01 | sector: Electricidad, gas y agua, measure: Índice, base: 2004=100 |
| `11.3_VMATC_2004_M_12` | EMAE Construcción | mensual | 2004-01-01 | 2026-08-01 | sector: Construcción, measure: Índice, base: 2004=100 |
| `11.3_AGCS_2004_M_41` | EMAE Comercio mayorista y minorista y reparaciones | mensual | 2004-01-01 | 2026-08-01 | sector: Comercio mayorista y minorista y reparaciones, measure: Índice, base: 2004=100 |
| `11.3_P_2004_M_20` | EMAE Hoteles y restaurantes | mensual | 2004-01-01 | 2026-08-01 | sector: Hoteles y restaurantes, measure: Índice, base: 2004=100 |
| `11.3_EMC_2004_M_25` | EMAE Transporte, almacenamiento y comunicaciones | mensual | 2004-01-01 | 2026-08-01 | sector: Transporte, almacenamiento y comunicaciones, measure: Índice, base: 2004=100 |
| `11.3_IM_2004_M_25` | EMAE Intermediación financiera | mensual | 2004-01-01 | 2026-08-01 | sector: Intermediación financiera, measure: Índice, base: 2004=100 |
| `11.3_SEGA_2004_M_48` | EMAE Actividades inmobiliarias, empresariales y alquiler | mensual | 2004-01-01 | 2026-08-01 | sector: Actividades inmobiliarias, empresariales y alquiler, measure: Índice, base: 2004=100 |
| `11.3_C_2004_M_60` | EMAE Administración pública, defensa y seguridad social | mensual | 2004-01-01 | 2026-08-01 | sector: Administración pública, defensa y seguridad social, measure: Índice, base: 2004=100 |
| `11.3_CMMR_2004_M_10` | EMAE Enseñanza | mensual | 2004-01-01 | 2026-08-01 | sector: Enseñanza, measure: Índice, base: 2004=100 |
| `11.3_HR_2004_M_24` | EMAE Servicios sociales y salud | mensual | 2004-01-01 | 2026-08-01 | sector: Servicios sociales y salud, measure: Índice, base: 2004=100 |
| `11.3_TAC_2004_M_60` | EMAE Otras actividades de servicios comunitarios, sociales y personales | mensual | 2004-01-01 | 2026-08-01 | sector: Otras actividades de servicios comunitarios, sociales y personales, measure: Índice, base: 2004=100 |
| `11.3_IF_2004_M_25` | EMAE Impuestos netos de subsidios | mensual | 2004-01-01 | 2026-08-01 | sector: Impuestos netos de subsidios, measure: Índice, base: 2004=100 |
<!-- series-table:end -->

## Unidades

Las series de índice usan base 2004=100. Las de variación vienen como fracción
entre -1 y 1: `-0.0174` es -1,74 %. El campo `unit` distingue cada caso.

El sufijo `_A_` de los IDs de nivel general no indica frecuencia anual. Esas
series son mensuales. La frecuencia válida está en el campo `frequency`.

## Nulos y demoras

El EMAE se publica con unos dos meses de demora. Si el último período todavía
no está en la API, el stream termina en el mes anterior. El tap no emite filas
vacías.

La serie tiene base 2004=100. Si INDEC publica otra base, la columna `base`
distingue las series. Los valores de bases distintas no son comparables.

## Ejemplo

```json
{
  "series_id": "11.3_VMATC_2004_M_12",
  "date": "2026-08-01",
  "value": 133.3939896401508,
  "series_name": "EMAE Construcción",
  "unit": "Índice 2004=100",
  "frequency": "monthly",
  "dataset": "Estimador Mensual de Actividad Económica (EMAE). Apertura Sectorial. Base 2004",
  "source": "INDEC",
  "sector": "Construcción",
  "measure": "Índice",
  "base": "2004=100"
}
```
