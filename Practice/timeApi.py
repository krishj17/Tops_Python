import requests

city = input("Enter the city name: ")
country = "IN"
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&country={}'.format(city, country)
response = requests.get(api_url, headers={'X-Api-Key': 'Ml3g87KuYSLZRHn80iTUDA==8legTfsX9LU9nvLf'})
data = response.json()
lat = data[0]["latitude"]
lon = data[0]["longitude"]

response2 = requests.get(f"http://api.timezonedb.com/v2.1/get-time-zone?key=SNVFB13ZN7AY&format=json&by=position&lat={lat}&lng={lon}")

data2 = response2.json()
arr = str(data2["formatted"]).split(" ")
print(f"Date: {arr[0]}\nTime: {arr[1]}")