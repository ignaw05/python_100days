import requests

response = requests.get("https://opentdb.com/api.php?amount=5&category=21&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()
print(data)

