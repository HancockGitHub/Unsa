# Diseñe una funcion que tenga como parametro de entrada una matriz y un vector. La funcion debera
# determinar si los elementos del vector corresponden a la diagonal completa de la matriz. Elija adecuadamente el
# parametro de salida de la funcion. Escriba un script que genere una matriz cuadrada de dimension n cuyos elementos
# sean numeros enteros aleatorios. El usuario debe poder ingresar un vector de n elementos, uno a uno. El Script
# utilizara la funcion programada anteriormente para informar si los elementos del vector corresponden a la diagonal
# principal de la matriz. Utilice las leyendas correspondientes para mostrar el resultado.

import numpy as np


def check_diagonal(matr, vector):
    diagonal = np.diag(matr)
    # np.diag me devuelve la diagonal de la matriz
    return np.array_equal(diagonal, vector)
    # verdadero si dos arreglos tienen la misma forma y elementos, falso en caso contrario


n = int(input('Ingrese la dimension de la matriz cuadrada:'))
matr = np.random.randint(0, 10, size=(n, n))
# devuelve numeros enteros de bajo(inclusivo) a alto (exlusivo) aleatorio.randint(bajo, alto=ninguno, tamaño=ninguno , dtype=int)
print('La matriz generada es:\n', matr)  # \n el comando se llama enter
# print(matr)
vector = []
for i in range(n):
    element = int(input(f'Ingrese el elemento {i+1} del vector:'))
    vector.append(element)
if check_diagonal(matr, vector):
    print('Los elementos del vector corresponden a la diagonal ppal de la matriz')
else:
    print('Los elementos del vector no corresponden a la diagonal ppal de la matriz')


# print("el resultado es %.3f el otro es %d"%(matr[2,1],n) sintaxis para determinar las cantidades de cifras significativas que uno desee


#############################################
"""
funcion creada en clase
"""


def check_diagonal(matriz, vector):
    # solo devuelve True si el vector coincide con la diagonal de la matriz
    f, c = matriz.shape()
    if f == c:
        n = vector.size  # con len(vector)
        if f == n:
            diag = np.empty_like()
            for i in range(f):
                for j in range(c):
                    if i == j:
                        diag = matriz[i, j]
            for k in range(n):
                if vector[k] == diag[k]:
                    salida = True
                else:
                    salida = False
                    break
            return salida
        else:
            return False
    else:
        return False


n = int(input('Ingrese dimension: '))
A = np.random.randint(1, 100, (n, n))
v = np.zeros(n)
print('Su matriz\n', A)
for i in range(n):
    v[i] = int(input('Ingrese el elemento' + str(i)+': '))
t = check_diagonal(A, v)
if t:
    print('El vector coincide con la diagonal')
else:
    print('El vector no coincide con la diagonal')


#####################################################
