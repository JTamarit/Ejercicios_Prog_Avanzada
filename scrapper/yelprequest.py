import requests
endpoint="https://api.yelp.com/v3/businesses/search"
response= requests.get(endpoint)
print(response)
print(response.headers['Content-Type'])
diccionario=response.json()
print(diccionario)