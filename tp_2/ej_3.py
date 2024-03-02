# Dados dos puntos en el plano (x1,y1) y (x2,y2) calcule y muestre la distancia que los separa
import numpy as np
x1, y1 = map(int, input(
    'Ingrese un punto del plano separados por un espacio: ').split())
x2, y2 = map(int, input(
    'Ingrese otro punto del plano separados por un espacio: ').split())
d = np.sqrt((x2-x1)**2+(y2-y1)**2)
print('La distancia que los separa sera de %.3f' % (d))
