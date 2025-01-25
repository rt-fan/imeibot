import requests
import json
import os
import re
from dotenv import load_dotenv

load_dotenv()


IMEI_API_TOKEN = os.getenv('IMEI_API_TOKEN')
url = 'https://api.imeicheck.net/v1/checks'


def is_valid_imei(imei: str) -> bool:
    return bool(re.match(r'^\d{15}$', imei))


async def check_api(imei: str):
    headers = {
    'Authorization': 'Bearer ' + IMEI_API_TOKEN,
    'Content-Type': 'application/json'
    }
    body =  json.dumps({
    "deviceId": imei,
    "serviceId": 1
    })
    response = requests.post(url, headers=headers, data=body)
    return response.text
