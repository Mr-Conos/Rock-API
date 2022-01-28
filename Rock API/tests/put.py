import requests


# Base Ip
BASE = "https://mrconos.pythonanywhere.com/"           
response = requests.put(BASE + "rock/" + "test", {"name": "test","desc":"test rock", "image": "none","rating": 4})
print(response.json())