# Changelog

Todos los cambios relevantes se documentan acá. El formato sigue
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) y el versionado
[SemVer](https://semver.org/).

## [Sin publicar]

## [0.1.0] - 2026-11-17

### Agregado

- Primer release del tap con 76 series en los streams `ipc`, `emae` y
  `mercado_trabajo`.
- Catálogo con 26 series de IPC, 22 de EMAE y 28 de mercado de trabajo.
- Cliente HTTP con paginación, reintentos y errores con contexto.
- Estado incremental por serie, no por stream.
- Tests con fixtures reales de la API y verificación del catálogo contra la API.
- Documentación de streams, fuente, troubleshooting y guía de estilo.
- CI en Python 3.10 a 3.13, workflow de release y documentación en español.

[Sin publicar]: https://github.com/akalautaro/tap-indec/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/akalautaro/tap-indec/releases/tag/v0.1.0
