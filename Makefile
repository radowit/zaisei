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
