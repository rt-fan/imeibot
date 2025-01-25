.PHONY: rebuild up down build logs api bot

r:
	docker-compose down
	docker image prune -a -f
	docker-compose build
	docker-compose up -d

# Остановка контейнеров, пересборка образов и перезапуск
rebuild:
	docker-compose down
	docker-compose build
	docker-compose up -d

# Запуск контейнеров
up:
	docker-compose up -d

# Остановка контейнеров
down:
	docker-compose down

# Пересборка образов
build:
	docker-compose build

# Просмотр логов
logs:
	docker-compose logs -f

# Зайти в контейнер
api:
	docker compose exec -it api bash

bot:
	docker compose exec -it bot bash