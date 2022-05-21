agenda = {
    "Darth Vader":{
        "email":"darth@vader.com",
        "telefone":"11 97564 6666"
    }
}

nome_contato = input("Digite o nome do novo contato")
email = input("Digite o email do novo contado")
telefone = input("Digite o telefone do novo contado")

agenda[nome_contato] = {
    "email":email,
    "telefone":telefone
}

print(agenda.items())

buscando = input("Informe o nome do contado que voce deseja visualizar")
if buscando in agenda.keys():
    for chave, valor in agenda[buscando].items():
        print(f"{chave} ----- {valor}")
else:
    print("O contado nao existe na agenda")