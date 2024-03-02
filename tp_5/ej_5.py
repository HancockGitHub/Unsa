# Escriba un script que normalice los elementos de un arreglo de numeros, de manera que los valores
# esten entre 0 y 1. Por ejemplo, el arreglo array([2, 4, 10, 6, 8, 4]) se convertira en
# array([0.0, 0.25, 1.0, 0.5, 0.75, 0.25]) .

#codigo para normalizar el ejemplo del enunciado
import numpy as np

arreglo = np.array([2, 4, 10, 6, 8, 4])
arreglo_normalizado = (arreglo - arreglo.min()) / (arreglo.max() - arreglo.min())

print(arreglo_normalizado)

#codigo para normalizar numeros aleatorios de 0 a 100
import numpy as np

n = int(input("Introduce la cantidad de elementos del arreglo: "))
arreglo = np.random.randint(0, 100, n)
arreglo_normalizado = (arreglo - arreglo.min()) / (arreglo.max() - arreglo.min())

print("El arreglo original es:", arreglo)
print("El arreglo normalizado es:", arreglo_normalizado)