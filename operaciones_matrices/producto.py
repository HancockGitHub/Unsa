# CODIGO PARA EL PRODUCTO ENTRE MATRICES
import numpy as np
count = 0
while True:
    try:
        f_1, c_1 = map(int, input(
            'Ingrese numeros de filas y columnas separados por un espacio para la matriz A: ').split())
        f_2, c_2 = map(int, input(
            'Ingrese numeros de filas y columnas separados por un espacio para la matriz B: ').split())
        if c_1 != f_2:
            raise ValueError(
                'Error el numero de columnas de A debe ser igual al numeros de filas de B')
        break
    except ValueError as e:
        count += 1
        if count >= 2:
            print('Es un PRODUCTO entre matrices ingrese las dimensiones validas')
        else:
            print(e)
print('Matriz A')
m1 = np.zeros((f_1, c_1))
for i in range(f_1):
    for j in range(c_1):
        m1[i][j] = float(
            input(f'Ingrese elemento ({i+1},{j+1}) de la matriz A: '))
print('Matriz B')
m2 = np.zeros((f_2, c_2))
for i in range(f_2):
    for j in range(c_2):
        m2[i][j] = float(
            input(f'Ingrese elemento ({i+1},{j+1}) de la matriz B: '))
m3 = np.zeros((f_1, c_2))
for i in range(f_1):
    for j in range(c_2):
        suma = 0
        for k in range(c_1):
            suma += m1[i][j]*m2[i][j]
        m3[i][j] = suma
print('')
print('El producto entre las matrices A y B es:\n', m3)


# * Este es un ejemplo de while mas resumido que el anterior
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
