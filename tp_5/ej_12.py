import numpy as np

n = int(input("Introduce el orden del sistema de ecuaciones: "))

A = np.zeros((n, n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Introduce el coeficiente a_{i+1}{j+1}: "))

for i in range(n):
    b[i] = float(input(f"Introduce el término independiente b_{i+1}: "))

while True:
    print("Seleccione un método para resolver el sistema:")
    print("1. Inversa de una matriz")
    print("2. Función para resolver un sistema de ecuaciones lineales")
    print("3. Método de Cramer")
    opcion = int(input("Opción: "))

    if opcion == 1:
        try:
            A_inv = np.linalg.inv(A)
            x = np.dot(A_inv, b)
            break
        except np.linalg.LinAlgError:
            print("La matriz A no es invertible. Intente con otro método.")
    elif opcion == 2:
        try:
            x = np.linalg.solve(A, b)
            break
        except np.linalg.LinAlgError:
            print("La matriz A no es invertible. Intente con otro método.")
    elif opcion == 3:
        det_A = np.linalg.det(A)
        if det_A == 0:
            print("La matriz A no es invertible. Intente con otro método.")
        else:
            x = []
            for i in range(n):
                A_i = A.copy()
                A_i[:, i] = b
                x_i = np.linalg.det(A_i) / det_A
                x.append(x_i)
            break
    else:
        print("Opción inválida. Intente nuevamente.")

print("La matriz A es:")
print(A)

print("El vector b es:")
print(b)

print("La solución del sistema es:")
print(x)
