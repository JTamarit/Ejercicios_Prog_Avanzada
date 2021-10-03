import requests

API_KEY = '4lwpSch1dj1Dxc4p6ZRzHNnBbQAcK8rD'

def download_gifs(endpoint, params):
    response = requests.get(endpoint, params=params).json()
    for i, gif in enumerate(response["data"]):
        title = gif["title"]
        url = gif["images"]["original"]["url"]

        print(title)

        with open(f"gif_{i}.gif", "wb") as f:
            f.write(requests.get(url).content)

trending_endpoint = 'https://api.giphy.com/v1/gifs/trending'
params = {
    "api_key" : API_KEY,
    "limit" : 5,
    "rating" : "g"
}

download_gifs(trending_endpoint, params)

search_endpoint = 'https://api.giphy.com/v1/gifs/search'
search = "morata"
params = {
    "api_key" : API_KEY,
    "limit" : 5,
    "rating" : "r",
    "q" : search
}

download_gifs(search_endpoint, params)