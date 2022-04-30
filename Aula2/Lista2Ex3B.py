print("Inverter sem 3a variavel")

a = int(input("Digite um numero:\n"))
b = int(input("Digite um segundo numero:\n"))

print(f"A {a}")
print(f"B {b}")

b = b + a
a = b - a
b = b - a

#a,b = b,a

print(f"A {a}")
print(f"B {b}")