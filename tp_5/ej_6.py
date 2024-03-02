# Escriba un script que dado un arreglo de numeros enteros "a" obtenga un nuevo arreglo
# "b" con la misma cantidad de elementos, tal que el elemento en la posicion b[i] sea el
# producto de todos los elementos de "a" a excepcion del elemento a[i]

import numpy as np

a = np.array([1, 2, 3])
# Zero_like fuerza la matriz original a transformarse en ceros
b = np.zeros_like(a)

for i in range(len(a)):
    b[i] = np.prod(np.delete(a, i))

print("El arreglo original es:", a)
print("El arreglo resultante es:", b)
