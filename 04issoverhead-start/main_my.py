import requests
from datetime import datetime
import smtplib
import threading

MY_EMAIL = "xxx@gmail.com"
PASSWORD = "xxx"

MY_LAT = 39.904202  # Your latitude
MY_LONG = 116.407394  # Your longitude

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

#If the ISS is close to my current position
def iss_trace():
    if  abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        # and it is currently dark
        if time_now.hour > (sunset + 8) % 24:
            # Then send me an email to tell me to look up.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="xxx@outlook.com",
                    msg="Subject:ISS Trace\n\nLook up"
                )
    # BONUS: run the code every 60 seconds.
    timer = threading.Timer(60, iss_trace)
    timer.start()

iss_trace()





