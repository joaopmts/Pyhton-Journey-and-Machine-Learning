#Importar pandas e numpy
import numpy as np
import pandas as pd

#criar a serie sem indices nomeados
serie_dados = pd.Series([10, 15, 30])
print(serie_dados)

#criar uma serie com indicies nomeados com base em um array
a1 = np.array([10, 15, 30])
serie_dados = pd.Series(a1, index=np.array(["Hugo", "José", "Luiz"]))
print(serie_dados)

#criar uma serie com indices nomeados com base em uma lista
a1 = np.random.randint(0, 1000, 11)
indices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
serie_dados = pd.Series(a1, index=indices)
print(serie_dados)

#exibir o cabeçalho
print(serie_dados.head(3))

#exibir o final
print(serie_dados.tail(3))

#exibir uma linha especifica
print(serie_dados["H"])

#exibir resumo estatistico
print(serie_dados.describe())

#exibir dados estatistico separadamente
print(serie_dados.describe()["max"])
