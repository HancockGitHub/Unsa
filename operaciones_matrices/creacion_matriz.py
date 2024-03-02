import numpy as np

# Usando zeros()

f = int(input('Ingrese la cantidad de filas: '))
c = int(input('Ingrese la cantidad de columnas: '))
M = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        M[i, j] = float(input(f'ingrese el elemento ({i+1},{j+1}): '))
print('El array ingresado es:\n', M)


# Usando empty()

f = int(input('Ingrese la cantidad de filas: '))
c = int(input('Ingrese la cantidad de columnas: '))
M = np.empty((f, c))
for i in range(f):
    for j in range(c):
        M[i, j] = float(input(f'Ingrese el elemento ({i},{j}): '))
print('La matriz generada es:\n', M)


# Creacion de una matriz sin utilizar librerias

fil = int(input('Ingrese numero de filas: '))
col = int(input('Ingrese numero de columnas: '))
ma = []
for i in range(fil):
    fila = []
    for j in range(col):
        elemento = (int(input(f'Ingrese el elemento ({i+1},{j+1}): ')))
        fila.append(elemento)
    ma.append(fila)
print('La matriz generada es:\n', ma)

while True:
    try:
        f, c = map(int, input(
            'Ingrese numeros de filas y columnas separadas por un espacio: ').split())
        break
    except ValueError:
        print('Error: Las dimensiones deben ser enteras positivas')
M = np.empty((f, c))
for i in range(f):
    for i in range(c):
        M[i][j] = int(
            input(f'Ingrese ele elemento ({i+1},{j+1}) de la matriz: '))
print(M)
