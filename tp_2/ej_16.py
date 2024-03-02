'''Dada una lista de números reales no nulos mostrar cuántos números ingresó al usuario, 
determinar el promedio de los positivos y la suma de los negativos. '''
k = int(input("Ingrese la cantidad de números de la lista: "))
N = []
sum_positivos = 0
sum_negativos = 0
for i in range(k):
    lista = int(input(f"Ingrese elemento N°{i+1} de la lista: "))
    N.append(lista)
print("la lista ingresada es: ", N)
for numero in N:
    if lista > 0:
        sum_positivos += numero

    else:
        sum_negativos += abs(numero)
prom_positivos = sum_positivos/k
print(prom_positivos)
print(sum_negativos)
