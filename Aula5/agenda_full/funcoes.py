def tem_items(estrutura):
    #Essa função verifica se uma determinada estrutura é uma lista ou uma tupla. É utilizada pela função "contato_para_texto()" para saber se uma determinada forma de contato possui uma série de valores ou um valor único
    if type(estrutura) == list or type(estrutura) == tuple:
        return True
    return False

def agenda_para_texto(agenda):
    agenda_texto = ""
    for nome, contatos in agenda.items():
        agenda_texto = f"{agenda_texto}\n{contato_para_texto(nome, contatos, agenda_texto)}"
    return agenda_texto

def contato_para_texto(nome, contatos, agenda_texto=""):
    #Essa função recebe o nome de um contato específico, o dicionário das formas de contato que ele possui e, de forma opcional, uma string contendo a agenda em forma de texto.
    #O objetivo dela é transformar o nome do contato e suas formas em uma string formatada. Essa função foi extraída da função "agenda para texto" original, feita em aula
    agenda_texto = f"{agenda_texto}\n{nome}"
    for contato, valor in contatos.items():
        agenda_texto = f"{agenda_texto}\n{contato.upper()}"
        if tem_items(valor):
            numero = 1
            for item in valor:
                agenda_texto = f"{agenda_texto}\n\t{numero} - {item}"
                numero = numero + 1
        else:
            agenda_texto = f"{agenda_texto}\n{valor}"
    agenda_texto = f"{agenda_texto}\n------------------"
    return agenda_texto

def localizar_contato(nome, agenda):
    #Função que recebe um nome de contato e verifica que se está na agenda. Se tiver, retorna uma string formatada com este contato.
    if nome in agenda.keys():
        return contato_para_texto(nome, agenda[nome])
    else:
        return f"O contato {nome} não foi localizado."

def excluir_contato(nome, agenda):
    #Função que excluí um contato da agenda caso ele exista
    if nome in agenda.keys():
        del agenda[nome]
        return "Contato excluído com sucesso"
    else:
        return "Não existe nenhum contato com o nome informado. A agenda não foi alterada"

def incluir_contato(agenda):
    #Função que inclui um contato a uma agenda fornecida.
    #É utilizada uma tupla (formas_disponiveis) contendo as formas de contato possíveis do sistema. Essa tupla é percorrida para solicitar ao usuário a digitação dos valores para cada uma das formas de contato.
    formas_disponiveis = ("telefones", "emails", "endereço")
    nome = input("Informe o nome da pessoa ou empresa que deseja incluir na agenda")
    contatos = {} #Este dicionário inicia vazio, e será construído com as formas de contato que o usuário digitar
    for forma in formas_disponiveis:
        print(f"Agora você incluirá registros para a seguinte forma de contato: {forma}")
        continuar = input(f"Deseja incluir um contato de {forma}: S - sim ou N - não")
        formas = [] #Esta lista é usada para que o usuário inclua vários itens em uma forma de contato
        while "S" in continuar.upper():
            formas.append(input("Informe o registro que deseja incluir: ")) #Cada novo item informado será incluido na lista
            continuar = input(f"Deseja incluir mais um registro de {forma}: S - sim ou N - não")
        if len(formas) == 1: #caso a lista tenha apenas um item, ele será incluído diretamente no dicionário
            contatos[forma] = formas[0]
        elif len(formas) > 1: #caso a lista contenha diversos itens, incluiremos a lista no dicionário
            contatos[forma] = formas
        agenda[nome] = contatos #ao final, incluiremos o dicionário de contatos como um valor na agenda, onde a chave será o nome do contato

def menu(agenda):
    op = 0
    while(op != 5):
        print("1 - Exibir todos os contatos da agenda ")
        print("2 - Incluir um contato na agenda ")
        print("3 - Localizar um contato na agenda ")
        print("4 - Excluir um contato na agenda ")
        print("5 - Sair")
        op = int(input("Indique o número da opção desejada "))
        if op == 1:
            #chamar função de exibir todos os contatos
            print(agenda_para_texto(agenda))
        elif op == 2:
            # chamar a função de incluir um único contato
            incluir_contato(agenda)
        elif op == 3:
            # chamar a função de Localizar um único contato
            nome = input("Informe o nome do contato que deseja localizar ")
            print(localizar_contato(nome, agenda))
        elif op == 4:
            # chamar a função de Excluir um único contato
            nome = input("Informe o nome do contato que deseja excluir ")
            excluir_contato(nome, agenda)
        elif op == 5:
            print("Saindo do sistema")
            exit(0)
        else:
            print("Opção inválida")
