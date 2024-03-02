import numpy as np
from numpy.polynomial import Polynomial
n = int(input('Ingrese el grado del polinomio: '))
coeficientes = []
for i in range(n+1):
    coeficiente = float(input(f'Ingrese coeficiente a_{i}: '))
    coeficientes.append(coeficiente)
polinomio = Polynomial(coeficientes)

m = int(input('Ingrese el grado del polinomio: '))
coeficientes1 = []
for i in range(m+1):
    coeficiente1 = float(input(f'Introduce coeficiente a_{i}: '))
    coeficientes1.append(coeficiente1)
polinomio1 = Polynomial(coeficientes1)
producto = polinomio*polinomio1
print(polinomio)
print(polinomio1)
print(producto)
