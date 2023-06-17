.PHONY: init upd fmt style tests verify

init:
	poetry install
	pre-commit install

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
	pylint --fail-under=9 currency_codes

tests:
	pytest tests -vv

pre-commit-check:
	pre-commit run

verify: fmt style tests pre-commit-check
