import numpy as np
import matplotlib.pyplot as plt
import os

local = f"{os.path.dirname(__file__)}\\arquivos"

a1 = np.random.randint(2, 100, 3) #sorteia um numero entre os intervalos, o terceiro argumento é a quantidade de elementos
print(a1)

a1 = np.random.rand(1, 39)  #gera valores entre 0 e 1 aleatorios, o segundo argumento é para a quantidade podendo apos a função ser + - / * para manipular o intervalor

a1 = np.random.randn(100) #gera valores em uma distribuição normal
print(a1)

np.savetxt(f"{local}\\teste.txt", a1)
#np.loadtxt #carrega

# print(np.random.shuffle(np.arange(10)))

#plt.hist(a1)
#plt.show()
