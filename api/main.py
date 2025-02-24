
import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from dotenv import load_dotenv
from imei_api.imei_check_api import check_api

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

app = FastAPI()


class IMEIRequest(BaseModel):
    imei: str
    token: str


def verify_token(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/")
async def main_page():
    response = {
        "IMEI API": "/api/check-imei",
        "Telegram Bot": "@imei_api_2401_bot - Для доступа к IMEI API через телеграм, нужно занести ваш телеграм id в белый список"
    }
    return response


@app.post("/api/check-imei")
async def check_imei(imei: str = Query(..., description="The IMEI to check"), token: str = Query(..., description="API token")):
    verify_token(token)
    response = check_api(imei)
    return response
