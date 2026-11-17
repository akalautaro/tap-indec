# Arquitectura

El tap usa el Singer SDK y tres piezas propias: el catálogo, el cliente HTTP y
los streams. El catálogo dice qué series se emiten. El cliente pide una serie y
devuelve sus puntos. Los streams convierten esos puntos en registros y guardan
el estado.

```text
tap_indec/
├── tap.py          # configuración y descubrimiento
├── streams.py      # streams, esquema y estado incremental
├── client.py       # HTTP, paginación y errores
└── catalog.json    # 76 series con metadatos y dimensiones
```

## Flujo

1. `TapIndec` valida la configuración y descubre `ipc`, `emae` y
   `mercado_trabajo`.
2. Cada stream lee su parte del catálogo y arma el esquema con las dimensiones
   que aparecen en sus series.
3. Para cada serie, el stream busca la última fecha en el estado y pide los
   puntos nuevos al cliente.
4. El cliente pagina hasta agotar `count`, reintenta ante 429 y 5xx y convierte
   los errores de la API en `IndecAPIError`.
5. El stream emite un registro por punto con valor no nulo y actualiza la fecha
   de esa serie en el estado.
6. El SDK escribe los mensajes `RECORD` y `STATE` en JSONL.

## Decisiones

### Un stream por indicador

`ipc`, `emae` y `mercado_trabajo` agrupan series de la misma frecuencia. Las
aperturas (región, categoría, sector, aglomerado, medida) son columnas. Si cada
serie fuera un stream, el catálogo tendría 76 streams y el usuario tendría que
elegir uno por uno.

### Una serie por request

La API acepta hasta 40 IDs por request, pero si uno no existe responde 400 y no
devuelve nada. Pedir de a una serie acota el error y permite guardar estado por
serie. El costo es una llamada por serie: 76 en la primera carga.

### Estado por serie

El estado no es un único bookmark por stream. Guarda la última fecha con valor
de cada serie:

```json
{
  "bookmarks": {
    "ipc": {
      "series_last_dates": {
        "145.3_INGNACNAL_DICI_M_15": "2026-10-01"
      }
    }
  }
}
```

Así una serie que se publica más tarde no arrastra a las demás ni se saltea
períodos. El tap pide desde la última fecha inclusive, para volver a leer el
último punto y corregir revisiones.

### Catálogo empaquetado

`catalog.json` viaja dentro del paquete. El tap no descubre series en runtime:
emite lo que está en el catálogo. Agregar una serie es un cambio de datos, no de
código, y el test de integración verifica que el ID exista.

### Errores

Un error de red o un 5xx se reintenta con backoff. Un 400 corta el sync por
defecto, porque suele ser un ID muerto. Con `fail_on_series_error: false` el tap
registra el ID y sigue con la próxima serie.

### Nulos

Un `null` en la API significa que la fuente no publicó ese período. El tap no
emite la fila y no interpola. El estado se queda en la última fecha con valor.

## Pruebas

- Tests unitarios con fixtures reales de la API, sin red.
- Tests de integración que verifican cada ID del catálogo contra `/series/`.
- CI en Python 3.10 a 3.13 con ruff, mypy y cobertura mínima de 85 %.
- Workflow semanal para detectar series que la API dejó de devolver.

## Lo que queda afuera

- Microdatos de la EPH.
- Archivos Excel del sitio de INDEC.
- Aperturas por división y región del IPC (84 series adicionales).
- Las 39 geografías de la EPH: la 0.1.0 incluye siete.
- Empalmes de series con cambios de base o metodología.
