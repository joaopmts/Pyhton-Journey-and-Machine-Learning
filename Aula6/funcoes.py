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

def infos_to_text(name, infos, dict_text=""):
    dict_text = f"{dict_text}\n{name}"
    for info, va in infos.items():
        dict_text = f"{dict_text}\n{info.upper()}"
        if tem_item(va):
            for i, item in enumerate(va):
                dict_text = f"{dict_text}\n\t{i}. {item}"
        else:
            dict_text = f"{dict_text}\n{va}"
    dict_text = f"{dict_text}\n------------------"
    return dict_text

def dict_to_text(agenda):
    dict_text = ""
    for name, infos in agenda.items():
        dict_text = f"{dict_text}\n{infos_to_text(name, infos, dict_text)}"