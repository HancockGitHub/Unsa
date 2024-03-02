import numpy as np

n = int(input("Introduce la dimensión de la matriz cuadrada: "))

matriz = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        matriz[i, j] = float(input(f"Introduce el elemento ({i+1}, {j+1}): "))

print("La matriz ingresada es:")
print(matriz)

escalonada = np.zeros_like(matriz)

for i in range(n):
    for j in range(n):
        if i == j:
            escalonada[i, j] = 1
        else:
            escalonada[i, j] = 0

for i in range(n):
    if matriz[i, i] == 0:
        for j in range(i+1, n):
            if matriz[j, i] != 0:
                matriz[[i, j]] = matriz[[j, i]]
                escalonada[[i, j]] = escalonada[[j, i]]
                break

    for j in range(i+1, n):
        if matriz[j, i] != 0:
            factor = matriz[j, i] / matriz[i, i]
            matriz[j] -= factor * matriz[i]
            escalonada[j] -= factor * escalonada[i]

rango = np.count_nonzero(np.sum(matriz != 0, axis=1))
print("La cantidad de vectores filas que son linealmente independientes es:", rango)

# Este script utiliza dos ciclos for para recorrer los elementos de la matriz y solicita al usuario que ingrese cada elemento.
# Luego, muestra por pantalla la matriz ingresada utilizando la función print(). A continuación, utiliza el método de eliminación de Gauss-Jordan
# para reducir la matriz a su forma escalonada reducida y cuenta el número de filas no nulas utilizando la función np.count_nonzero().

# n = int(input('Ingrese dimension de la matriz caudarada: '))
# matriz = np.random.randint(1, 100, (2, 2))
