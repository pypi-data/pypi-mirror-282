## Version 1.20.0 (2024-07-02)
### 🎉 New features

- sqlite: boolean are now returned as python bool, instead of 0 or 1 (https://forge.extranet.logilab.fr/cubicweb/cubicweb/-/issues/1051)

## Version 1.19.0 (2024-01-03)
### 🎉 New features

- setup.py: enforce semver dependencies for our own packages (logilab-*)

## Version 1.18.6 (2023-11-14)
### 🤷 Various changes

- remove an import to logilab.common.modutils

## Version 1.18.5 (2023-10-17)
### 👷 Bug fixes

- postgres: schemas list had trailing spaces which broke later on code
- setup.py: without include_package_data python files aren't distributed for some reason

### 🤷 Various changes

- README has been renamed to README.rst
- remove autodoc for modules that have been removed

## Version 1.18.4 (2023-07-18)
### 👷 Bug fixes

- python 3.11 compatibility: inspect.getargspec has been deprecated

## Version 1.18.3 (2023-07-04)
### 👷 Bug fixes

- psycopg2: escape mostly all easy functions to escape (#1)

## Version 1.18.2 (2023-02-23)
### 👷 Bug fixes

- use maintained yapps2-logilab
- uses psycopg2-binary for tests

### 🤖 Continuous integration

- add check-dependencies-resolution
- add twine-check job
- disable heavy consuming jobs since the CI is dying
- make py3-from-forge extends from .retry
- make py3-from-forge interruptible
- move the v2 of gitlab templates
- move to native heptapod rtfd integration
- use templates

## Version 1.18.1 (2021-08-06)

### 🤷 Various changes

- maintenance release to remove deprecation warnings

## Version 1.18.0 (2021-05-04)
### 🎉 New features

- order: add support for order by NULLS LAST and NULLS FIRST
- order: use specific postgres function to order by NULLS LAST and NULLS FIRST

### 🤷 Various changes

- bump version to 1.17.2
- Remove mysql compatibility since it's no more used.
- Remove sqlserver compatibility since it's no more used.
