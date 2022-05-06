from varias_funcoes.funcoes import agenda_para_texto

agenda = {
    "Darth Vader" : {
        "email" : "darth@vader.com",
        "telefone" : ("11 97894 5612", "11 6566 4455")
    },
    "Luke Skywalker" : {
        "email" : ["luke@skywalker.com", "piloto001@rebelliance.com"],
        "telefone" : "11 4656 4294",
        "endereço" : "Lars Farm - Tattoine"
    },
    "Imperador Palpatine" : {
        "email" : "thebest@darkside.com.br"
    },
    "Mestre Yoda" : {
        "email" : ["thegreen@yoda.com", "master@temple.com"],
        "telefone" : "31 44444 5555",
        "endereço" : "Old Swamp - Dagobah"
    }
}

for nome, contatos in agenda.items():
    print(f"{nome}")
    for contatos, valor in contatos.items():
        if type(valor) == list or type(valor) == tuple:
            for i, item in enumerate(valor, start=1):
                print(f"{i}. {item}")
        else:
            print(f"{valor}")
    print("----------------------------")

print(agenda_para_texto(agenda))