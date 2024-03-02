# Escriba un script que realice la multiplicacion entre dos matrices nxn. Compare el resutado utilizando el resultado con el operador @
import numpy as np

# *Codigo sencillo sin uso de librerias

matriz1 = [[1, 2], [3, 4], [5, 6]]
matriz2 = [[7, 8], [9, 10]]

resultado = [[0 for j in range(len(matriz2[0]))] for i in range(len(matriz1))]

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

print(resultado)

# *Codigo mejorado
count = 0
while True:
    try:
        f_1, c_1 = map(int, input(
            'Ingrese números de filas y columnas separados por un espacio para la matriz A: ').split())
        f_2, c_2 = map(int, input(
            'Ingrese números de filas y columnas separados por un espacio para la matriz B: ').split())
        if c_1 != f_2:
            raise ValueError(
                'Error el número de columnas de A debe ser igual al numeros de filas de B')
        break
    except ValueError as e:
        count += 1
        if count >= 2:
            print('Es un PRODUCTO entre matrices ingrese las dimensiones válidas')
        else:
            print(e)
print('Matriz A')
m1 = np.zeros((f_1, c_1))
for i in range(f_1):
    for j in range(c_1):
        m1[i][j] = float(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz A: '))
print('Matriz B')
m2 = np.zeros((f_2, c_2))
for i in range(f_2):
    for j in range(c_2):
        m2[i][j] = float(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz B: '))
m3 = np.zeros((f_1, c_2))
for i in range(f_1):
    for j in range(c_2):
        suma = 0
        for k in range(c_1):
            suma += m1[i][j]*m2[i][j]
        m3[i][j] = suma
print('')
print('El producto entre las matrices A y B es:\n', m3)
