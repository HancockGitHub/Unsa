# Escriba una funcion que calcule la media aritmetica de los elementos de una matriz de cualquier dimension mxn
import numpy as np


def media_aritmetica(matriz):
    suma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
            elementos += 1
    media = suma/elementos
    return media


while True:
    try:
        f, c = map(int, input(
            'Ingrese numero de filas y columnas separadas por un esapcio: ').split())
        break
    except ValueError:
        print('Por favor ingrese numeros enteros positivos.')

matriz = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        matriz[i][j] = float(
            input(f'Ingrese elemento ({i+1},{j+1}) de la matriz: '))
print('La matriz generada es:\n', matriz)
