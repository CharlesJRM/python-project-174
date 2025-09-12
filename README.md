### Gendiff

Proyecto para comparar archivos JSON y YML mostrando sus diferencias de manera clara.

### Instalación cmd

git clone https://github.com/CharlesJRM/python-project-174.git
cd python-project-174

📌 Instalar dependencias
poetry install
poetry show pyyaml
poetry lock
poetry update package
poetry add pytest-cov --dev

### Comandos de uso
poetry run gendiff --help
poetry run gendiff -h
poetry run python -v

### Instalación wsl

cd "/mnt/c/Users/python-project-174"
git clone https://github.com/CharlesJRM/python-project-174.git

📌 Instalar dependencias
pip install poetry

📌 Ejecutar flake8 (linting)
poetry run flake8

### Ejecucion del programa

#### Uso con JSON
Comparar dos archivos JSON:
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json

#### Uso con YAML
Comparar dos archivos YAML:
poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

#### Uso con JSON --format stylish 
poetry run gendiff --format stylish tests/fixtures/file1.json tests/fixtures/file2.json

#### Uso con JSON --format plain
poetry run gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json

#### Compilacion pruebas del programa
poetry run pytest -v

#### Uso con cli
poetry run pytest tests/test_gendiff_cli.py -v

#### Uso con yml
poetry run pytest tests/test_gendiff_yml.py -v

#### Uso con generate_diff
poetry run pytest tests/test_generate_diff.py -v

#### Uso con coverage
poetry run pytest --cov=gendiff --cov-report term-missing

### Demostracion ASCIINEMA
Demostración con **Asciinema**:

[![asciicast](https://asciinema.org/a/P35feJ6GIY2BQX8FB7EVQ9bzt.svg)](https://asciinema.org/a/P35feJ6GIY2BQX8FB7EVQ9bzt)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/CharlesJRM/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/CharlesJRM/python-project-174/actions)

### Proyecto Calculadora de Diferencias GitHub
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/CharlesJRM/python-project-174/python-app.yml?branch=main&logo=github&label=CI)](https://github.com/CharlesJRM/python-project-174/actions/workflows/python-app.yml)

### Codeclimate
[![Maintainability](https://qlty.sh/gh/CharlesJRM/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/CharlesJRM/projects/python-project-174)

### Code Coverage
[![Code Coverage](https://qlty.sh/gh/CharlesJRM/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/CharlesJRM/projects/python-project-174)
