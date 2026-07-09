.PHONY: help up down logs backend frontend ollama model clean

help:
	@echo "Enterprise RAG AI Agent"
	@echo ""
	@echo "Available commands:"
	@echo "  make up         - Build and start all containers"
	@echo "  make down       - Stop containers"
	@echo "  make logs       - Show all logs"
	@echo "  make backend    - Backend logs"
	@echo "  make frontend   - Frontend logs"
	@echo "  make ollama     - Ollama logs"
	@echo "  make model      - List installed Ollama models"
	@echo "  make clean      - Remove containers and volumes"

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

backend:
	docker compose logs -f backend

frontend:
	docker compose logs -f frontend

ollama:
	docker compose logs -f ollama

model:
	docker compose exec ollama ollama list

clean:
	docker compose down -v