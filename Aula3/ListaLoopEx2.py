#Faça um programa que receba 100 valores digitados pelo usuario e, ao final, informe qual é o maior deles

print("Função maior numero")

x = 0
y = 0
while x < 5:
    n = int(input("Digite um numero"))
    if n > y:
        y = n
    x = x + 1

print(y)

amostra = 0

for n in range(1, 6, 1):
    x = int(input("Digite um numero"))
    if x > amostra or n == 1:
        amostra = x

print(amostra)