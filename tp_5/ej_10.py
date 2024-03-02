import numpy as np
import sympy as sp

n = int(input("Introduce el orden del polinomio: "))

coeficientes = []

for i in range(n+1):
    coeficiente = float(input(f"Introduce el coeficiente a_{i}: "))
    coeficientes.append(coeficiente)

x = sp.symbols('x')
polinomio = sum([coeficientes[i] * x**i for i in range(n+1)])

raices = np.roots(coeficientes)

valor = float(input("Introduce el valor a evaluar: "))
resultado = polinomio.subs(x, valor)

print("El polinomio es:")
print(polinomio)

print("Las raíces del polinomio son:")
print(raices)

print(f"El valor ingresado es: {valor}")
print(f"El resultado de la evaluación es: {resultado}")

# ###################################

n = int(input("Introduce el orden del polinomio: "))

coeficientes = []

for i in range(n+1):
    coeficiente = float(input(f"Introduce el coeficiente a_{i}: "))
    coeficientes.append(coeficiente)

raices = np.roots(coeficientes)

polinomio = f"{coeficientes[0]}"

for i in range(1, n+1):
    if coeficientes[i] > 0:
        polinomio += f" + {coeficientes[i]}*x^{i}"
    elif coeficientes[i] < 0:
        polinomio += f" - {-coeficientes[i]}*x^{i}"

valor = float(input("Introduce el valor a evaluar: "))

resultado = 0

for i in range(n+1):
    resultado += coeficientes[i] * valor**i

print("El polinomio es:")
print(polinomio)

print("Las raíces del polinomio son:")
print(raices)

print(f"El valor ingresado es: {valor}")
print(f"El resultado de la evaluación es: {resultado}")
