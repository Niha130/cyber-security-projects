import requests
from config import API_URL, API_KEY

def check_ip(ip):
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        return response.json()
    except:
        return {"error": "API request failed"}
