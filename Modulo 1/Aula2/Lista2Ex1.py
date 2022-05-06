from datetime import datetime

ano = int(input("Informe seu ano de nascimento:\n"))
ano_atual = datetime.now().year

idade = ano_atual - ano

print(f"Ao final do ano você tera:{idade}")