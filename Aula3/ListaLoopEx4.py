#Um professor quer saber quantos alunos de uma sala de 50 tiveram nota maior do que a media. Faça um programa onde o professor informe a media e as notas de cada um dos 50 alunos e, ao final, seja exibido quantos alunos tiveram ntoa superior a media e quantos tiveram nota inferior a media.

malunos = int(input("Digite a media dos alunos"))
qalunos = int(input("Digite a quantidade de alunos"))
c = 0
for n in range(0, qalunos, 1):
    nota = int(input(f"Digite a nota do aluno {n}:"))
    if nota >= malunos:
        c = c + 1


b = qalunos - c

print(f"A quantidade de alunos que tiveram nota acima de média foi {c} e a quantidade de alunos que tiveram nota abaixo da media foi de {b}")