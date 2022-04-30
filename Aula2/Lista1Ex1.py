print("Calculadora de Consumo Médio")

distancia = float(input("Qual foi a distancia percorrida em KM "))
combustivel = float(input("Qual foi a quantidade de combustivel gasto em L "))
eficiencia = distancia / combustivel

print(f"A eficiencia do carro foi:{eficiencia} KM/L")