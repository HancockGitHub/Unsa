# Escriba una funcion que realice la transformacion de coordenadas cartesianas en coordenadas polares en un plano. Los parametros de entrada deben ser x e y
# los parametros de salida r y tita. Programe tambien en la funcion que realice la transformacion inversa

import numpy as np


def coord_cart_a_polares(x, y):

    # import numpy as np
    r = np.sqrt(x**2+y**2)
    tita = np.arctan(y/x)
    return (r, tita)


def coord_polares_a_cart(r, tita):

    # import numpy as np
    x = r*np.cos(tita)
    y = r*np.sin(tita)
    return (x, y)

# coordenadas=input('ingresar coordenadas: ')


a = coord_cart_a_polares(5, 3)
print(a)

b = coord_polares_a_cart(4, 1)
print(b)
