# Escriba una funcion que tenga como parametro de entrada un vector de dimensioin n y como salida la suma de los elementos del vector. \
# Usar el ciclo for, no emeplear las fuinciones predefinidas de python o numpy


# usando el comando range(len())

def suma_vector(vector):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]
    return suma

# usando funcion enumerate


def suma_vector(vector):
    suma = 0
    for i, valor in enumerate(vector):
        suma += valor
    return suma


# llamo a la funcion
vector = [2, 3, 4, 5]
resultado = suma_vector(vector)
print(resultado)

# Esta es la forma mejor escrita


def suma_vec(vector):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]
    return suma


n = int(input('Ingrese la cantidad de elementos para el vector: '))
vec = []
for i in range(n):
    elemento = float(input(f'Ingrese el elemento {i+1} del vector: '))
    vec.append(elemento)
print('El vector formado es:\n', vec)
print('La suma de los elementos del vector es:\n', suma_vec(vec))
