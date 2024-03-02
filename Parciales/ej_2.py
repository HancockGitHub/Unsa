import numpy as np


def simetrica(A):
    '''obtiene la matriz simetrica de una cuadrada'''
    n, n = A.shape  # obtengo las dimensiones de la matriz ingresada
    # creo dos matrices de las mismas dimensiones que A
    T = np.empty_like(A)  # matriz traspuesta
    S = np.empty_like(A)  # matriz simetrica
    for i in range(n):
        for j in range(n):
            # asigno los elementos correspondientes a la transpuesta
            T[i, j] = A[j, i]
            # asigno los elementos correspondientes a la simetrica
            S[i, j] = (A[i, j] + T[i, j])*0.5
    return S


# script para prueba de simetrica()
# creo matriz cuadrada de enteros aleatorios
A = np.random.randint(0, 10, (3, 3))
B = simetrica(A)
print('Matriz ingresada:\n', A)
print('Matriz simetrica asociada\n', B)


def matriz_simetrica(matriz):
    # obtenemos la matriz traspuesta
    matriz_traspuesta = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(matriz[j][i])
        matriz_traspuesta.append(fila)

    # Obtenemos la matriz simetrica
    matriz_simetrica = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            # [i][j] es lo mismo que [i,j]
            fila.append(((matriz[i][j]+matriz_traspuesta[j][i]))/2)
        matriz_simetrica.append(fila)
    return matriz_simetrica
