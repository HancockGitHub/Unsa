# Modifique la funcion programada en el punto 1 para que devuelva la suma de todos los elementos de cualquier matriz de dimension nxm


# # usando la funcion enumerate


# def suma_matriz(matriz):
#     for i, fila in enumerate(matriz):
#         for j, valor in enumerate(fila):
#             suma += valor
#     return suma

# Practica
import numpy as np


def sum_elementos_matriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
    return suma


while True:
    try:
        f, c = map(int, input(
            'Ingrese numero de filas y columnas por separado: ').split())
        break
    except ValueError:
        print('Por favor ingrese numeros naturales es para el tamaño de una matriz no sea pendejo')

matr = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        matr[i, j] = float(
            input(f'Ingrese elemento ({i+1},{j+1}) de la matriz: '))
print('La matriz ingresada es:\n', matr)
print('La suma de todos los elementos de la matriz es:\n',
      sum_elementos_matriz(matr))

# Practica2
while True:
    try:
        f, c = map(int, input(
            'Ingrese numeros de fila y columna separados por un espacio: ').split())
        break
    except ValueError:
        print('Por favor ingrese solo numeros enteros positivos')

ma = np.zeros((f, c))
for i in range(f):
    for i in range(j):
        ma[i, j] = float(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
print(ma)

while True:
    try:
        f, c = map(int, input(
            'Ingrese numeros de filas y columnas separados por un espacio: ').split())
        break
    except ValueError:
        print('numeros enteros positivos plis')

ma = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        ma[i, j] = float(
            input(f'Ingrese el elemento ({i+1},{j+1} de la matriz: ) '))
print(ma)
