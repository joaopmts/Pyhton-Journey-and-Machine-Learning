def tem_item(estrutura):
    if type(estrutura) == list or type(estrutura) == tuple:
        return True
    return False

def agenda_para_texto(agenda):
    agenda_texto = ""
    for nome, contatos in agenda.items():
        agenda_texto = f"{agenda_texto}\n{nome}"
        for contato, valor in contatos.items():
            agenda_texto = f"{agenda_texto}\n{contato.upper()}"
            if tem_item(valor):
                for i, item in enumerate(valor):
                    agenda_texto = f"{agenda_texto}\n\t{i}. {item}"
            else:
                agenda_texto = f"{agenda_texto}\n------------------"
    return agenda_texto