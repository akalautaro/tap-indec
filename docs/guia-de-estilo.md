# Guía de estilo

Cómo se escribe en tap-indec: README, docstrings, comentarios, errores,
documentación de streams, commits y release notes. Adaptada de
[`declauding`](https://github.com/oaustegard/claude-skills/tree/main/declauding),
un catálogo de las marcas que dejan los modelos de lenguaje en la prosa técnica.
La regla de fondo: cada oración dice el dato o lo hace aparecer.

## El test de una oración

Preguntate si la oración enuncia el hallazgo o si lo presenta. `El tap pide una
página por serie` enuncia. `Y acá aparece el problema de la paginación` presenta.
La segunda forma obliga al lector a esperar el dato. Aplicá el test a cada
oración del README, a cada docstring y al cuerpo del commit. No recortes de más:
la certeza con evidencia y la opinión del autor se quedan.

## Construcciones para evitar

**Negación primero.**
Mal: `El problema no es el formato de la respuesta, sino la paginación.`
Bien: `La respuesta viene paginada de a 1000 puntos, así que el tap pide una página por serie.`

Si el lector ya sostenía la lectura equivocada, el contraste entra en una cláusula: `La paginación, no el formato, obliga a partir el request.`

**Importancia designada.**
Mal: `El catálogo es la parte que importa.`
Bien: `El catálogo define qué series emite cada stream.`

`Lo interesante`, `el verdadero desafío` y `la clave está en` ordenan la lectura por vos.

**Agencia abstracta.**
Mal: `El schema esconde las series discontinuadas.`
Bien: `El tap omite las series discontinuadas salvo que include_discontinued sea true.`

Si el sujeto no puede actuar, la oración esconde al actor.

**Sustantivo diferido.**
Mal: `Hay un stream que falla con fechas viejas.`
Bien: `ipc falla si la fecha es anterior a la primera publicación: la API devuelve 404.`

**Encabezados.**
Mal: `Qué significa "serie discontinuada"` / `Por qué el EMAE llega tarde`
Bien: `Series discontinuadas` / `Demora del EMAE`

Un encabezado es una entrada de índice, sin comas ni cláusulas relativas.

**Cierre aforístico.**
Mal: `Al final, un tap es tan bueno como los datos que trae.`
Bien: `El tap no valida valores; eso queda en el modelo de dbt.`

**Tríadas.**
Mal: `El tap es simple, robusto y escalable.`
Bien: `El tap hace un request por serie y reintenta solo ante 429 y 5xx.`

**Guion largo y dos puntos.**
Mal: `El cliente funciona — salvo cuando la API devuelve HTML en vez de JSON.`
Bien: `El cliente funciona. Si la API devuelve HTML, falla con ParseError.`

Máximo un guion largo cada 150 palabras. Reemplazalo por una coma: si el sentido no cambia, era paréntesis; si se pierde el golpe, era suspenso. Los dos puntos que cierran un párrafo para revelar algo en la línea siguiente también sobran.

**Negrita decorativa.**
Mal: `**Importante**: el token vence a los 30 minutos.`
Bien: `El token vence a los 30 minutos.`

**Hedging.**
Mal: `En algunos casos podría llegar a ocurrir que la API devuelva un error.`
Bien: `Si la serie no existe, la API devuelve 404.`

Un hedge con contenido se queda: `en 2 de 10 corridas la API devolvió 502`.

**Autoevaluación y humildad.**
Mal: `Cabe aclarar que los tests son rigurosos.`
Bien: `Los tests comparan las 12 filas del fixture contra la respuesta grabada.`

**Documentación anclada al diff.**
Mal: `Este stream se agregó para reemplazar el scraping de HTML.`
Bien: `El stream emae lee la API de series; no parsea HTML.`

`Ahora`, `ya no`, `antes` y `se reemplazó` describen el cambio, no el estado.

**Metáfora y rango falso.**
Mal: `El catálogo es la columna vertebral del tap.`
Bien: `El catálogo lista las series y sus campos.`

Mal: `Desde series mensuales hasta microdatos.`
Bien: `Emite IPC, EMAE y mercado de trabajo.`

**Sintaxis comprimida.**
Mal: `El test verifica el stream devuelve los campos.`
Bien: `El test verifica que el stream devuelve los campos.`

Mal: `el proceso de validación de esquema de respuesta de la API`
Bien: `validar el esquema de la respuesta de la API`

Si el sujeto espera detrás de una lista para recibir su verbo, adelantá el verbo.

## Léxico

| En vez de | Escribí |
|---|---|
| robusto, potente, sin fisuras | qué hace y bajo qué condiciones |
| permite obtener, realiza, se encarga de | devuelve, pide, extrae |
| actúa como, sirve como | es |
| cuenta con | tiene |
| a la hora de | cuando, para |
| en este sentido, por otro lado | nada |
| es importante destacar, cabe señalar | nada |
| en el mundo actual, en la era de los datos | nada |
| de vanguardia, de última generación | la versión o el estándar |
| escalable | cuántas filas o requests por minuto |
| bajo el capó | el archivo o la función que lo hace |
| el tap, la herramienta, la integración (para el mismo objeto) | el tap |
| ¡Excelente pregunta!, espero que te sirva | nada |

## README

Orden de secciones, sin agregar otras:

1. Una oración: qué es y qué produce.
2. Requisitos e instalación: Python, Meltano y los comandos que corriste.
3. Configuración: tabla de settings con tipo, default y si es obligatorio.
4. Uso: un comando y tres líneas de salida real.
5. Streams: tabla con nombre, endpoint, granularidad y clave primaria.
6. Limitaciones: qué no hace y qué asume.
7. Desarrollo: tests y lint.
8. Licencia.

- Primera oración sin adjetivos: `tap-indec extrae series del INDEC y las escribe
  como JSONL de Singer.`
- Nada de historia ni roadmap. Si no aceptás PRs, decilo en una línea.
- Las limitaciones se nombran con el caso que falla: `La API corta a 1000 puntos
  por request.` No `puede haber limitaciones de volumen`.

Mal: `tap-indec es una solución moderna y robusta que te permite integrar los datos del INDEC a tu stack de manera simple y eficiente.`
Bien: `tap-indec extrae series del INDEC y las escribe como JSONL de Singer. Emite tres streams: ipc, emae y mercado_trabajo.`

## Docstrings y comentarios

La primera línea dice qué hace o qué devuelve. Después, unidades, nulos, efectos
secundarios y excepciones.

Mal: `"""Esta función se encarga de obtener la serie indicada."""`

Bien:

```python
def get_series(serie_id: str) -> list[dict]:
    """Devuelve los puntos de una serie, paginando hasta agotarla.

    Una serie sin datos devuelve una lista vacía; no lanza excepción.
    """
```

- No repitas el nombre de la función ni empieces con `Esta función`.
- Documentá el formato del argumento: `YYYY-MM-DD`, no `la fecha`.
- Decí qué significa un nulo: `value: null` es un punto sin publicación, no un cero.
- Los comentarios explican por qué. `# la API cuenta las páginas desde 1` sirve;
  `# incremento el contador` no.
- Sin código comentado. Un `TODO` lleva issue: `# TODO(#42): paginar emae`.

## Errores y troubleshooting

Un mensaje de error dice qué falló, con qué input y qué hacer después.

Mal: `Ocurrió un error inesperado.`
Bien: `No se pudo parsear la respuesta de ipc para 2024-03-01: el cuerpo empieza con <html>, no con {. Reintentá en unos minutos; si persiste, abrí un issue con la fecha.`

En troubleshooting el orden es síntoma, causa, solución, con el comando incluido.
Mal: `Si tenés problemas, revisá la configuración.` Bien: `Si meltano invoke
tap-indec no emite nada, revisá que start_date sea anterior a end_date. El tap no
avisa cuando el rango está invertido.`

## Documentación de streams

Cada stream tiene su archivo en `docs/streams/` con:

- Qué mide y en qué unidad: `pesos corrientes`, `índice base 2004=100`.
- Endpoint y parámetros que usa el tap.
- Clave primaria y granularidad: una fila por fecha, por fecha y región.
- Significado de los nulos y demora de publicación de la fuente.
- Una fila de ejemplo.

No copies el schema entero. Una tabla de campos con tipo y unidad se lee mejor. Si
renombrás un campo de la fuente, decilo: `fecha` se emite como `date`.

## Commits

Conventional Commits, en el idioma del repo y sin mezclar.

```
<tipo>(<scope>): <resumen>
<cuerpo: por qué>
<footer>
```

Tipos: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`. Scope: el stream
o el módulo (`ipc`, `emae`, `catalog`, `client`).

- Resumen de 72 caracteres como máximo, en minúscula, sin punto final.
- Verbo en tercera persona: `agrega`, `corrige`, `documenta`.
- Sin emojis, sin `WIP`, sin `varios cambios`.
- Un commit, un cambio lógico. Si el cuerpo necesita `y también`, son dos.
- El cuerpo explica por qué. El diff ya dice qué cambió.
- Cambio incompatible: `BREAKING CHANGE:` en el footer y qué hacer para migrar.

Mal: `feat: mejoras en el tap`

Bien:

> fix(ipc): pagina por serie cuando la respuesta supera 1000 puntos
>
> La API devuelve como máximo 1000 puntos y no incluye cursor. Sin paginar, las
> series largas se truncaban sin error.
>
> Refs #42

## Release notes

Una sección por versión, con fecha y los grupos `Agregado`, `Cambiado`,
`Corregido`, `Eliminado`, `Seguridad`. Cada línea dice qué cambió para quien usa
el tap, con el stream y el número de issue.

Mal: `## 1.2.0` seguido de `¡Gran actualización! Mejoramos un montón de cosas y dejamos el tap más robusto que nunca.`

Bien:

> ## 1.2.0 - 2026-11-16
>
> ### Corregido
> - `ipc`: la paginación ya no duplica el último punto cuando la serie cae en el
>   límite de 1000 registros (#42).
>
> ### Cambiado
> - `mercado_trabajo`: el campo `region` pasa a `region_id`. Actualizá el modelo
>   de dbt antes de correr la próxima extracción.

Las release notes son el único lugar donde `ahora` y `ya no` están bien.

## Checklist

1. ¿La primera oración del README dice qué hace el tap, sin adjetivos?
2. ¿Cada encabezado funciona como entrada de índice?
3. ¿Cada oración tiene un sujeto que puede actuar?
4. ¿Están dichos los números, las unidades y el significado de los nulos?
5. ¿Quedan guiones largos, dos puntos o negritas que solo buscan suspenso?
6. ¿Quedó alguna tríada, algún `no es X sino Y` o un cierre que repite lo anterior?
7. ¿El texto describe el estado actual y no la historia del cambio?
8. ¿El commit explica por qué, con un resumen de menos de 72 caracteres?
9. ¿Las release notes nombran el stream y el efecto sobre quien usa el tap?
10. ¿Hay algún dato, fecha o nombre que no esté en la fuente?
