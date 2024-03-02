
import numpy as np
print("Ingrese los numeros separados por un espacio")

# La funcion map() se utiliza para aplicar una fn a cada elemento de una lista y devolver un iterable del tipo map
x1, y1 = map(int, input('Ingrese un punto del plano: ').split())
x2, y2 = map(int, input('Ingrese otro punto del plano: ').split())
d1 = np.sqrt((x1**2)+(y1**2))
d2 = np.sqrt((x2**2)+(y2**2))
mensaje = 'La mayor distancia será %.3f' % (
    d1) if d1 > d2 else 'La mayor distancia sera %.3f' % (d2)
print(mensaje)
