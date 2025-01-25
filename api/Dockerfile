# api/Dockerfile

FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /api

# Скопируйте папку imei_check в контейнер
COPY ../imei_api /api/imei_api

# Копируем исходный код приложения
COPY ./api /api
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]