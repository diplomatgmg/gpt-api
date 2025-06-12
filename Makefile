.PHONY: help up venv lint lint-fix

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

up: ## compose up
	@docker compose up --wait -d

venv: ## Создает виртуальное окружение
	@uv sync --frozen --no-install-project --dev

lint: ## Запуск линтеров без правок
	@uv run ruff check . && \
	uv run isort . --check-only && \
	uv run ruff format --check . && \
	uv run mypy .

lint-fix: ## Запуск линтеров с правками
	@uv run ruff check . && \
	uv run isort . && \
	uv run ruff format . && \
	uv run mypy .
