#arquivo = open("C:\\Users\\JOAO NOTE WORK\\Documents\\GitHub\\Pyhton-Journey-and-Machine-Learning\\Aula6\\arquivos\\teste.txt", encoding="UTF-8", mode="a")

#arquivo.write("\nBoa noite pessoal\n")
#arquivo.write("O que sera que acontece\n")

#arquivo.close()

import os

local = f"{os.path.dirname(__file__)}\\arquivos\\teste.txt"
print(local)

with open("C:\\Users\\JOAO NOTE WORK\\Documents\\GitHub\\Pyhton-Journey-and-Machine-Learning\\Aula6\\arquivos\\teste.txt", encoding="UTF-8", mode="a") as arquivo:
    arquivo.write("sera que funcionou")

