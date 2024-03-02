# Escriba una funcion que calcule el area y el perimetro de un poligono regular de n lados inscrito en una
# circunferencia de radir r. La misma debe poseer como parametros de entrada el numero de lados y el radio;
# y como parametros de salida el area y el perimetro correspondiente.

import math


def poligono(n, r):
    area = (1/2) * n * r ** 2 * math.sin(2*math.pi/n)
    perimetro = 2 * n * r * math.sin(math.pi/n)
    return area, perimetro
