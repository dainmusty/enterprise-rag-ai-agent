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