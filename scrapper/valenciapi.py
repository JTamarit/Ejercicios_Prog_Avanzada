import requests

endpoint1="http://apigobiernoabiertortod.valencia.es/rest/datasets/estado_parkings.json"
endpoint2="http://apigobiernoabiertortod.valencia.es/rest/datasets/estado_parkings/1.json"
lista_endpoints=[endpoint1,endpoint2]

for endpoint in lista_endpoints:

    response = requests.get(endpoint)
    print(response)
    print(response.headers['Content-Type'])
    diccionario=response.json()
    print(diccionario)
    