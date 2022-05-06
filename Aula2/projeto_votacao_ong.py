#Uma ONG resolveu prestar um serviço bem diferente: ela oferece vans para buscar pessoas com qualquer tipo de dificuldade de locomoção para poderem votar.
#Para evitar problemas no momento do embarque, porém, você foi convidado a criar um programa que valide a idade dos passageiros: caso tenham 16 anos ou menos, não podem votar (e nem embarcar). Caso tenham entre 16 anos e 18 incompletos, podem optar por votar ou não. Caso tenham mais de 18 anos, devem votar obrigatoriamente.


idade = int(input("Digite sua idade:\n"))

if idade >= 18:
    print("Você é obrigado a votar")
elif idade >= 16:
    print("Você pode votar mas não é obrigado")
else:
    print("Você não pode votar")