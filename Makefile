.PHONY: init upd fmt style tests verify

init:
	poetry install

upd:
	poetry lock

shell:
	poetry shell

fmt:
	isort .
	black .

style:
	python -m isort --check --diff .
	python -m black --check --diff .
	python -m mypy -p currency_codes

tests:
	python -m pytest tests -vv

verify: fmt style tests
