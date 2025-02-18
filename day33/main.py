import requests
import datetime

parameters = {
    "lat" : -32.888355,
    "lng" : -68.838844,
    "formatted" : 0
}

response_weather = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response_weather.json()["results"]

response_iss = requests

time_now = datetime.datetime.now().hour

sunset = (data["sunset"]
.split(sep="T")
[1].split(":")[0])

sunrise = (data["sunrise"]
          .split(sep="T")
          [1].split(":")[0])

# if  sunset <= time_now <= sunrise:



