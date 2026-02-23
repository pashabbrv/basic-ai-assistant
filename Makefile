.PHONY: install run run-docker lint format

install:
	uv sync --extra dev

run:
	uv run python main.py

run-docker:
	docker compose up --build

lint:
	ruff check .

format:
	ruff format .
