import requests

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

querystring = {"q":"San Francisco"}

headers = {
    'x-rapidapi-key': "68405429a6msh91892f3fedade27p1b9244jsn4ea99508d46d",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)