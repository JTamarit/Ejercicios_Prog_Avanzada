import requests

api_key ="9a16a8e5458b6fdb0d040e46ee221bca"

endpoint=(f"https://api.openweathermap.org/data/2.5/onecall?lat=39.3333&lon=-0.8333&units=metric&exclude=hourly,minutely&appid={api_key}")

response= requests.get(endpoint)

print(response)
print(response.headers['Content-Type'])
diccionario=response.json()
print(diccionario)