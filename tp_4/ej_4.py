# Escriba un script que me permita obtener el producto interno o escalar de dos vectores (representados
# mediante dos arrays unidimensionales). Compare el resultado obtenido utilizando el operador @ y el metodo dot


# utilizando la funcion inner

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

producto_interno = np.inner(a, b)

print(producto_interno)


# utilizando el operador @


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
prod_interno = a@b
print(prod_interno)

# utlizando el metodo dot


# a = [1, 2, 3]
# b = [4, 5, 6]
c = np.dot([1, 2, 3], [4, 5, 6])
print(c)
