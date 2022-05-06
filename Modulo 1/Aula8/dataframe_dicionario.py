#importar pandas e numpy
import pandas as pd
import numpy as np

#criar um dataframde de dicionario para representar o desempenho dos genrentes em uma gincana rotativa, onde cada dia um gerente diferente fica repsonsavel pela loja:

#As colunas devem ser gerente (nomes dos 4 gerentes), avaliacao(array aleatorio de numeros inteiros entre 1 e 10), faturamento(array com valores 350.99, 350.99, 480.80, 450.24) quanidade vendida (array com os valores 12, 5, 6, 9) e categoria com os valores veterano, novato, novato e veterano.

dicionario = {
    "GERENTE": np.array(["Jaspion", "Goku", "Snarf", "Rick"]),
    "AVALIACAO": np.random.randint(1, 11, 4),
    "FATURAMENTO": np.array([350.99, 350.99, 480.80, 450.24]),
    "QUANTIDADE VENDIDA": np.array([12, 5, 6, 9]),
    "CATEGORIA": pd.Categorical(["Veterano", "Novato", "Novato", "Veterano"])
}

#os indicies devem ser 4 datas
indice = pd.date_range("20220505", periods=4)

data_frame = pd.DataFrame(dicionario, index=indice)

#exibir dataframe completo
print(data_frame)

#filtrar por quantidade vendida > 6
print(data_frame[data_frame["QUANTIDADE VENDIDA"] > 6])

#exibir os dados da coluna QUANTIDADE VENDIDA ordenados em ordem decrescente
print(data_frame.sort_values(by="QUANTIDADE VENDIDA", ascending=False))
print(data_frame[["GERENTE", "AVALIACAO"]].sort_values(by="AVALIACAO", ascending=False))
print(data_frame["AVALIACAO"].describe())

#exibir os dados do dia 05-05-2022
print(data_frame.loc["2022-05-05"])

#exibir os dados no intervalo de datas
print(data_frame.loc["2022-05-05":"2022-05-07"])

#exibir apenas os gerentes veteranos
print(data_frame[data_frame["CATEGORIA"].isin(["Veterano", "Novato"])])

#exibir o faturamento de apenas um data
print(data_frame.loc["2022-05-05"]["FATURAMENTO"])