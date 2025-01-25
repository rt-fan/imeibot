# # api/main.py

# import os
# from fastapi import FastAPI, HTTPException, Depends, Request
# from fastapi.security import APIKeyHeader
# import httpx
# import re
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()


# # Получаем токен из переменных окружения
# API_TOKEN = os.getenv('API_TOKEN')


# @app.get("/")
# def read_root():
#     return {"message": "Hello World", "token": API_TOKEN}


# api_key_header = APIKeyHeader(name='token', auto_error=False)

# async def get_api_token(token: str = Depends(api_key_header)):
#     if token != API_TOKEN:
#         raise HTTPException(status_code=401, detail="Недействительный или отсутствующий токен.")
#     return token


# def is_valid_imei(imei: str) -> bool:
#     return bool(re.match(r'^\d{15}$', imei))


# async def query_imeicheck(imei: str) -> dict:
#     api_url = "https://imeicheck.net/ajax/promo-check"
#     headers = {
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "api_key": "e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b",  # Sandbox API Key
#         "imei": imei
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.post(api_url, json=payload, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None


# @app.post("/api/check-imei")
# async def check_imei(request: Request, token: str = Depends(get_api_token)):
#     data = await request.json()
#     imei = data.get('imei')
#     if not imei:
#         raise HTTPException(status_code=400, detail="Параметр 'imei' обязателен.")
#     if not is_valid_imei(imei):
#         raise HTTPException(status_code=400, detail="Недействительный формат IMEI.")
    
#     imei_info = await query_imeicheck(imei)
#     if imei_info is None:
#         raise HTTPException(status_code=500, detail="Ошибка при запросе к сервису imeicheck.net.")
#     return imei_info

import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from dotenv import load_dotenv
from imei_check_api import check_api

load_dotenv()


# Получаем токен из переменных окружения
API_TOKEN = os.getenv('API_TOKEN')

app = FastAPI()

# Пример токена для авторизации
#VALID_TOKEN = "your_valid_token_here"

class IMEIRequest(BaseModel):
    imei: str
    token: str

def verify_token(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/api/check-imei")
async def check_imei(request: IMEIRequest):
    # Проверка токена
    verify_token(request.token)

    # Здесь можно добавить логику для обработки IMEI
    response = check_api(request.imei)
    # Например, получение информации о IMEI из базы данных или другого источника
    # imei_info = {
    #     "imei": request.imei,
    #     "status": "active",  # Пример статуса
    #     "device": "Example Device"  # Пример устройства
    # }

    return response

