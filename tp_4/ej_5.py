# Escriba un script que me permita obtener el producto vectorial de dos vectores (representados mediante
# dos arrays unidimensionales) de 3 componentes cada uno. Compare el resultado obtenido utilizando el metodo cross .

import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

prod_vect = np.array([v1[1]*v2[2]-v1[2]*v2[1], v1[2] *
                     v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]])

print(prod_vect)

# utilizando el metodo cross


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
# v3 es el nombre de la variable para el resultado del producto vectorial de v1 y v2
v3 = np.cross(v1, v2)
print(v3)
