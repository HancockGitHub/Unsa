import numpy as np

m = int(input("Introduce la cantidad de filas de la matriz: "))
n = int(input("Introduce la cantidad de columnas de la matriz: "))

matriz = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        matriz[i, j] = float(input(f"Introduce el elemento ({i+1}, {j+1}): "))

print("La matriz ingresada es:")
print(matriz)

diagonal = np.diag(matriz)
print(f"El vector formado por los elementos de la diagonal ppal es {diagonal}")


# Este script utiliza dos ciclos for para recorrer los elementos de la matriz y solicita al usuario que ingrese cada elemento.
# Luego, muestra por pantalla la matriz ingresada utilizando la función print() y el vector formado por los elementos de la diagonal
# principal utilizando la función np.diag().

# *Sin usar librerias me devuelve como salida una matriz de una dimension
f, c = map(int, input(
    'Ingrese numeros de fila y columnas separadas por un espacio: ').split())
matr = []
for i in range(f):
    fila = []
    for j in range(c):
        elemento = int(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
        fila.append(elemento)
    matr.append(fila)
print(matr)


# Practica1
f, c = map(int, input(
    'Ingrese el numero de filas y columnas para una matriz separadas por un espacio: ').split())
matriz = []
for i in range(f):
    fila = []
    for j in range(c):
        elemento = int(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
        fila.append(elemento)
    matriz.append(fila)
print(matriz)


# Practica2
f, c = map(int, input(
    'Ingrese el numero de filas y columnas para una matriz separadas por un espacio: ').split())
#!El par de parentesis adicionales agrupan a f y c en una sola tupla porque si no los estoy pasando como un argumento
matriz = np.zeros((f, c))
for i in range(f):
    for j in range(c):
        matriz[i, j] = int(
            input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
print(matriz)


#!CODIGO MEJORADO PARA EL INGRESO DE UNA MATRIZ
# Pedir al usuario las dimensiones de la matriz
while True:
    try:
        f, c = map(int, input(
            'Ingrese el numero de filas y columnas para una matriz separadas por un espacio: ').split())
        break
    except ValueError:
        print('Por favor, ingrese numeros enteros es para el tamaño de una matriz no sea pendejo.')

# *Para mejorar el codigo de entrada utilizo el bloque try-except para detectar errores de entrada del usuario
# *y solicitar que se ingrese una entrada valida en caso de un error

# Crear una matriz de ceros con las dimensiones especificadas
matriz = np.zeros((f, c))

# Pedir al usuario los elementos de la matriz
for i in range(f):
    for j in range(c):
        while True:
            try:
                matriz[i, j] = float(
                    input(f'Ingrese el elemento ({i+1},{j+1}) de la matriz: '))
                break
            except ValueError:
                print('Por favor, ingrese un numero real valido.')
print(matriz)
