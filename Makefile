lint:
	poetry run flake8 gendiff tests
test:
	poetry run pytest
coverage:
	poetry run pytest --cov=gendiff --cov-report xml
install:
	poetry install --with dev
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache coverage.xml htmlcov