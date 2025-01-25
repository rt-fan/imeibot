import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
from imei_api.imei_check_api import is_valid_imei, check_api

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WHITELIST_USER_IDS = set(map(int, os.getenv('WHITELIST_USER_IDS').split(',')))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


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
    
    imei_info = await check_api(imei)
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
