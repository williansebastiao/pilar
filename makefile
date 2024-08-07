SHELL := /bin/bash
.DEFAULT_GOAL := help
DOCKER_COMPOSE := docker-compose
POETRY := poetry run

.PHONY: help start build stop container flake8 black isort autoflake pylint pytest pre-commit pre-commit-install

help:
	@echo "Pilar Makefile"
	@echo "---------------------"
	@echo "Usage: make <command>"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-26s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

start: ## Start all containers
	$(DOCKER_COMPOSE) up -d

build: ## Build all containers without detach
	$(DOCKER_COMPOSE) up --build

stop: ## Stop all containers
	$(DOCKER_COMPOSE) down

container: ## Enter the container
	docker exec -it pilar-app bash

flake: ## Run flake8
	poetry run flake8 .

black: ## Run black
	poetry run black .

isort: ## Run isort
	poetry run isort .

autoflake: ## Run autoflake
	poetry run autoflake .

pylint: ## Run pylint
	poetry run pylint .  --recursive=true

pytest: ## Enter the container and run pytest
	docker exec pilar-app poetry run pytest

pre-commit: ## Running pre-commit
	poetry run pre-commit run --all-files

pre-commit-install: ## Install pre-commit
	poetry run pre-commit install --allow-missing-config
