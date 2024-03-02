# Se requiere obtener el area de la figura dados el radio de la circunferencia R y la longitud de la hipotenusa H.
from numpy import *
# import numpy as np
num_pi = pi
radio = int(input('Ingresar radio: '))
longitud = int(input('Ingresar longitud: '))
area1 = (num_pi*(radio)**2)/2
area2 = (2*radio*longitud)/2
total_area = add(area1, area2)
print('El area de la figura sera de: ', total_area)
