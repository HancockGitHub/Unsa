# Llamemos punto fijo de una matriz (o vector) al elemento cuyo valor es igual a su posici´on en el vector.
# Por ejemplo, 4 es un punto fijo del vector v = [-4 2 -3 3 4] .
# Escriba una funci´on que dada una matriz, devuelva sus puntos fijos, si existen. De lo contrario debe devolver una
# lista vac´ıa [] . Por ejemplo, dado [1, -6, 2, 8, 4, 5] , devuelve [2, 4, 5] y para [4, 5, 7, 8] devuelve
# [] (o cualquier valor pertinente).
# Escriba un script que permita a un usuario ingresar una matriz de dimensi´on n × m y utilice la funci´on programada anteriormente para verificar si el arreglo posee puntos fijos. La salida del programa debe contener las leyendas
# correspondientes.

import numpy as np


def puntos_fijos(matriz):
    puntos = []
    matriz = matriz.reshape(-1) #convierte la matriz en una matriz unidimensional. El argumento -1 se utiliza para que NumPy calcule automáticamente el tamaño de la dimensión desconocida. En otras palabras, -1 significa “cualquier tamaño”. Por lo tanto, esta línea de código convierte cualquier matriz en una matriz unidimensional.
    for i in range(len(matriz)):
        if matriz[i] == i:
            puntos.append(i)
    return puntos


n =int(input('Ingrese el numero de filas de la matriz: '))
m =int(input('Ingrese el numero de columnas de la matriz: '))
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        elemento = int(input(f'Ingrese el elemento ({i}, {j}): '))
        fila.append(elemento)
    matriz.append(fila)

matriz= np.array(matriz)
puntos_fijos = puntos_fijos(matriz)
if len(puntos_fijos) > 0:
    print(f'La matriz tiene los siguientes puntos fijos :{puntos_fijos}')
else:
    print('La matriz no tiene puntos fijos')
    


#más resumido


# def puntos_fijos(matriz):
#     return[i for i in matriz.reshape(-1) if i==matriz[i]]

# n,m=map(int,input('Ingrese el numero de filas y columnas: ').split())
# matriz= [list(map(int,input(f'Ingrese la fila {i+1}: ').split())) for i in range (n)]
# puntos  =puntos_fijos(np.array(matriz))
# print (f'Los puntos fijos son: {puntos}' if len(puntos)>0 else 'La matriz no tiene puntos fijos.')
