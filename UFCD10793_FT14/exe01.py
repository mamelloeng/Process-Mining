import numpy as np
obj = np.array([1,2,3])
matrix = np.array([[1,2,3],[4,5,6]])

print(obj)
print("\n")
print(matrix)

print("Número de dimensões do vetor obj: ",obj.ndim)
print("Número de dimensões da matrix matrix: ",matrix.ndim)

print("Tamanho do vetor obj: ",obj.size)
print("Tamanho da matrix matrix: ",matrix.size)

print("Forma do vetor obj: ",obj.shape)
print("Forma da matrix matrix: ",matrix.shape)

print("Tipo do vetor obj: ",type(obj))
print("Tipo da matrix matrix: ",type(matrix))

print(np.ones((10,2)))
print(np.zeros((5,4)))

obj1 = np.arange(0,101,3)
print(obj1)
