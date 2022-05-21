print("Calculadora de Consumo Médio")

distancia = float(input("Qual foi a distancia percorrida em KM:\n"))
combustivel = float(input("Qual foi a quantidade de combustivel gasto em L:\n"))
eficiencia = distancia / combustivel

print(f"A eficiencia do carro foi:{eficiencia} KM/L")