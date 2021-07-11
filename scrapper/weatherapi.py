import requests
import os
import datetime


city="Valencia"
units="metric"
api_key ="9a16a8e5458b6fdb0d040e46ee221bca"
language="es"

#Get icon: http://openweathermap.org/img/w/icon.png

endpoint=(f"http://api.openweathermap.org/data/2.5/weather?q={city},es&units={units}&uk&lang={language}&APPID={api_key}")
response= requests.get(endpoint)
print(response)
print(response.headers['Content-Type'])
diccionario=response.json()
print(diccionario)
try:
    temp = diccionario['main']['temp']
except KeyError:
        print("City not found")
        quit()
temp_feel=diccionario['main']['feels_like']
lon = diccionario["coord"]["lon"]
lat = diccionario["coord"]["lat"]
print(lon)
print(lat)
print(temp)
print(temp_feel)

# Save weather icon
icon_weather=diccionario['weather'][0]['icon']
file_icon=(f"http://openweathermap.org/img/w/{icon_weather}.png")
f=open('res/weathericon.png','wb')
response_icon=requests.get(file_icon)
f.write(response_icon.content)
f.close

# 7 Days Forescast
endpoint_7days=(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&exclude=hourly,minutely&appid={api_key}")
response_7days= requests.get(endpoint_7days)
print(response_7days)
print(response_7days.headers['Content-Type'])
diccionario_7days=response_7days.json()
print(diccionario_7days)

class ExceptionForecast(Exception):
    ''' Own exceptions'''
    pass
class Alerts(ExceptionForecast):
    '''There are any especial Alerts'''
    pass

# Alerts

try:
    print(diccionario_7days['alerts'])
except KeyError:
    print("No hay alertas")
    quit()

print(diccionario_7days['alerts'][0]['sender_name'])
timestamp = datetime.datetime.fromtimestamp(diccionario_7days['alerts'][0]['start'])
print(f"Starts: {timestamp.strftime('%d-%m-%Y %H:%M')}")
timestamp = datetime.datetime.fromtimestamp(diccionario_7days['alerts'][0]['end'])
print(f"Ends: {timestamp.strftime('%d-%m-%Y %H:%M')}")
print(diccionario_7days['alerts'][0]['event'])
print(diccionario_7days['alerts'][0]['description'])


