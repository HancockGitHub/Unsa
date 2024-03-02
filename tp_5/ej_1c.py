'''Dada una lista de numeros enteros determinar cuantos pares hay'''
n = int(input('Introduce la cantidad de numeros para la lista: '))
N = []
pares = 0
for i in range(n):
    elemento = int(input(f'Ingrese elemento {i+1} de la lista: '))
    N.append(elemento)
print('La lista ingresada es', N)

for elemento in N:
    if elemento % 2 == 0:
        pares += 1
print('La cantidad de pares de la lista es:', pares)
