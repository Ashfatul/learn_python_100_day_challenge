import requests, time, smtplib
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = "dbb0227b750917"
my_pass = "f422092661e498"

def checkISSPosition():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    ISS_NEAR = False
    DARK = False

    if iss_longitude - MY_LONG > 5 or iss_longitude + MY_LONG < -5:
        ISS_NEAR = False
    else:
        ISS_NEAR = True

    if time_now.hour < sunrise or time_now.hour > sunset:
        DARK = True

    if ISS_NEAR & DARK:
        print("ISS is close to your area and it is dark")
        with smtplib.SMTP("smtp.mailtrap.io", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(
                from_addr="ashfatul.islam@gmail.com",
                to_addrs="ashfatul.islam@gmail.com",
                msg=f"Subject: ISS is close to your area\n\n ISS is close to your area and it is dark go to open place to see\nhave a nice day"
            )
    else:
        print("ISS is not close to your area or it is not dark")



Watching = True

while Watching:
    print("Checking for ISS position...")
    checkISSPosition()
    print("Waiting 60s before retrying...")
    time.sleep(60)
