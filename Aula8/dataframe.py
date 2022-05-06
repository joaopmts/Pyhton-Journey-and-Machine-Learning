#import pandas, numpy e matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

local = f"{os.path.dirname(__file__)}\\arquivos"

#importar arquivo Pokemon.csv, usando colunas Name, Type 1, HP e Attack e os nomes dos pokemons como indices
data_frame = pd.read_csv(f"{local}\\Pokemon.csv",usecols=["Name", "Type 1", "HP", "Attack"], index_col=["Name"])
print(data_frame)

#exibir quantos pokemons possuem valores de vida que nenhum outro tenha
#exibir quais os valores
print(f"Existem {data_frame['HP'].nunique()}")
print(f"Existem os sequintes valores unicos de vida {data_frame['HP'].unique()}")

#resumo estatistico
print(f"{data_frame.describe(include='all')}\n")
print(data_frame["Type 1"].describe())

#exibir a lista de pokemons que seja de um tipo informado pelo usuario
tipos = []
continuar = ""

while "N" not in continuar.upper():
    tipo = input("Informe o tipo de pokemon que deseja visualizar")
    tipos.append(tipo)
    print(data_frame[data_frame["Type 1"].isin([tipo])])
    continuar = input("Voce deseja continuar? SIM OU NAO")

#plotar um grafico com a distribuicao de tipos de pokemon
histograma = data_frame["Type 1"].hist()
plt.show()

#gravar a imagem do grafico
arquivo = histograma.get_figure()
arquivo.savefig(f"{local}\\pokemons.jpg")

#exibir o pokemon mais comum da lista
print(data_frame["Type 1"].describe().top)

#exibir os dados em formato json
print(data_frame.to_json())

#exibir o dataframe para csv e html
print(data_frame.to_csv(f"{local}\\dataframe.csv"))
print(data_frame.to_html(f"{local}\\dataframe.html"))