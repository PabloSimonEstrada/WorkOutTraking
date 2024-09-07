import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "96"
HEIGHT_CM = "182"
AGE = "27"
TOKEN = os.getenv("TOKEN")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
URL = "trackapi.nutritionix.com/"

post_url = f" https://{URL}v2/natural/exercise"

parameters = {
    "query": input("Tell me what exercises you do: ")

}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(post_url, headers=headers, json=parameters)
result = response.json()
print(result)
sheet_post_url = 'https://api.sheety.co/4d4104b03c989c8fd324ac2fb2c2ea49/myWorkouts/workouts'

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_header = {"Authorization": f"Bearer {TOKEN}"}
for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }}
    sheet_response = requests.post(url=sheet_post_url, json=sheet_input, headers=bearer_header)
