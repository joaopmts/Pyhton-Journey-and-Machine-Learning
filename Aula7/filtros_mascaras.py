import numpy as np

a1 = np.arange(10)
print(a1)
print(a1 < 7)

mask = a1 < 7 #gera um array booleano com base na comparacao
print(a1[mask]) #aplica a mascara como um filtro

print(a1[a1 != 5])

print(np.where(a1 > 4)) #retorna as posicoes onde os valores atendem a condição
print(np.extract(a1 > 4, a1)) #retorna os valores onde atemdem a posicao

