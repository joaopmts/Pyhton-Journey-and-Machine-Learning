print("Calcuadora Conta de Luz")

casa = 1
comercio = 2
industria = 3

valorcasa = 0.6
valorcomercio = 0.48
valorindustria = 1.29

tipo = int(input("Qual é o seu tipo de local:\n1 - Casa\n2 - Comercio\n3 - Industria\n"))
quantidade = float(input("Quantos KW/h você consumiu nos ultimos 30 dias?\n"))

if tipo == 1:
    valorfinal = quantidade * valorcasa
    print(valorfinal)
elif tipo == 2:
    valorfinal = quantidade * valorcomercio
    print(valorfinal)
elif tipo == 3:
    valorfinal = quantidade * valorindustria
    print(valorfinal)
else:
    print("Você digitou um tipo errado")