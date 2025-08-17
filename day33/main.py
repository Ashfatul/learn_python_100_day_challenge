import requests, datetime
lat = 23.7928448
lon = 90.3610368

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)
parameters = {
    "lat": lat,
    "lng": lon,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]

sunrise_min = data["results"]["sunrise"].split("T")[1].split(":")[1]
sunset_min = data["results"]["sunset"].split("T")[1].split(":")[1]

sunrise_sec = data["results"]["sunrise"].split("T")[1].split(":")[2]
sunset_sec = data["results"]["sunset"].split("T")[1].split(":")[2]

currentTime = datetime.datetime.now().hour