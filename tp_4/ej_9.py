# Escriba un script que transponga una matriz. Compare el resultado con el metodo transpose.


import numpy as np


matriz = [[1, 2], [3, 4], [5, 6]]
matriz_traspuesta = []

# con este for recorro los indices de las columnas de la matriz original
for i in range(len(matriz[0])):
    # con len(matriz[0]) obtengo el numero de columnas
    fila = []
    # con el segundo for recorro los indices de las filas de la matriz original
    for j in range(len(matriz)):
        # len(matriz) obtengo el numero de filas
        fila.append(matriz[j][i])
    matriz_traspuesta.append(fila)

print(matriz_traspuesta)


# usando numpy

matriz = np.array([[1, 2], [3, 4], [5, 6]])
print(matriz.transpose())
