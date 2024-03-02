# Escriba una script que calcule el determinante de una matriz de 2x2.
import numpy as np
while True:
    try:
        f, c = map(int, input(
            'Ingrese la cantidad de filas y columnas seapradas por un espacio: ').split())
        if f == 2 and c == 2:
            break
        else:
            print('Error: Ingrese una matriz de 2x2')
    except ValueError:
        print('Error ingrese números eneteros positivos.')
ma = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        ma[i][j] = float(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
print('La matriz ingresada es:\n', ma)
determinante = ma[0][0]*ma[1][1] - ma[1][0]*ma[0][1]
print('El determinante de la matriz ingresada de 2x2 es:\n', determinante)

# Practica del while
while True:
    try:
        f, c = map(int, input(
            'Ingrese numeros de filas y columnas separadas popr un espcio: ').split())
        if f == c:
            break
        else:
            print('Error: La matriz no es cuadrada')
    except ValueError:
        print('Error: Ingrese numeros enteros positivos y respete las dimensiones validas')
