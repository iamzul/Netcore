import requests
import json, os
from dotenv import load_dotenv
load_dotenv()

url = "https://apiind.netcoresmartech.com/v4/audience/list"

payload = json.dumps({
  "audience_details": {
    "audience_type": "segment",
    "audience_id": 50,
    "attributes_needed": [
      "email"
    ],
    "blocklist_type": "email"
  },
  "file_type": "csv",
  "notify_email": "zulkifliarshd@gmail.com",
  "callback_details": {
    "method": "POST",
    "endpoint": "https://www.ideaktiv.com/callback",
    "header": [],
    "body": {}
  }
})
headers = {
  'api-key': os.getenv('netcore_apikey'),
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
