# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:44:09 2020

@author: jadta
"""

key = 'c2a7ba0de3afc0bcd21e6a0df7e2b05d'

import pandas
import requests

df = pandas.read_csv('airport-codes.csv')
airport = input("Please enter an airport code: ")
found = 0
for i in range(df['ident'].shape[0]):
    if airport == df['ident'][i]:
        found = 1
        location = df['coordinates'][i].replace(" ", "").split(",")
        lat = location[0]
        lon = location[1]
        airport = df['name'][i]
    
if found == 0:
    print("Airport not found. Please try again later.")
else:
    print("{} found!".format(airport))
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid={}".format(lat,lon,key))
    if response.status_code != 200:
        print("Unable to connect to OpenWeatherMaps. Please try again later.")
    else:
        print("Connected to OpenWeatherMaps!\n")
        weather_data = response.json()
        print("The current forecast is {}.".format(weather_data['weather'][0]['main']))
        print("The current temperature is {}°F.".format(weather_data['main']['temp']))
        print("The wind is currently blowing at {} mph.".format(weather_data['wind']['speed']))
        
        
    