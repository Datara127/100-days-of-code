import requests

parametrs = {
    "amount": 5,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=boolean",
                             params=parametrs)
response.raise_for_status()
data = response.json()
question_data = data["results"]
#print(data["results"][0]["question"])



