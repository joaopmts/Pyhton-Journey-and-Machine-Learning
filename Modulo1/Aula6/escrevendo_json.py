import os
import json
local = f"{os.path.dirname(__file__)}\\arquivos\\ficha.json"

dicionario = {
    "Nome":"Joao",
    "Peso":"80",
    "Altura":"1.73"
}

json_final = json.dumps(dicionario, indent=4, ensure_ascii=False)

with open(local, encoding="UTF-8", mode="w") as arquivo:
    arquivo.write(json_final)
