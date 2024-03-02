# Escriba una funcion que realice el producto entre dos matrices. La salida de la
# misma debe ser este producto.
import numpy as np
while True:
    try:
        f, c = map(int, input(
            'Ingrese la cantidad de filas y columnas para una matriz cuadrada: ').split())
        if f == c:
            break
        else:
            print('Error: La matriz no es cuadrada.')
    except ValueError:
        print('Error: Ingrese las dimensiones validas y enteros positivos.')

ma = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        ma[i][j] = int(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
print('La matriz ingresada es:\n', ma)
