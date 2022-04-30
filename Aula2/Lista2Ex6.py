print("Calculadora de desconto")

valor = int(input("Digite o valor da compra"))
cupom = input("Digite o cupom de desconto")

if cupom.upper() == "DIADEFESTA":
    valor = valor * 0.97
else:
    valor = valor

print(f"O valor final é de {valor}")