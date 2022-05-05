import requests

connection = requests.get("https://fruityvice.com/api/fruit/all")

objeto = connection.json()

for fruta in objeto:
    print(fruta["name"])