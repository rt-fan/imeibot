# bot/Dockerfile

FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код бота
COPY . .

# Указываем команду для запуска бота
CMD ["python", "bot.py"]