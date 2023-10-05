import requests
from datetime import datetime

# https://api.sunrise-sunset.org/json?lat=39.904202&lng=116.407394
# formatted: 0 是关闭 12小时， 显示 Unix 24 小时

MY_LAT = 39.904202
MY_LNG = 116.407394

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise, sunset)
print(time_now.hour)