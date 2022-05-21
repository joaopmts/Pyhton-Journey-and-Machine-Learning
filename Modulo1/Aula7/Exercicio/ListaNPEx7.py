import os
import numpy as np

local = f"{os.path.dirname(os.path.dirname(__file__))}\\arquivos"

print(local)

with open(f"{local}\\funcionarios_projeto.txt", encoding="UTF-8", mode="r") as fp:
    funcp = fp.read().splitlines()

with open(f"{local}\\funcionarios_treinamento.txt", encoding="UTF-8", mode="r") as ft:
    funct = ft.read().splitlines()

fparray = np.array(funcp)
ftarray = np.array(funct)

lista1 = np.intersect1d(fparray, ftarray, assume_unique=False, return_indices=False)
lista2 = np.setxor1d(lista1, ftarray)


print(lista1)
print(lista2)