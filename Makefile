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
	isort --check --diff .
	black --check --diff .
	mypy -p currency_codes

tests:
	pytest tests -vv

verify: fmt style tests
