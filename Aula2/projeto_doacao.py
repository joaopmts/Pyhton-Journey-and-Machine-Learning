#O estatuto de uma ONG determina que todas as doações recebidas devem gerar um valor para investimento, para cobrir momentos de necessidade.
#O valor do investimento deve ser de 5% da doação. Porém, em casos em que as doações ultrapassem R$1000,00 o investimento deve ser de 15% da doação.
#Sua missão é criar um programa capaz de fazer os cálculos necessários e indicar quanto deve ser investido.


doacao = float(input("Digite o valor da doação:\n"))

if doacao >= 1000:
    investimento = doacao * 0.15
else:
    investimento = doacao * 0.05

uso_imediato = doacao - investimento

print(f"A doação foi de {doacao}, o investimento foi de {investimento} e o valor para uso imediato foi de {uso_imediato}")