'''Dados dos puntos en el plano (x1,y1) y (x2,y2) determine cuál de ellos está más alejado del origen.'''
# Traigo la biblioteca de Numpy
from numpy import *
# Asigno a las variables valores numéricos
x1, y1 = map(int, input(
    "Ingrese los números de un punto del plano separados por una coma:").split(","))
x2, y2 = map(int, input(
    "Ingrese los números de un punto del plano separados por una coma:").split(","))
# Utilizo el Teorema de Pitágoras para resolver cuál punto esta más alejado al origen
d1 = sqrt(x1**2+y1**2)
d2 = sqrt(x2**2+y2**2)
# Aplico un condicional para ejecutar el código
if d1 < d2:
    print("El punto más alejado del origen es", (x2, y2))
elif d1 > d2:
    print("El punto más alejado del origen es", (x1, y1))
else:
    print("Ambos puntos están alejados a la misma distancia del origen")


# * Aplico un condicional en línea
resultado = (
    ("El punto más alejado del origen es", (x2, y2)) if d1 < d2 else
    ("El punto más alejado del origen es", (x1, y1)) if d1 > d2 else
    "Ambos puntos están alejados a la misma distancia del origen"
)
print(resultado)
#! Aquí devuelvo dos valores (msj,punto) por lo que agrupo los pares (msj,punto) entre \
#! paréntesis para asegurar que python los interprete como un solo valor
