# Changelog

Todos los cambios relevantes se documentan acá. El formato sigue
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) y el versionado
[SemVer](https://semver.org/).

## [Sin publicar]

## [0.2.0] - 2026-11-17

### Agregado

- 72 series nuevas de IPC: las 12 divisiones de la canasta para las seis
  regiones. El stream `ipc` pasa de 26 a 98 series.
- 95 series nuevas de `mercado_trabajo`: el catálogo cubre 123 de las 156
  combinaciones de geografía y tasa de la EPH continua, contra 28 de la 0.1.0.
- Setting `full_refresh` para ignorar el estado y recargar cada serie desde
  `start_date` o desde su primera fecha disponible.
- Tests de cobertura del catálogo y del modo `full_refresh`.

### Cambiado

- La documentación de streams refleja las nuevas series y la cobertura real de
  la EPH.
- El catálogo empaquetado pasa de 76 a 243 series.

## [0.1.0] - 2026-11-17

### Agregado

- Primer release del tap con 76 series en los streams `ipc`, `emae` y
  `mercado_trabajo`.
- Catálogo con 26 series de IPC, 22 de EMAE y 28 de mercado de trabajo.
- Cliente HTTP con paginación, reintentos y errores con contexto.
- Estado incremental por serie, no por stream.
- Tests con fixtures reales de la API y verificación del catálogo contra la API.
- Documentación de streams, fuente y troubleshooting.
- CI en Python 3.10 a 3.13, workflow de release y documentación en español.

[Sin publicar]: https://github.com/akalautaro/tap-indec/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/akalautaro/tap-indec/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/akalautaro/tap-indec/releases/tag/v0.1.0
