
import numpy as np

m = int(input("Introduce la cantidad de filas de la matriz: "))
n = int(input("Introduce la cantidad de columnas de la matriz: "))

A = np.random.uniform(1, 10, (m, n))

if m == n:
    print("La matriz creada es:")
    print(A)

    U = np.triu(A)
    L = np.tril(A)

    print("La matriz triangular superior es:")
    print(U)

    print("La matriz triangular inferior es:")
    print(L)

    traza = np.trace(A)
    print("La traza de la matriz es:", traza)
else:
    print("La matriz no es cuadrada.")

# Este script utiliza la función np.random.uniform() para crear una matriz A con elementos aleatorios entre 1 y 10. Luego, verifica si A es cuadrada
# utilizando una estructura condicional if. Si A es cuadrada, muestra por pantalla la matriz creada utilizando la función print(), obtiene y muestra por
# pantalla la matriz triangular superior e inferior utilizando las funciones np.triu() y np.tril(), respectivamente, y obtiene y muestra por pantalla la
# traza de la matriz utilizando la función np.trace(). Si A no es cuadrada, muestra un mensaje que lo informa.

# Practica1
#!CODIGO MAL GENERADO
while True:
    try:
        m, n = map(int, input(
            'Ingrese numero de filas y columnas para una matriz separadas por un espacio: ').split())
        break
    except ValueError:
        print('La matriz no es cuadrada, ingrese únicamente números iguales y enteros.')
    except ValueError:
        print('No seas mamon te dije NUMEROS IGUALES Y ENTEROS.')
matriz = np.random.randint(1, 100, size=[m, n])
if m == n:
    print('La matriz creada es:\n', matriz)
# else:
#    print('La matriz no es cuadrada.')


# *FORMA MAS DIVERTIDA DE HACER EL CODIGO
count = 0
while True:
    try:
        m, n = map(int, input(
            'Ingrese número de filas y columnas para una matriz separadas por un espacio: ').split())
        if m != n:
            raise ValueError(
                'La matriz no es cuadrada, ingrese únicamente números iguales y enteros.')
        break
    except ValueError as e:
        count += 1
        if count >= 3:
            print(
                '¡Te dije que ingresaras números iguales y enteros! ¡Hazlo bien, no seas mamón!')
        else:
            print(e)
# En este ejemplo se agrego un contador count para rastrear el numero de entradas no validas que ingreso el usuario.
# si el contador alcanza un valor de 3 o mas, se muestra el mje mas imperativo. Si el comtador es menor que 3, se
# muestra el mje de error especifico para la entrada no valida.
# Tambien se modifico el codigo del bloque try para incluir una comprobacion adicional depues de la entrada
# de datos para asegurarse de que la matriz sea cuadrada. si no lo es se lanza una excepcion con un msj de error personalizado
