from time import sleep

texto = "Há muito tempo atras, numa galaxia muito, muito distante"

for letra in texto:
    print(letra, end="", flush=True)
    sleep(0.1)