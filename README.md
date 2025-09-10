# Gendiff

Proyecto para comparar archivos JSON y YML mostrando sus diferencias de manera clara.

## Instalación
```bash
git clone https://github.com/CharlesJRM/python-project-174.git
cd python-project-174
poetry install
poetry show pyyaml
poetry lock
poetry update package
poetry add pytest-cov --dev
poetry run flake8 gendiff tests
poetry run pytest --version


# Ayuda del CLI
poetry run gendiff -h
:: si falla por entrypoint:
poetry run python -m gendiff.scripts.gendiff -h

# Linter
poetry run flake8 gendiff tests

# Tests
poetry run pytest -q
:: cobertura
poetry run pytest --cov=gendiff --cov-report xml

# CLI examples
poetry run gendiff tests\fixtures\file1.json tests\fixtures\file2.json
poetry run gendiff -f plain tests\fixtures\file1.json tests\fixtures\file2.json
poetry run gendiff -f json tests\fixtures\file1.json tests\fixtures\file2.json

## Comandos de uso
poetry run gendiff --help
poetry run gendiff -h
poetry run python -v

## Uso con JSON
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json

## Uso con JSON --format stylish 
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json --format stylish

## Uso con JSON --format plain
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml --format plain

## Uso con cli
poetry run pytest tests/test_gendiff_cli.py -v

## Uso con coverage
poetry run pytest --cov=gendiff --cov-report term-missing

## Uso con coverage reporte HTML
poetry run pytest --cov=gendiff --cov-report html

## Uso con YAML
Comparar dos archivos YAML:

```bash
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml




## Demostracion ASCIINEMA

Demostración con **Asciinema**:
```markdown
[![asciicast](https://asciinema.org/a/rd2GVsqMOdIKu6064BvzKh6tq.svg)](https://asciinema.org/a/rd2GVsqMOdIKu6064BvzKh6tq)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/CharlesJRM/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/CharlesJRM/python-project-174/actions)


![GitHub Actions](https://github.com/CharlesJRM/python-project-174/actions/workflows/python-app.yml)

[![Maintainability](https://qlty.sh/gh/CharlesJRM/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/CharlesJRM/projects/python-project-174)

[![Code Coverage](https://qlty.sh/gh/CharlesJRM/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/CharlesJRM/projects/python-project-174)
