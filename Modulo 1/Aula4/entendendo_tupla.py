tupla = (150, 900)

#exibir
print(tupla)
print(tupla[0])
for valor in tupla:
    print(valor)

#operacoes
print(tupla.index(900)) #Imprime a posicao do valor
print(tupla.count(900)) #Imprime a quantidade de vezes que o valor esta na tupla

#desempacotando valores

x, y = tupla
print(f"X={x}, Y={y}")