#Para representar os tempos de 16 corredores de uma competição, crie um array formado por numeros aleatorios do tipo float (com casas decimais) que variem entre 0 e 11

import numpy as np

array = np.random.uniform(0,11,[1,16])

#array = np.random.randint(0,11,16) + np.random.random(16)

print(array)