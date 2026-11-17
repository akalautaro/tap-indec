# Catálogo de series INDEC para un tap de Meltano

Generado: 2026-11-17T03:13:02+00:00  
Fuente: API de series de datos.gob.ar (https://apis.datos.gob.ar/series/api/)  
Verificación: cada serie listada en `catalog.json` fue consultada con un request real a `/series/` (metadata=full, limit=1000) y devolvió al menos una observación.

## Resumen

| Stream | Series incluidas | Frecuencia | Cobertura temporal | Dataset(s) |
|---|---:|---|---|---|
| `ipc` | 26 | mensual | 2016-12 → 2026-10 | 145 (IPC Nacional, base dic-2016) |
| `emae` | 22 | mensual | 2004-01 → 2026-08 | 143 (nivel general) y 11 (apertura sectorial), base 2004 |
| `mercado_trabajo` | 28 | trimestral | 2003-01 → 2026-04 | 43, 44, 45, 46 (EPH continua) |

La base vigente del IPC en la API es **diciembre 2016**. No existe una serie con base posterior (2024/2025) en datos.gob.ar al 2026-11-17. Las bases 2003, abril-2008, 2013-2014, 1988 y 1974 están marcadas `SERIE DISCONTINUADA` y no son comparables con la actual.

## Comportamiento de la API (relevante para el tap)

- **Máximo 40 ids por request.** Con 41 ids devuelve HTTP 400. Conviene lotes de ≤40.
- **Mezclar frecuencias colapsa todo a la frecuencia más baja.** Un request con una serie mensual y una anual devuelve solo los valores de enero de la mensual. Hay que agrupar por frecuencia (mensual / trimestral) o pedir de a una serie.
- **Los porcentajes vienen como fracción 0-1.** `0.079` = 7.9%, aunque `units` diga `Porcentaje` o `Variación`. Multiplicar por 100 si se quiere publicar en porcentaje.
- **Formato ancho.** La respuesta trae `[fecha, valor_id1, valor_id2, ...]`; el orden de columnas es `params.identifiers`. Al mezclar series con distintos inicios aparecen `null` antes del primer dato de cada una.
- **Búsqueda:** `/search/?q=...&limit=1000&start=N`; el máximo de `limit` es 1000 y la paginación es por `start`.
- **Sin rate limit explícito observado.** Solo headers de Cloudflare; usar lotes y pausas.
- **El dump de metadatos está atrasado.** `series-tiempo-metadatos.csv` marca fines de 2026-07/2026-04 y `dataset.temporal` viejo; las fechas reales se obtienen del endpoint `/series/`. Ejemplo: IPC llega a 2026-10, no a 2026-07.

## Stream `ipc`

Descripción: IPC Nacional base diciembre 2016. Se incluyen nivel general nacional, nivel general por las seis regiones, las 12 divisiones de la canasta, bienes/servicios y las categorías núcleo/regulados/estacionales. Todo mensual, en índices (base dic-2016=100) salvo las dos series de variación.

Dataset: `145` — *Índice de Precios al Consumidor Nacional (IPC). Base diciembre 2016.*  
Fuente: INDEC / Subsecretaría de Programación Macroeconómica.

| ID | Nombre | Región | Categoría | Medida | Unidades | Inicio | Fin | Dataset |
|---|---|---|---|---|---|---|---|---|
| `145.3_INGNACNAL_DICI_M_15` | IPC Nivel General Nacional | Nacional | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGNACUAL_DICI_M_38` | IPC Nivel General Nacional - variación mensual | Nacional | Nivel general | variacion_mensual | Variación intermensual (0-1) | 2017-01 | 2026-10 | 145 |
| `145.3_INGNACIOR_DICI_M_57` | IPC Nivel General Nacional - variación acumulada anual | Nacional | Nivel general | variacion_acumulada_anio | Variación Porcentual (0-1) | 2017-01 | 2026-10 | 145 |
| `145.3_INGGBAGBA_DICI_M_10` | IPC Nivel General GBA | GBA | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGPAMANA_DICI_M_15` | IPC Nivel General Región Pampeana | Región Pampeana | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGNEANEA_DICI_M_10` | IPC Nivel General Región Noreste | Región Noreste | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGNOANOA_DICI_M_10` | IPC Nivel General Región Noroeste | Región Noroeste | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGCUYUYO_DICI_M_11` | IPC Nivel General Región Cuyo | Región Cuyo | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `145.3_INGPATNIA_DICI_M_16` | IPC Nivel General Región Patagonia | Región Patagonia | Nivel general | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IALIMENNAL_DICI_M_45` | IPC Alimentos y bebidas no alcohólicas - Nacional | Nacional | Alimentos y bebidas no alcohólicas | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IBEBIDANAL_DICI_M_39` | IPC Bebidas alcohólicas y tabaco - Nacional | Nacional | Bebidas alcohólicas y tabaco | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IPRENDANAL_DICI_M_35` | IPC Prendas de vestir y calzado - Nacional | Nacional | Prendas de vestir y calzado | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IVIVIENNAL_DICI_M_52` | IPC Vivienda, agua, electricidad, gas y otros combustibles - Nacional | Nacional | Vivienda, agua, electricidad, gas y otros combustibles | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IEQUIPANAL_DICI_M_46` | IPC Equipamiento y mantenimiento del hogar - Nacional | Nacional | Equipamiento y mantenimiento del hogar | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_ISALUDNAL_DICI_M_18` | IPC Salud - Nacional | Nacional | Salud | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_ITRANSPNAL_DICI_M_23` | IPC Transporte - Nacional | Nacional | Transporte | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_ICOMUNINAL_DICI_M_27` | IPC Comunicaciones - Nacional | Nacional | Comunicaciones | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IRECREANAL_DICI_M_31` | IPC Recreación y cultura - Nacional | Nacional | Recreación y cultura | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IEDUCACNAL_DICI_M_22` | IPC Educación - Nacional | Nacional | Educación | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IRESTAUNAL_DICI_M_33` | IPC Restaurantes y hoteles - Nacional | Nacional | Restaurantes y hoteles | indice | Índice | 2016-12 | 2026-10 | 145 |
| `146.3_IBIENESNAL_DICI_M_36` | IPC Bienes y servicios varios - Nacional | Nacional | Bienes y servicios varios | indice | Índice | 2016-12 | 2026-10 | 145 |
| `147.3_IBIENESNAL_DICI_T_19` | IPC Bienes - Nacional | Nacional | Bienes | indice | Índice | 2016-12 | 2026-10 | 145 |
| `147.3_ISERVICNAL_DICI_T_22` | IPC Servicios - Nacional | Nacional | Servicios | indice | Índice | 2016-12 | 2026-10 | 145 |
| `148.3_INUCLEONAL_DICI_M_19` | IPC Núcleo - Nacional | Nacional | Núcleo | indice | Índice | 2016-12 | 2026-10 | 145 |
| `148.3_IREGULANAL_DICI_M_22` | IPC Regulados - Nacional | Nacional | Regulados | indice | Índice | 2016-12 | 2026-10 | 145 |
| `148.3_IESTACINAL_DICI_M_25` | IPC Estacionales - Nacional | Nacional | Estacionales | indice | Índice | 2016-12 | 2026-10 | 145 |

Según el dump de metadatos (2026-08), el dataset 145 tiene 570 series (437 mensuales, 133 trimestrales). Las 437 mensuales se reparten en: 21 de nivel general (7 regiones × índice/variación mensual/variación acumulada), 84 de capítulos (12 divisiones × 7 regiones), 14 de bienes/servicios (2 × 7), 28 de categorías (4 × 7), 144 de incidencia por capítulo, 14 de incidencia bienes/servicios, 48 de incidencia por categoría y 84 de precios de productos individuales. El catálogo toma solo las 26 series de índice/variación; las de incidencia y precios de productos no son índices y no deben mezclarse.

Huecos y trampas del IPC:

- **Duplicados exactos:** las series `148.3_INIVEL*` (nivel general por región, distribución 145.9) son idénticas a las `145.3_ING*` (distribución 145.3). Verificado con maxdiff = 0 en 119 observaciones. Usar una sola familia; el catálogo usa `145.3_ING*`.
- **Corte de base:** la serie base 2008 termina 2013-12, la IPC-NU termina 2015-10 y la base 2016 empieza 2016-12. Hay un hueco 2015-11 → 2016-11 sin serie comparable. No encadenar sin empalme.
- **Aperturas cruzadas:** existen las 84 series de categoría por región (`146.3_I<CATEGORIA><REGION>_DICI_M_*`), pero no se incluyen para no inflar el stream. Están disponibles si se necesita granularidad regional por división.
- **Dataset 101 (IPC-GBA):** según el dump, 236 series con aperturas GBA más detalladas (38 principales aperturas mensuales, alimentos y bebidas, etc.). Es alternativo; no sumar con las nacionales porque los valores no coinciden (son índices distintos, no duplicados).
- **Dataset 173:** según el dump, 3 series de tasas de variación mensual por categoría (núcleo, regulados, estacionales), 2017-01 → 2026-10 (fecha verificada en la API). Se pueden derivar de los índices; no se incluyen para evitar duplicar.
- **Sufijo `_T_` en IDs mensuales:** `147.3_IBIENESNAL_DICI_T_19` y `147.3_ISERVICNAL_DICI_T_22` son mensuales pese al `_T_`. La frecuencia válida es `frequency_iso`.

## Stream `emae`

Descripción: EMAE base 2004. Nivel general (serie original, desestacionalizada, tendencia-ciclo, variación interanual y variaciones mensuales) y apertura por 16 sectores. Todo mensual.

Datasets: `143` — *EMAE. Base 2004* (nivel general); `11` — *EMAE. Apertura Sectorial. Base 2004* (sectores).  
Fuente: INDEC / Subsecretaría de Programación Macroeconómica.

| ID | Nombre | Sector | Medida | Unidades | Inicio | Fin | Dataset |
|---|---|---|---|---|---|---|---|
| `143.3_NO_PR_2004_A_21` | EMAE Nivel General - serie original | Nivel general | indice_original | Índice 2004=100 | 2004-01 | 2026-08 | 143 |
| `143.3_NO_PR_2004_A_31` | EMAE Nivel General - desestacionalizado | Nivel general | indice_desestacionalizado | Índice 2004=100 | 2004-01 | 2026-08 | 143 |
| `143.3_NO_PR_2004_A_28` | EMAE Nivel General - tendencia-ciclo | Nivel general | tendencia_ciclo | Índice 2004=100 | 2004-01 | 2026-08 | 143 |
| `143.3_ICE_SERVIA_2004_A_25` | EMAE Nivel General - variación interanual | Nivel general | variacion_interanual | Variación interanual (0-1) | 2005-01 | 2026-08 | 143 |
| `143.3_ICE_SER_VM_2004_A_34` | EMAE Nivel General - variación mensual desestacionalizada | Nivel general | variacion_mensual_desestacionalizada | Variación mensual (0-1) | 2004-12 | 2026-08 | 143 |
| `143.3_ICE_SER_VM_2004_A_31` | EMAE Nivel General - variación mensual tendencia-ciclo | Nivel general | variacion_mensual_tendencia_ciclo | Variación mensual (0-1) | 2004-12 | 2026-08 | 143 |
| `11.3_ISOM_2004_M_39` | EMAE Agricultura, ganadería, caza y silvicultura | Agricultura, ganadería, caza y silvicultura | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_VIPAA_2004_M_5` | EMAE Pesca | Pesca | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_ISD_2004_M_26` | EMAE Explotación de minas y canteras | Explotación de minas y canteras | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_VMASD_2004_M_23` | EMAE Industria manufacturera | Industria manufacturera | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_ITC_2004_M_21` | EMAE Electricidad, gas y agua | Electricidad, gas y agua | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_VMATC_2004_M_12` | EMAE Construcción | Construcción | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_AGCS_2004_M_41` | EMAE Comercio mayorista y minorista y reparaciones | Comercio mayorista y minorista y reparaciones | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_P_2004_M_20` | EMAE Hoteles y restaurantes | Hoteles y restaurantes | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_EMC_2004_M_25` | EMAE Transporte, almacenamiento y comunicaciones | Transporte, almacenamiento y comunicaciones | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_IM_2004_M_25` | EMAE Intermediación financiera | Intermediación financiera | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_SEGA_2004_M_48` | EMAE Actividades inmobiliarias, empresariales y alquiler | Actividades inmobiliarias, empresariales y alquiler | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_C_2004_M_60` | EMAE Administración pública, defensa y seguridad social | Administración pública, defensa y seguridad social | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_CMMR_2004_M_10` | EMAE Enseñanza | Enseñanza | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_HR_2004_M_24` | EMAE Servicios sociales y salud | Servicios sociales y salud | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_TAC_2004_M_60` | EMAE Otras actividades de servicios comunitarios, sociales y personales | Otras actividades de servicios comunitarios, sociales y personales | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |
| `11.3_IF_2004_M_25` | EMAE Impuestos netos de subsidios | Impuestos netos de subsidios | indice | Índice 2004=100 | 2004-01 | 2026-08 | 11 |

Según el dump de metadatos, el dataset 11 tiene 48 series (16 sectores × anual/trimestral/mensual) y el 143 tiene 18 (6 conceptos × 3 frecuencias). El catálogo toma las 6 series mensuales de nivel general y los 16 sectores mensuales.

Huecos y trampas del EMAE:

- **Base 1993 discontinuada de hecho:** el dataset 10 (11 series) termina 2013-12 y no está marcado como discontinuado en todos los campos. No usar.
- **El sufijo del ID no es la frecuencia:** `143.3_NO_PR_2004_A_21` es mensual aunque el ID tenga `_A_`. La frecuencia está en `frequency_iso`/`indice_tiempo_frecuencia`.
- **Nombre de archivo engañoso:** el `downloadURL` de 143.3 se llama `emae-valores-anuales-indice-base-2004-mensual.csv`; el contenido es mensual.
- **Sectores con etiquetas viejas:** `11.3_IF_2004_M_25` figura como "Subsidios netos" pero es "Impuestos netos de subsidios"; `11.3_TAC_2004_M_60` figura como "Servicios comunitarios" pero es "Otras actividades de servicios comunitarios, sociales y personales". El nombre del catálogo usa la etiqueta larga.
- **Variaciones en fracción:** la variación interanual de 2026-08 es `-0.0174` = -1.74%.

## Stream `mercado_trabajo`

Descripción: EPH continua. Tasas de actividad, empleo, desempleo y subocupación para el total de 31 aglomerados urbanos y para 6 aglomerados seleccionados. Frecuencia trimestral (la fecha es el primer mes del trimestre).

Datasets: `43` (actividad), `44` (empleo), `45` (desempleo), `46` (subocupación) — *Principales variables ocupacionales. EPH continua.*  
Fuente: INDEC / Subsecretaría de Programación Macroeconómica.

| ID | Nombre | Aglomerado | Tasa | Unidades | Inicio | Fin | Dataset |
|---|---|---|---|---|---|---|---|
| `43.2_ECTAT_0_T_33` | EPH Tasa de actividad - Total 31 aglomerados urbanos | Total 31 aglomerados urbanos | Actividad | Porcentaje (0-1) | 2003-01 | 2026-04 | 43 |
| `44.2_ECTET_0_T_30` | EPH Tasa de empleo - Total 31 aglomerados urbanos | Total 31 aglomerados urbanos | Empleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 44 |
| `45.2_ECTDT_0_T_33` | EPH Tasa de desempleo - Total 31 aglomerados urbanos | Total 31 aglomerados urbanos | Desempleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 45 |
| `46.2_ECTST_0_T_36` | EPH Tasa de subocupación - Total 31 aglomerados urbanos | Total 31 aglomerados urbanos | Subocupación | Porcentaje (0-1) | 2003-01 | 2026-04 | 46 |
| `43.2_ECTATC_0_T_38` | EPH Tasa de actividad - CABA | CABA | Actividad | Porcentaje (0-1) | 2003-01 | 2026-04 | 43 |
| `44.2_ECTETC_0_T_35` | EPH Tasa de empleo - CABA | CABA | Empleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 44 |
| `45.2_ECTDTC_0_T_38` | EPH Tasa de desempleo - CABA | CABA | Desempleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 45 |
| `46.2_ECTSTC_0_T_41` | EPH Tasa de subocupación - CABA | CABA | Subocupación | Porcentaje (0-1) | 2003-01 | 2026-04 | 46 |
| `43.2_ECTATPG_0_T_46` | EPH Tasa de actividad - Partidos de GBA | Partidos de GBA | Actividad | Porcentaje (0-1) | 2003-01 | 2026-04 | 43 |
| `44.2_ECTETPG_0_T_43` | EPH Tasa de empleo - Partidos de GBA | Partidos de GBA | Empleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 44 |
| `45.2_ECTDTPG_0_T_46` | EPH Tasa de desempleo - Partidos de GBA | Partidos de GBA | Desempleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 45 |
| `46.2_ECTSTPG_0_T_49` | EPH Tasa de subocupación - Partidos de GBA | Partidos de GBA | Subocupación | Porcentaje (0-1) | 2003-01 | 2026-04 | 46 |
| `43.2_ECTATGM_0_T_46` | EPH Tasa de actividad - Gran Mendoza | Gran Mendoza | Actividad | Porcentaje (0-1) | 2003-01 | 2026-04 | 43 |
| `44.2_ECTETGM_0_T_43` | EPH Tasa de empleo - Gran Mendoza | Gran Mendoza | Empleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 44 |
| `45.2_ECTDTGM_0_T_46` | EPH Tasa de desempleo - Gran Mendoza | Gran Mendoza | Desempleo | Porcentaje (0-1) | 2003-01 | 2026-04 | 45 |
| `46.2_ECTSTGM_0_T_49` | EPH Tasa de subocupación - Gran Mendoza | Gran Mendoza | Subocupación | Porcentaje (0-1) | 2003-01 | 2026-04 | 46 |
| `43.2_ECTATGP_0_T_45` | EPH Tasa de actividad - Gran Paraná | Gran Paraná | Actividad | Porcentaje (0-1) | 2003-07 | 2026-04 | 43 |
| `44.2_ECTETGP_0_T_42` | EPH Tasa de empleo - Gran Paraná | Gran Paraná | Empleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 44 |
| `45.2_ECTDTGP_0_T_45` | EPH Tasa de desempleo - Gran Paraná | Gran Paraná | Desempleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 45 |
| `46.2_ECTSTGP_0_T_48` | EPH Tasa de subocupación - Gran Paraná | Gran Paraná | Subocupación | Porcentaje (0-1) | 2003-07 | 2026-04 | 46 |
| `43.2_ECTATGR_0_T_50` | EPH Tasa de actividad - Gran Resistencia | Gran Resistencia | Actividad | Porcentaje (0-1) | 2003-07 | 2026-04 | 43 |
| `44.2_ECTETGR_0_T_47` | EPH Tasa de empleo - Gran Resistencia | Gran Resistencia | Empleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 44 |
| `45.2_ECTDTGR_0_T_50` | EPH Tasa de desempleo - Gran Resistencia | Gran Resistencia | Desempleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 45 |
| `46.2_ECTSTGR_0_T_53` | EPH Tasa de subocupación - Gran Resistencia | Gran Resistencia | Subocupación | Porcentaje (0-1) | 2003-07 | 2026-04 | 46 |
| `43.2_ECTATGSJ_0_T_47` | EPH Tasa de actividad - Gran San Juan | Gran San Juan | Actividad | Porcentaje (0-1) | 2003-07 | 2026-04 | 43 |
| `44.2_ECTETGSJ_0_T_44` | EPH Tasa de empleo - Gran San Juan | Gran San Juan | Empleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 44 |
| `45.2_ECTDTGSJ_0_T_47` | EPH Tasa de desempleo - Gran San Juan | Gran San Juan | Desempleo | Porcentaje (0-1) | 2003-07 | 2026-04 | 45 |
| `46.2_ECTSTGSJ_0_T_50` | EPH Tasa de subocupación - Gran San Juan | Gran San Juan | Subocupación | Porcentaje (0-1) | 2003-07 | 2026-04 | 46 |

El **total** de la EPH es el total de **31 aglomerados urbanos**, no el total nacional. Los valores son fracciones 0-1: `0.079` = 7.9% de desempleo.

### Aglomerados EPH: disponibilidad real en `/series/`

La EPH continua tiene 39 geografías (38 aglomerados/regiones + total). La tabla marca con ✓ las combinaciones que devolvieron datos en `/series/` y con — las que devolvieron 0 filas pese a estar registradas y `available=true`. Los IDs completos de las 4 tasas para cada geografía están en `catalog.json` → `streams.mercado_trabajo.aglomerados`.

| Aglomerado | key | Actividad | Empleo | Desempleo | Subocupación |
|---|---|---|---|---|---|
| Total 31 aglomerados urbanos | `TOTAL` | ✓ | ✓ | ✓ | ✓ |
| Bahía Blanca | `bahia_blanca` | ✓ | ✓ | ✓ | ✓ |
| CABA | `caba` | ✓ | ✓ | ✓ | ✓ |
| Comodoro Rivadavia | `comodoro_rivadavia` | ✓ | ✓ | ✓ | — |
| Concordia | `concordia` | ✓ | ✓ | ✓ | ✓ |
| Corrientes | `corrientes` | ✓ | — | ✓ | ✓ |
| Formosa | `formosa` | ✓ | ✓ | ✓ | — |
| GBA | `gba` | — | ✓ | — | ✓ |
| Gran Catamarca | `gran_catamarca` | ✓ | — | ✓ | — |
| Gran Córdoba | `gran_cordoba` | ✓ | ✓ | — | ✓ |
| Gran La Plata | `gran_la_plata` | — | ✓ | — | ✓ |
| Gran Mendoza | `gran_mendoza` | ✓ | ✓ | ✓ | ✓ |
| Gran Paraná | `gran_parana` | ✓ | ✓ | ✓ | ✓ |
| Gran Resistencia | `gran_resistencia` | ✓ | ✓ | ✓ | ✓ |
| Gran Rosario | `gran_rosario` | — | ✓ | — | ✓ |
| Gran San Juan | `gran_san_juan` | ✓ | ✓ | ✓ | ✓ |
| Gran Santa Fe | `gran_santa_fe` | ✓ | — | ✓ | ✓ |
| Gran Tucumán | `gran_tucuman` | ✓ | — | ✓ | ✓ |
| Jujuy | `jujuy` | ✓ | ✓ | ✓ | — |
| La Rioja | `la_rioja` | ✓ | ✓ | ✓ | ✓ |
| Mar del Plata | `mar_del_plata` | ✓ | ✓ | — | ✓ |
| Neuquén | `neuquen` | ✓ | ✓ | ✓ | — |
| Partidos de GBA | `partidos_gba` | ✓ | ✓ | ✓ | ✓ |
| Posadas | `posadas` | ✓ | — | ✓ | — |
| Rawson-Trelew | `rawson_trelew` | ✓ | — | — | — |
| Región Cuyo | `cuyo` | — | ✓ | ✓ | ✓ |
| Región Noreste | `nordeste` | ✓ | ✓ | ✓ | ✓ |
| Región Noroeste | `noroeste` | — | ✓ | — | ✓ |
| Región Pampeana | `region_pampeana` | — | ✓ | — | ✓ |
| Región Patagonia | `patagonia` | ✓ | ✓ | ✓ | ✓ |
| Río Cuarto | `rio_cuarto` | ✓ | ✓ | ✓ | ✓ |
| Río Gallegos | `rio_gallegos` | ✓ | ✓ | ✓ | — |
| Salta | `salta` | — | ✓ | — | ✓ |
| San Luis | `san_luis` | ✓ | ✓ | ✓ | ✓ |
| San Nicolás | `san_nicolas` | ✓ | ✓ | ✓ | ✓ |
| Santa Rosa | `santa_rosa` | ✓ | ✓ | ✓ | ✓ |
| Santiago del Estero | `santiago_del_estero` | ✓ | ✓ | — | ✓ |
| Ushuaia-Río Grande | `ushuaia_rio_grande` | ✓ | ✓ | ✓ | ✓ |
| Viedma-Carmen de Patagones | `viedma_carmen_patagones` | ✓ | — | ✓ | — |

Solo 17 geografías tienen las 4 tasas con datos: Total, Bahía Blanca, CABA, Concordia, Gran Mendoza, Gran Paraná, Gran Resistencia, Gran San Juan, La Rioja, Partidos de GBA, Región Noreste, Región Patagonia, Río Cuarto, San Luis, San Nicolás, Santa Rosa y Ushuaia-Río Grande. Las otras 22 tienen al menos una tasa vacía. Las regiones GBA, Pampeana, Noroeste y Cuyo **no** tienen las 4 tasas completas: GBA funciona en empleo y subocupación; Pampeana en empleo y subocupación; Noroeste en empleo y subocupación; Cuyo en empleo, desempleo y subocupación. Actividad y desempleo son las tasas con más huecos.

Huecos y trampas de la EPH:

- **Series registradas pero vacías:** varias combinaciones devuelven `data: []` y `count: 0` aunque el search diga `time_index_end=2026-04`, `available=true` y el CSV de la distribución tenga valores. Es un hueco del store de valores de la API, no del catálogo. El catálogo excluye esas combinaciones; si se necesitan, hay que bajar el CSV de la distribución (`downloadURL`).
- **Nulls estructurales:** el total tiene `null` en 2015-10 y 2016-01. Algunos aglomerados tienen huecos extra (p. ej. Gran Resistencia subocupación tiene 13 trimestres nulos: 2003-01/04, 2012-07 a 2016-01, 2018-04 y 2019-07). El tap debe emitir null o saltar esos períodos.
- **Códigos ambiguos:** `ECTATC` se usa para CABA, Concordia y Corrientes; el sufijo numérico desambigua. En empleo, `ECTETNO` es **nordeste** y `ECTETNE` es **noroeste** (al revés de la intuición y distinto de actividad). Usar la descripción del campo, no el código.
- **No mezclar EPH puntual y continua:** la EPH puntual es `R/P6M` y termina 2003-05; la continua es `R/P3M` y empieza 2003-01. El dataset 42 las mezcla. El catálogo usa solo la continua.
- **Subocupación demandante/no demandante:** datasets 47 y 48 (78 series cada uno). No se incluyen; son aperturas de la tasa de subocupación.
- **Anuales:** cada tasa tiene 39 series anuales (`*.1_*_A_*`) que terminan 2025-01. No mezclar con las trimestrales.

## Series excluidas verificadas (discontinuadas o de frecuencia incorrecta)

| Stream | ID | Descripción | Frec. | Inicio | Fin | Obs. | Motivo | Dataset |
|---|---|---|---|---|---|---|---|---|
| ipc | `97.2_ING_2008_M_17` | IPC Nivel General. Base Abril 2008. Mensual | monthly | 1993-01-01 | 2013-12-01 | 252 | discontinuada (base abril 2008) | Índice de Precios al Consumidor GBA (IPC-GBA). Base abril 2008. SERIE DISCONTINUADA |
| ipc | `100.3_I2NG_2003_M_22` | IPC Nivel General. Base 2003. Mensual | monthly | 2005-09-01 | 2008-03-01 | 31 | discontinuada (base 2003) | Índice de Precios al Consumidor (IPC) Nacional. Por capítulos. Base 2003. SERIE DISCONTINUADA |
| ipc | `98.3_INNG_2013_0_20` | Índice de Precios al Consumidor. Nivel general. Base 10/2013 - 9/2014. Mensual | monthly | 2013-12-01 | 2015-10-01 | 23 | discontinuada (IPC-NU 2013-2014) | Índice de Precios al Consumidor Nacional Urbano (IPC-NU). Base 10/2013 - 9/2014. SERIE DISCONTINUADA |
| emae | `10.3_ISOM_1993_M_29` | Serie original EMAE en Mensual. Índice (base 1993) | monthly | 1993-01-01 | 2013-12-01 | 252 | discontinuada (base 1993) | Estimador Mensual de Actividad Económica (EMAE). Base 1993 |
| emae | `143.1_NO_PR_2004_A_21` | EMAE. Base 2004 | annual | 2004-01-01 | 2025-01-01 | 22 | frecuencia anual (el stream EMAE es mensual) | Estimador Mensual de Actividad Económica (EMAE). Base 2004 |
| mercado_trabajo | `43.1_ECTAT_0_A_33` | Tasa de actividad total. En porcentaje. | annual | 2004-01-01 | 2025-01-01 | 22 | frecuencia anual (el stream es trimestral) | Principales variables ocupacionales. EPH continua. Actividad |
| mercado_trabajo | `42.2_EPAT_0_M_27` | Tasa de actividad total. En porcentaje. | semiannual | — | — | 0 | EPH puntual sin datos en /series/ | Principales variables ocupacionales. EPH puntual y continua. |

Además de las anteriores, el catálogo de la API conserva las bases IPC 1988 y 1974, la IPC-GBA base abril 2008 por aperturas y la IPC-NU por aperturas. Todas están marcadas `SERIE DISCONTINUADA` y varias devuelven pocas observaciones o ninguna en `/series/`; no se incluyen.

## Recomendación de agrupación en streams

Mantener tres streams, un registro por `(series_id, fecha)`:

| Stream | Clave primaria | Dimensiones | Medida | Unidad recomendada |
|---|---|---|---|---|
| `ipc` | `series_id`, `date` | `region`, `categoria`, `medida` | `value` | índice o porcentaje (convertir fracción ×100) |
| `emae` | `series_id`, `date` | `sector`, `medida` | `value` | índice o porcentaje (×100) |
| `mercado_trabajo` | `series_id`, `date` | `aglomerado`, `tasa`, `tipo_geografia` | `value` | porcentaje (×100) |

Diseño de extracción:

1. Agrupar los IDs por frecuencia antes de pedir: un request mensual para IPC (26 ids), uno mensual para EMAE (22 ids) y uno trimestral para EPH (28 ids). Nunca mezclar mensual con trimestral/anual en el mismo `ids`.
2. Pedir `metadata=full` y usar `meta[i+1].distribution.downloadURL` como referencia de linaje; `meta[0]` es el metadato general de la ventana, no de una serie.
3. Para incremental, usar `start_date` = último período cargado menos un período y `end_date` = hoy. La API acepta ambas.
4. Normalizar los porcentajes a 0-100 en el tap (o mantener la fracción y exponer `value_scale`), y documentar la unidad en el schema.
5. Descartar filas con `value=null` o emitirlas como null; no interpolares. Los nulls de 2015-10/2016-01 en EPH son estructurales.
6. No incluir las series `148.3_INIVEL*` para evitar duplicar el nivel general regional.
7. Para las combinaciones EPH vacías en la API, si se necesitan, implementar un extractor alternativo desde el CSV de la distribución; no asumir que el endpoint `/series/` las va a devolver.

## Huecos de cobertura

- IPC: no hay base posterior a dic-2016; el tramo 2015-11 → 2016-11 no tiene serie comparable. La serie nacional arranca 2016-12.
- IPC: las aperturas por división y región existen pero no están en el catálogo (84 series). Si se agregan, el stream pasa de 26 a 110 series.
- EMAE: la apertura sectorial es solo índice, no hay series de valor agregado en pesos en este stream; el EMAE es un índice de volumen.
- EPH: 22 de 39 geografías tienen al menos una tasa vacía en la API. Las regiones GBA/Pampeana/Noroeste/Cuyo no tienen las 4 tasas completas.
- EPH: el total es urbano (31 aglomerados), no nacional.
- Series históricas (IPC bases viejas, EMAE 1993, EPH puntual) están disponibles parcialmente pero no son comparables con las vigentes.
