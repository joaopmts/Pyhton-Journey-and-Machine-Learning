dicionario = {
    "nome" : "Joao",
    "altura" : 1.73,
    "nascimento" : 1999
}

#exibindo
print(dicionario["nome"]) #Imprime o valor da chave no dicionario
print(dicionario.get("Estado Civil"))
print(dicionario)

#inserindo
dicionario["Estado Civil"] = "Solteiro"
print(dicionario.get("Estado Civil")) #Pega o valor da chave no dicionario
print(dicionario.setdefault("peso", 88))
print(dicionario)
print(dicionario.setdefault("nome", "Maria")) #Mostra o valor a chave no dicioanario, se este valor for vazio. Ele já coloca o novo valor
print(dicionario)

#operacoes
print(dicionario.values()) #Imprime apenas os valores sem chaves
print(dicionario.keys()) #Imprime apenas as chaves sem os valores
print(dicionario.items()) #Imprime o conjunto chave e valor

for chave, valor in dicionario.items():
    print(f"{chave} ----- {valor}")

#removendo]
dicionario.pop("peso") #remove a chave desejada
print(dicionario)
dicionario.popitem() #remove a ultima chave
print(dicionario)
dicionario.clear()
print(dicionario) #limpa o dicionario

