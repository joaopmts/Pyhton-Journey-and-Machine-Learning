#Uma ONG criou um jogo para alertar as pessoas sobre os riscos das drogas.
#Por se tratar de um assunto sensível, ficou decidido que a idade mínima para jogar é de 12 anos.
#Sua função é criar um programa que receba a idade do usuário e exiba a mensagem "Você pode jogar" caso ele tenha 12 anos ou mais.

idade = int(input("Digite sua idade:\n"))

if idade >= 12:
    print("Você está apto a jogar")
else:
    print("Você não pode jogar")