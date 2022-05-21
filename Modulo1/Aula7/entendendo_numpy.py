import numpy as np
#criando vetor
novo_array = np.array([1, 2, 3, 7], dtype=np.float_) #np.bool_ para valor booleanos 0 = False

print(type(novo_array))
print(novo_array)

array_bidimensional = np.array([[1., 2 ,3], [3, 2, 1], [1, 5, 7]]) #Estrutura homogenea, só dados do mesmo tipo
print(array_bidimensional)

#gerando vetor
novo_array = np.arange(1, 50, 3) #gera array com valores igualmente espacados com base no vinicial, vfinal e step
print(novo_array)

novo_array = np.arange(50) #gera array com valores igualmente espacado com step 1
print(novo_array)

novo_array = np.linspace(1, 50, 5) #gera numero de elementes igualmente espacados no interfalo fornecido
print(novo_array)

novo_array = np.ones(50) #gera vetor com valores um na quantidade desejada
print(novo_array)

array_bidimensional = np.ones((5, 3, 2)) #z, y, z
print(array_bidimensional)

novo_array = np.zeros(50) #gera vetor com valores zeros na quantidade desejada
print(novo_array)

array_bidimensional = np.empty([5, 3]) #faz um vetor com a "sujeira" da memoria ram
print(array_bidimensional)

array_bidimensional = np.full((5, 3), 4) #gera um array customizado
print(array_bidimensional)

matriz_identidade = np.eye(5) #gera uma matriz identidade quadrada
print(matriz_identidade)

#trabalhando com dimensoes

print(array_bidimensional.flatten()) #mostra como um vetor unidimensional

print(array_bidimensional.ravel("F")) #cria um array unidimensional com bae nas colunas

array_bidimensional = np.array([[6, 5, 4], [7, 8, 9]])
print(array_bidimensional)
print(np.transpose(array_bidimensional)) #inverte linhas em colunas e vice versa
print(array_bidimensional.T) #inverte linhas em colunas e vice versa

array1 = np.array([1, 2, 3])
array2 = np.array([5, 6 ,7])
array3 = np.concatenate((array1, array2)) #faz um array se juntar
print(array3)

print(np.hstack((array1, array2))) #empilha horizontalmente os arrays
print(np.vstack((array1, array2))) #empilha verticalmente os arrays

novo_array = np.arange(10)
print(novo_array)
print(novo_array.reshape(2, 5))