#importar pandas e numpy
import pandas as pd
import numpy as np

#criar um indice de datas e um array aleatorio de 6,4
indice_datas = pd.date_range("20220505", periods=6, freq="D")
a1 = np.array(np.random.randint(1, 1000, 24)).reshape(6, 4)

#criar um dataframe com base no array para os valores, as datas com indices e uma lista de letras como colunas
data_frame = pd.DataFrame(a1, index=indice_datas)
print(data_frame)
print(data_frame.describe())