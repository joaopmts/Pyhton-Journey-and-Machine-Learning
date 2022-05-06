import os

local = f"{os.path.dirname(__file__)}\\arquivos\\lista_usuarios.csv"

with open(local,encoding="UTF-8",mode="r") as arquivo:
    conteudo = arquivo.read().splitlines()

print(conteudo)

dicionario = {}

for item in conteudo:
    dados_linha = item.split(";")
    print(dados_linha)
    if len(dados_linha) > 1 and conteudo.index(item) > 0:
        dicionario[dados_linha[0]] = {
            "Identifier":dados_linha[1],
            "First Name":dados_linha[2],
            "Last Name":dados_linha[3]
    }

username = input("Informe o nome do usuario para obter dados")

dados = dicionario.get(username)

print(f"{dados.get('First Name')} {dados.get('Last Name')}")

print(dicionario)