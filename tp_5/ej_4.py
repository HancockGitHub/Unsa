# Escriba un script que permita el ingreso de un vector de N elementos.
# (a) Muestre por pantalla el vector ingresado.
# (b) Muestre el menor y el mayor elemento.
# (c) Calcule y muestre el promedio de los elementos pares y la suma de los elementos impares.
# (d) Muestre el vector ordenado de menor a mayor, y mayor a menor.

# Ingreso los datos que el usuario elegirá
n = int(input("Introduce la cantidad de elementos del vector: "))
# Creo una lista vacia en la que se almacenaran mas tarde los elementos
vector = []
# Uso la sentencia for para recorrer cada elemento del vector
for i in range(n):
    # Asigno el valor de cada elemento
    elemento = int(input(f"Introduce el elemento {i+1}: "))
    # Append hara que la lista vector se rellene con los elementos por el usuario
    vector.append(elemento)
# Muestro el vector ingresado
print("El vector ingresado es:", vector)

minimo = min(vector)
maximo = max(vector)
print("El mínimo es:", minimo)
print("El máximo es:", maximo)

# Asigno contadores
suma_impares = 0
suma_pares = 0
cantidad_pares = 0

for elemento in vector:
    # Uso un condicional para verficar que el numero sea par
    if elemento % 2 == 0:
        suma_pares += elemento
        cantidad_pares += 1
    else:
        suma_impares += elemento

if cantidad_pares > 0:
    promedio_pares = suma_pares / cantidad_pares
    print("El promedio de los elementos pares es:", promedio_pares)
else:
    print("No hay elementos pares en el vector")

print("La suma de los elementos impares es:", suma_impares)

vector_ordenado = sorted(vector)
print("El vector ordenado de menor a mayor es:", vector_ordenado)

vector_ordenado_inverso = sorted(vector, reverse=True)
print("El vector ordenado de mayor a menor es:", vector_ordenado_inverso)
