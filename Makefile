lint:
	poetry run flake8 gendiff tests
test:
	poetry run pytest
coverage:
	poetry run pytest --cov=gendiff --cov-report xml
