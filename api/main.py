
import os
from fastapi import FastAPI, HTTPException, Depends
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


@app.post("/api/check-imei")
async def check_imei(request: IMEIRequest):
    verify_token(request.token)
    response = check_api(request.imei)
    return response
