print("Calculadora de calorias")

total_calorias = 0

for refeicao in ["Café da manhã", "Almoço", "Jantar"]:
    calorias = int(input(f"Digite a quantidade de calorias que voce ingeriu {refeicao}"))
    total_calorias = total_calorias + calorias

media_calorias = total_calorias / 3

print(f"Ao longo do dia voce consumiu um total de {total_calorias}. Com uma média de {media_calorias} por refeição")