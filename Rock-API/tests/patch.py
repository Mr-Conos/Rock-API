import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "rate/" + "test", {"rating":0})
print(response.json())