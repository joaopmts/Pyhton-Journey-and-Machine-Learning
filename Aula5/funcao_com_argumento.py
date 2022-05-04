def somar(v1, v2):
    r = v1 + v2
    print(r)

def saudacao(periodo="manha", elogio=False):
    print(f"É muito legal estar nesta {periodo}")
    if elogio:
        print("Você é muito legal")

def somar_diversos(mensagem=False, *valores):
    resultado = 0
    for valor in valores:
        resultado = resultado + valor
    if mensagem:
        print(f"A soma dos valores foi de {resultado}")
    else:
        print(resultado)

def mostrar_ficha(**ficha):
    print(ficha)
    for chave, valor in ficha.items():
        print(f"{chave} -------- {valor}")

mostrar_ficha(nome="André", peso=88, altura=1.65)