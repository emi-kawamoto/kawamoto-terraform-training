"""training python api"""
import json
import requests
from dotenv import load_dotenv
import os
load_dotenv()

app_id = os.getenv("API_KEY")

url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "Fujimino", "appid": app_id}

res = requests.get(url, params=params)
jsonText = res.json()
print(json.dumps(jsonText, indent=4))
