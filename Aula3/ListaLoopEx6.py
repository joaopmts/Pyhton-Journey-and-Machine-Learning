n = int(input("Digite a quantidade de numeros para a sequencia"))
q = n

for x in range (1, n + 1, 1):
    num = 1
    den = 1
    for y in range (1, x + 1, 1):
        num = num * y
    for z in range (q, 1, -1):
        den = den * z
    print(f"{num}/{den}")
    q = q -1
