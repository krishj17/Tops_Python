import requests

data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=21.1702&longitude=72.8311&current_weather=true")

print(data.json())