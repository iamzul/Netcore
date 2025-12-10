import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('netcore_apikey')
BASE_URL = 'https://api.netcoresmartech.com/v4/audience/export'  
payload = {
    "audience_details" : {
        "audience_type" : "segment",
        "audience_id" : 50,
        "atrributes_needed" : ["email", "mobile"]
    },
    "notify_email" : "zulkifli_ritzwan@ideaktiv.com",
    "callback_details" : {
        "method": "POST",
        "endpoint" : "https://www.ideaktiv.com/callback",
        "header" : [{
        }]
    }
}

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

resp = requests.post(BASE_URL, json=payload, headers=headers)
data = resp.json()
print(data)

