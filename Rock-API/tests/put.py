import requests


# Base Ip
BASE = "http://127.0.0.1:5000/"           
response = requests.put(BASE + "rock/" + "fuck", {"name": "fuck","desc":"we rock", "image": "none","rating": 1})
print(response.json())