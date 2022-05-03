lista = ["Wolverine", "Cyclops", "Professor"]

#exibicao
print(lista) #Imprime toda a lista
print(lista[-1]) #Imprime de tras para frente
print(lista[0:2]) #Imprime o intervalo da lista
for xmen in lista:
    print(xmen)

#inserindo
lista.append("Fera") #Adiciona na ultima posicao
print(lista)
lista.insert(0, "Vampira") #Adiciona na posicao desejada
print(lista)
lista[1] = "Jubileu" #Faz a substituicao na posicao desejada
print(lista)

#Operacoes bacanas
print(lista.index("Jubileu")) #Mostra a posicao da palavra na lista
lista.append("Cyclops")
print(lista)
print(lista.count("Cyclops")) #Conta quantas vezes se repete na lista
print(len(lista)) #Conta a quantidade de elementos da lista
lista.reverse() #Inverte a lista
print(lista)
lista.sort() #Faz a lista aleatoriamente
print(lista)

#Removendo
lista.pop() #Tira o ultimo item da lista
print(lista)
lista.pop(1) #Tira o item da lista na posicao desejada
print(lista)
del lista[1:3] #Deleta um intervalo da lista
print(lista)
lita.clear() #Deleta a lista
print(lista)
