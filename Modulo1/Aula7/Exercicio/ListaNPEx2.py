#Utilizando o array gerado anteriormente, cria um novo array que não contenha os anos de 1942 e 1946, em que as copas nao foram realizadas em decorrencia da segunda guerra mundial.

import numpy as np


array = np.arange(1930,2019, 4)

mask = (array != 1942) & (array != 1946)
#mask = np.logical_and(array != 1942, array != 1946)

print(array[mask])


