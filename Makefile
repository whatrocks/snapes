build:
	docker-compose build

run:
	docker-compose up -d

build-and-run:
	make build
	make run

build-local:
	pip3 install --no-cache-dir -e ".[dev]"

unit:
	pytest

static-analysis:
	mypy --ignore-missing-imports snapes

check:
	flake8 snapes tests

check-all:
	make check
	make static-analysis
	make unit
