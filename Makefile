#!make

export DJANGO_SETTINGS_MODULE=config.settings.local
export PYTHONPATH=.
include .envs/.local/.postgres
export
include .envs/.local/.django
export

test-unit:
	docker-compose -f local.yml up postgres -d
	pytest

test-unit-cov:
	docker-compose -f local.yml up postgres -d
	pytest --cov

deploy-local:
	docker-compose -f local.yml up --build

install:
	pip install -U pip
	pip install poetry
	poetry install

mypy:
	poetry run mypy config manage.py merge_production_dotenvs_in_dotenv.py zaisei
