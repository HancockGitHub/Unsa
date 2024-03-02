import numpy as np
from numpy.polynomial import Polynomial
n = int(input('Introduce el orden del polinomio: '))
coeficientes = []
for i in range(n+1):
    coeficiente = float(
        input(f'Intoduce el coeficiente a_{i} del polinomio: '))
    coeficientes.append(coeficiente)
polinomio = Polynomial(coeficientes)
raices = np.roots(coeficientes)
print('El polinomio ingresado es:\n', polinomio)
