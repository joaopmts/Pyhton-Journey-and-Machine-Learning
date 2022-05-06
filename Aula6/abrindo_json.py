import os
import json

local = f"{os.path.dirname(__file__)}\\arquivos\\star_wars.json"

with open(local, encoding="UTF-8", mode="r") as arquivo:
    conteudo = arquivo.read()

male = 0
female = 0
na = 0

convertido = json.loads(conteudo)

for i in convertido:
    if i["gender"] == "male":
        male = male + 1
    if i["gender"] == "female":
        female = female + 1
    else:
        na = na + 1

print(f"Existem {male} personagens masculinos, {female} personagens feminino e {na} personagens NA")
