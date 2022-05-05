import os
import json
from funcoes import agenda_para_texto

local = f"{os.path.dirname(__file__)}\\arquivos\\star_wars2.json"

with open(local,encoding="UTF-8",mode="r") as arquivo:
    c = arquivo.read()

c2 = json.loads(c)


print(agenda_para_texto(c2))