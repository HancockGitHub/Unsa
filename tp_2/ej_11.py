'''Dada una lista de n números, entonces determinar cuántos pares hay.'''
pares = 0
N = int(input("Ingesar cantidad de números enteros de la lista: "))
for c in range(1, N+1):
    list_num = int(input(f"Ingrese {c} número de la lista: "))
    if list_num % 2 == 0:
        pares += 1
print("La cantidad de números pares de la lista es: ", pares)
