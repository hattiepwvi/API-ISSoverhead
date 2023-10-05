import requests

# requests package: get method => response code(200, 404) =>response.json() 像字典
   # response.status_code => response.raise_for_status()自动反馈不同的exception
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)