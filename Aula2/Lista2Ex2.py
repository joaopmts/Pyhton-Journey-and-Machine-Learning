print("Calculadora de Duração do Filme")

min = int(input("Quantas horas tem o filme em minutos"))

horas = min / 60
#horas = min // 60
minutos = min % 60

print(horas)
print(minutos)
print(f"O filme tem {horas:.0f}:{minutos}")