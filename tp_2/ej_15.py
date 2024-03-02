'''Dada una lista de números no nulos que pertenecen a movimientos de dinero, en donde los números positivos corresponden a ingresos 
y los números negativos corresponden a egresos. Se desea mostrar el total de ingresos, el total de egresos y el saldo'''
n = int(input("Introduzca la cantidad de números para la lista: "))
N = []
tot_ingr = 0
tot_egr = 0
for i in range(n):
    numero = int(input(f"Ingrese número {i+1} de la lista: "))
    N.append(numero)
print("La lista ingresada es: ", N)
for monto in N:
    if numero > 0:
        tot_ingr += monto
    else:
        tot_egr += abs(monto)
saldo = tot_egr-tot_ingr
print("El total de ingresos es: ", tot_ingr)
print("El total de egresos es: ", tot_egr)
print("El saldo es de: ", saldo)
#! Corregir código
