print("Calculadora de pontuação")

segundograu = 1
graduacao = 2
posgraduacao = 3

nome = input("Qual o seu nome?")
titulacao = int(input("Qual a sua titulação?\n1 - Segundo Grau\n2 - Graduação\n3 - Pós Graduação"))
idade = int(input("Quantos anos de experiencia voce possui?"))
experiencia = int(input("Quantos anos você tem?"))

pontos = 0

if titulacao == 1:
    pontos = pontos + 50
elif titulacao == 2:
    if idade <= 4:
        pontos = pontos + 70
    else:
        pontos = pontos + 90
elif titulacao == 3:
    if idade <= 4:
        pontos = pontos + 100
    elif idade <=6 and idade > 4:
        pontos = pontos + 120
    else:
        pontos = pontos +150

if experiencia < 40:
    pontos = pontos + 100
else:
    pontos = pontos - 50

print(f"Sua pontuacao final é {pontos}")