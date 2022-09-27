from datetime import datetime
import requests
MY_LAT = 48.135124
MY_LNG = 11.581981
# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# print(response)
parameters ={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}

response = requests.get(url= "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
#print(sunrise.split("T")[1].split(":")[0])
print(sunset)
#print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)