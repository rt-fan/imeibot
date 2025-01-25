# bot/bot.py

import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import httpx
import re
from dotenv import load_dotenv

load_dotenv()

# Получаем токен бота и белый список пользователей из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WHITELIST_USER_IDS = set(map(int, os.getenv('WHITELIST_USER_IDS').split(',')))

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

def is_valid_imei(imei: str) -> bool:
    return bool(re.match(r'^\d{15}$', imei))

async def query_imeicheck(imei: str) -> dict:
    api_url = "https://imeicheck.net/ajax/promo-check"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "api_key": "e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b",  # Sandbox API Key
        "imei": imei
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    if user_id not in WHITELIST_USER_IDS:
        await message.reply("У вас нет доступа к этому боту.")
        return
    
    imei = message.text.strip()
    if not is_valid_imei(imei):
        await message.reply("Пожалуйста, введите корректный 15-значный IMEI.")
        return
    
    imei_info = await query_imeicheck(imei)
    if imei_info is None:
        await message.reply("Не удалось получить информацию об IMEI.")
        return
    
    # Форматирование полученной информации
    response_text = f"Информация об IMEI:\n\n{imei_info}"
    await message.reply(response_text)

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())