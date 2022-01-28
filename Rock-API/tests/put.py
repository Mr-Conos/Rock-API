import requests


# Base Ip
BASE = "https://mrconos.pythonanywhere.com/"           
response = requests.put(BASE + "rock/" + "rock", {"name": "rock","desc":"Welcome to rock API where you can find rocks and rate them. This isn't what you think lol.", "image": "none","rating": 5})
print(response.json())