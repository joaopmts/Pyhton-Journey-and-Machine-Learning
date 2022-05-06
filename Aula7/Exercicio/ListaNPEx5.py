#O arquivo dinheir_lanche.txt contem o valor que uma criança recebeu de seus pais em cada um dos 23 dias letivos de um mes para comprar seu lanche na escola. Crie um script que abra este aquivo e informe em quantos dias a criança recebeu R$20 dos pais

import os

import numpy as np

local = f"{os.path.dirname(os.path.dirname(__file__))}\\arquivos"

with open(f"{local}\\dinheiro_lanche.txt", encoding="UTF-8", mode="r") as arquivo:
    txt = arquivo.read().splitlines()

array = np.array(txt, dtype=np.float_)

qdias = np.count_nonzero(array == 20)
print(qdias)
