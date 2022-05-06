print("Selecionador de lixo mais leve")

peso1 = int(input("Digite um peso:\n"))
peso2 = int(input("Digite um peso:\n"))
peso3 = int(input("Digite um peso:\n"))

if peso1 < peso2 and peso1 < peso3:
    print("O peso 1 deve ser carregado")
elif peso2 < peso1 and peso2 < peso3:
    print("O peso 2 deve ser carregado")
else:
    print("O peso 3 deve ser carregado")

