from funcoes import menu
agenda_fora = {
    "Darth Vader":{
        "emails":"darth@vader.com",
        "telefones": ("11 1234 5678", "11 98765-4321")
    },
    "Luke Skywalker":{
        "emails": ["luke@skywalker.com", "pilot001@rebelalliance.com"],
        "telefones": "21 6543-1234",
        "endereço": "Lars Farm - Tatooine"
    },
    "Mestre Yoda":{
        "emails": ["thegreen@yoda.com", "master@temple.com"],
        "telefones": "31 7894-1234",
        "endereço": "Old Swamp - Dagobah"
    },
    "Imperador Palpatine":{
        "emails": "thebest@darkside.com.br"
    }
}


menu(agenda_fora)