# Required Libraries
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


# Получаем токен из переменных окружения
IMEI_API_TOKEN = os.getenv('IMEI_API_TOKEN')
# Base URL
url = 'https://api.imeicheck.net/v1/checks'


def check_api(imei: str):
    # Add necessary headers
    headers = {
    'Authorization': 'Bearer ' + IMEI_API_TOKEN,
    'Content-Type': 'application/json'
    }

    # Add body
    body =  json.dumps({
    "deviceId": imei,
    "serviceId": 1
    })

    # Execute request
    response = requests.post(url, headers=headers, data=body)

    return response.text

print(check_api("356735111052198"))
