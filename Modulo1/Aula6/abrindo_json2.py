import os
import json
from funcoes import *

local = f"{os.path.dirname(__file__)}\\arquivos\\star_wars2.json"

with open(local,encoding="UTF-8",mode="r") as arquivo:
    c = arquivo.read()

c2 = json.loads(c)

print(dict_to_text(c2))