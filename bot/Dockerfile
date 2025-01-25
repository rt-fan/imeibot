# bot/Dockerfile

FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Скопируйте папку imei_check в контейнер
COPY ./imei_api /bot/imei_api

# Копируем исходный код бота
COPY ./bot /bot

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска бота
CMD ["python", "bot.py"]