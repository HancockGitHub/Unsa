import numpy as np

n = int(input("Introduce el orden de los polinomios: "))

coeficientes1 = []
coeficientes2 = []

for i in range(n+1):
    coeficiente1 = float(input(f"Introduce el coeficiente del primer polinomio a_{i}: "))
    coeficientes1.append(coeficiente1)

for i in range(n+1):
    raiz = float(input(f"Introduce la raíz del segundo polinomio {i+1}/{n+1}: "))
    coeficiente2 = 1
    for j in range(n+1):
        if j != i:
            coeficiente2 *= (raiz - float(input(f"Introduce la raíz {j+1}/{n}: ")))
    coeficientes2.append(coeficiente2)

polinomio1 = f"{coeficientes1[0]}"

for i in range(1, n+1):
    if coeficientes1[i] > 0:
        polinomio1 += f" + {coeficientes1[i]}*x^{i}"
    elif coeficientes1[i] < 0:
        polinomio1 += f" - {-coeficientes1[i]}*x^{i}"

polinomio2 = f"{coeficientes2[0]}"

for i in range(1, n+1):
    if coeficientes2[i] > 0:
        polinomio2 += f" + {coeficientes2[i]}*x^{i}"
    elif coeficientes2[i] < 0:
        polinomio2 += f" - {-coeficientes2[i]}*x^{i}"

producto = np.convolve(coeficientes1, coeficientes2)

polinomio_producto = f"{producto[0]}"

for i in range(1, 2*n+1):
    if producto[i] > 0:
        polinomio_producto += f" + {producto[i]}*x^{i}"
    elif producto[i] < 0:
        polinomio_producto += f" - {-producto[i]}*x^{i}"

valor = float(input("Introduce el valor a evaluar: "))

resultado = 0

for i in range(2*n+1):
    resultado += producto[i] * valor**i

print("El primer polinomio es:")
print(polinomio1)

print("El segundo polinomio es:")
print(polinomio2)

print("El producto de ambos polinomios es:")
print(polinomio_producto)

print(f"El valor ingresado es: {valor}")
print(f"El resultado de la evaluación es: {resultado}")
