# Versionado y releases

El tap usa [SemVer](https://semver.org/). La versión vive en
`tap_indec/__init__.py` y `pyproject.toml` la lee desde ahí. Un tag `vX.Y.Z`
dispara el workflow de release, que construye el wheel, el sdist y publica la
GitHub Release.

## Qué cambia en cada número

| Cambio | Versión |
|---|---|
| Corrección de un bug sin cambiar el esquema | patch, `0.1.1` |
| Serie nueva en un stream existente | minor, `0.2.0` |
| Stream nuevo o columna nueva | minor, `0.3.0` |
| Cambio incompatible de esquema o estado | major, `1.0.0` |
| Cambio incompatible antes de 1.0 | minor, con nota de migración |

Antes de 1.0 la API puede cambiar. Igual se documenta cada cambio incompatible
en `CHANGELOG.md` y en las release notes.

## Checklist de release

1. Actualizá `CHANGELOG.md` con la versión y la fecha.
2. Corré:

   ```bash
   make lint
   make typecheck
   make test
   make test-integration
   uv build
   ```

3. Revisá que el wheel incluya `tap_indec/catalog.json` y `py.typed`.
4. Commiteá con `chore(release): prepara X.Y.Z`.
5. Creá el tag y empujalo:

   ```bash
   git tag -a vX.Y.Z -m "tap-indec X.Y.Z"
   git push origin vX.Y.Z
   ```

6. Verificá la release y los assets:

   ```bash
   gh release view vX.Y.Z
   ```

## Compatibilidad

- El estado guarda `series_last_dates` por stream. Un cambio de nombre de stream
  pierde el estado y fuerza una recarga.
- Agregar una columna al esquema no rompe el estado. El target tiene que
  aceptar la columna nueva.
- Quitar una serie del catálogo no borra su estado. El estado viejo queda
  ignorado.
- Cambiar la clave primaria requiere una migración en el target y una versión
  major.

## PyPI

Las releases 0.1.0 y 0.2.0 se publican como GitHub Release. La publicación en
PyPI queda para cuando el proyecto tenga una versión estable y un nombre
disponible.
