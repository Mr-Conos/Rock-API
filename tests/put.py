import requests


# Base Ip
BASE = "http://127.0.0.1:5000/"           
response = requests.put(BASE + "rock/" + "test", {"name": "test","desc":"test rock", "image": "none","rating": 4})
print(response.json())