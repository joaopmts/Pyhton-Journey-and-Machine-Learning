arquivo = open("C:\\Users\\JOAO NOTE WORK\\Documents\\GitHub\\Pyhton-Journey-and-Machine-Learning\\Aula6\\arquivos\\trecho.txt", encoding="UTF-8")

# print(type(arquivo))
# print(arquivo) Mostra o caminho

# conteudo = arquivo.read() Le o conteudo completo
# conteudo = arquivo.readline() Le uma linha do arquivo
# conteudo = arquivo.readlines() Le o arquivo e a cada linha é uma lista e inclui o \n
conteudo = arquivo.read().splitlines() #Le o arquivo e cada linha é uma lista e nao inlcui o \n
arquivo.close()

#for linha in conteudo:
#    print(linha.replace("\n", ""))

for linha in conteudo:
    if "meu" in linha:
        conteudo.pop(conteudo.index[linha])



print(conteudo)
# print(type(conteudo))

