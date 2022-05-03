opcao = 0

while opcao != 4:
    print("1 - Receber elogio pessoal")
    print("2 - Receber elogio profissional")
    print("3 - Receber um elogio fisico")
    print("4 - Sair")
    opcao = int(input("Digite uma opção:"))

    if opcao == 1:
        print("Você é muito firmeza")
    if opcao == 2:
        print("Seus codigos sao bem estruturados")
    if opcao == 3:
        print("Os seus ossos tem uma otima densidade")
    if opcao == 4:
        print("Sair")
    else:
        print("Opcao invalida")