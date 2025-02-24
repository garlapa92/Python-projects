import requests
import os
from datetime import datetime

api_key = "Enter your api key here"
location = input("\n Enter the city name :")

complete_api_link =  ("Https://api.openweathermap.org/data/2.5/weather?q=" +location +"&appid="+api_key)

api_link = requests.get(complete_api_link)
api_data = api_link.json()

try:
    temp_city = (api_data["main"]["temp"]) - 237.15
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M: %S %P")
    
    f= open("weatherinfo.txt", "w+")
    f.write("--------------------------------\n")
    f.write("weather stats for - {}  || {}\n".format(location.upper(), date_time))
    f.write("------------------------------------------\n")

    f.write("\tCurrent temperature is : {:.2f}  \n".format(temp_city))
    f.write("\tCurrent weather desc   :  "+ weather_desc + "\n")
    f.write("\tCurrent Humidity       : {}%\n".format(hmdt))
    f.write("\tCurrent wind speed     : {} km\h \n")



