import requests
import os

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
temp = diccionario['main']['temp']
temp_feel=diccionario['main']['feels_like']
print(temp)
print(temp_feel)
icon_weather=diccionario['weather'][0]['icon']
file_icon=(f"http://openweathermap.org/img/w/{icon_weather}.png")
f=open('res/weathericon.png','wb')
response_icon=requests.get(file_icon)
f.write(response_icon.content)
f.close
