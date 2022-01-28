import requests

BASE = "https://mrconos.pythonanywhere.com/"

response = requests.patch(BASE + "rock/" + "bruce rock", {"desc":"A bruce rock. Rock = Bruce. Bruce = Rock. Could take over the world of used 555 times."})
print(response.json())