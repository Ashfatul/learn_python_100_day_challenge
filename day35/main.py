from operator import contains
import requests, os

params = {
    "lat": 17.231,
    "lon": 73.737,
    "cnt": 3,
    "appid": "51aa0d3d1ca0b5cd83d667813a83d60c"
}


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

# rain = []
willrain = False

for item in data["list"]:
    for w in item["weather"]:
        if w["id"] < 700:
            # rain.append(1)
            willrain = True
        # else:
            # rain.append(0)

# if 1 in rain:
#     print("May be rain")
# else:
#     print("Will not rain")

if willrain:
    print("Rain is coming")
else:
    print("No rain")

test = os.environ.get("AAA")
print(test)