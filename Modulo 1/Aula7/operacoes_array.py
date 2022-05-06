import numpy as np

a1 = np.arange((50))

#exibindo intervalos especificos

print(a1)
print(a1[15]) #imprime o valor na posicao
print(a1[1:45]) #imprime o valor no intervalor
print(a1[-1]) #imprime o valor na ultima posicao
print(a1[:7]) #imprime o valor até a posicao
print(a1[7:]) #imprime o valor a partir da posicao

a1 = a1.reshape(5, 10) #rearranja para a linha e coluna desejada
print(a1)
print(a1[3, 5]) #imprime o valor na posicao linha e coluna
print(a1[0:3, 7:]) #imprime o intervalor de valores na posicao linha e coluna
print(a1[3:, 2:4])
print(a1[[2, 4]]) #imrpime somente as linhas
print(a1[:,1]) #imprime somente as colunas

print("-------------------------------")
#iterando array
print(a1)

for i in np.nditer(a1): #se for pelo for comum ele pega por linha
    print(i)

print("---------------------------")

#operacoes matematicas
a1 = np.arange(10)
print(a1)
r = a1 + 50 #serve para todas as operações + - * /
print(r)
a2 = np.ones(10)
r = a1 + a2
print(r)

print(np.add(a1, a2))
print(np.subtract(a1, a2))
print(np.multiply(a1, a2))
print(np.divide(a1, a2))

print(np.power(a1, 2)) #potencia
print(np.mod(a1, 2)) #resto de divisao

#outras operacoes

a1 = np.arange(50).reshape(5, 10)
print(a1)
print(np.amax(a1, axis=1)) #valor maximo
print(np.amin(a1, axis=1)) #valor minimo

print(np.sum(a1))  #soma de todos os valores do vetor
print(np.mean(a1)) #media do vetor
print(np.median(a1)) #mediana do vetor
print(np.percentile(a1, 25))

a2 = np.array([9, 4, 5, 1, 3, 2])
print(np.sort(a2)) #ordena o vetor
print(np.argsort(a2)) #mostra as posicoes de cada elemento ordenado na posicao original
print(np.argmax(a2)) #existe arg para as outras funcoes
