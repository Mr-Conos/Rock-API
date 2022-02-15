import requests


# Base Ip
BASE = "http://127.0.0.1:5000/"           
response = requests.put(BASE + "rock/" + "crunchy rock", {"name": "crunchy rock","desc":"Pretty crunchy rock tbh. Great for snacking, eating, drinking, and snacking!", "image": "none","rating": 4})
print(response.json())