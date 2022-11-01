import requests
from datetime import datetime
from os import environ

nutritionix_API_ID = "ea021ccf"
nutritionix_API_KEY = "49cdd36bb5924daf854f8e830222b1ea"
user_gender = "male"
user_weight_kg = "68"
user_height_cm = "176"
user_age = "20"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "X-APP-ID": nutritionix_API_ID,
    "X-APP-KEY": nutritionix_API_KEY
}

user_query = input("Tell me which exercises you did: ")

body = {
    "query": user_query,
    "gender": user_gender,
    "weight_kg": user_weight_kg,
    "height_cm": user_height_cm,
    "age": user_age
}

today = datetime.now()

response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=body)
result = response.json()
for exercises in result['exercises']:
    sheety_body = {
        "workout": {
            "date": f"{today.strftime('%d/%m/%Y')}",
            "time": f"{today.strftime('%X')}",
            "exercise": exercises['name'].title(),
            "duration": exercises['duration_min'],
            "calories": exercises['nf_calories']
        }
    }

sheety_url = "https://api.sheety.co/7fd905e8d258ed7243a2a9b784c52193/myWorkouts/workouts"
SHEETY_TOKEN = "qwertyuiopasdfg"
SHEETY_HEADER = {
    "Authorization": "Bearer qwertyuiopasdfg"
}
# responce = requests.get(url=sheety_url, headers=SHEETY_HEADER)

sheet_response = requests.post(url=sheety_url, json=sheety_body, headers=SHEETY_HEADER)
print(sheet_response.json())
