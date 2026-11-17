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

6. Verificá la release, los assets y la publicación en PyPI:

   ```bash
   gh release view vX.Y.Z
   curl -s https://pypi.org/pypi/tap-indec/json | jq -r .info.version
   ```

   El tag dispara tres jobs: `build`, `github-release` y `pypi`. Si `pypi`
   falla, la release de GitHub igual queda creada.

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

El paquete se publica como `tap-indec`. El job `pypi` del workflow de release lo
sube con Trusted Publishing: GitHub pide un token efímero a PyPI por OIDC, así
que no hay contraseñas ni tokens guardados en el repositorio.

La configuración en PyPI se hace una sola vez. En
https://pypi.org/manage/account/publishing/ se agrega un *pending publisher* con
estos valores:

| Campo | Valor |
|---|---|
| PyPI Project Name | `tap-indec` |
| Owner | `akalautaro` |
| Repository name | `tap-indec` |
| Workflow name | `release.yml` |
| Environment name | `pypi` |

El entorno `pypi` del workflow tiene que coincidir con ese último campo. Si no
coincide, PyPI rechaza el token y el job falla antes de subir nada.

Cuando la publicación falla, el tag y la GitHub Release ya existen. Se corrige
la configuración y se vuelve a correr el job `pypi` desde la pestaña Actions.

## Meltano Hub

El Hub indexa definiciones de plugins en el repositorio `meltano/hub`. La del
tap vive en `_data/meltano/extractors/tap-indec/akalautaro.yml`, donde el último
segmento es la variante y por convención es el dueño del repositorio.

Mientras no esté listado, el tap se instala con `meltano add --custom` o con una
definición propia en `meltano.yml`.

Para darlo de alta:

1. El repositorio tiene que ser público y el paquete tiene que estar en PyPI.
   `hub-utils` instala el tap en un entorno temporal y le corre `--about`.
2. Cloná el Hub y creá una rama:

   ```bash
   git clone https://github.com/meltano/hub.git
   cd hub
   git checkout -b add-tap-indec
   ```

3. Generá la definición:

   ```bash
   uv run hub-utils add --repo-url https://github.com/akalautaro/tap-indec
   ```

   La herramienta completa `pip_url`, `namespace`, `executable`, settings y
   capabilities desde `--about`, y agrega las entradas en
   `_data/default_variants.yml` y `_data/maintainers.yml`.

4. Revisá el YAML, corregí el formato y abrí el PR:

   ```bash
   uv run hub-utils yamllint fix _data/meltano/extractors/tap-indec/akalautaro.yml
   git add _data static/assets/logos
   git commit -m "Add tap-indec (akalautaro)"
   git push --set-upstream origin add-tap-indec
   ```

Los campos que `hub-utils` no puede inferir son `description`, `domain_url`,
`label`, `logo_url`, `maintenance_status` y `quality`. `quality` lo asigna el
equipo del Hub según los criterios de la guía de contribución; no se declara en
el PR.

Si preferís no tocar el repositorio del Hub, hay una plantilla de pedido de
plugin en `meltano/hub` que hace el mismo trabajo.
