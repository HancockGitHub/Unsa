'''Dada una lista de números reales no nulos mostrar cuántos números ingresó al usuario, 
determinar el promedio de los positivos y la suma de los negativos. '''
list_num = []
positivos = []
negativos = []
sum_negativos = 0
# Pido al usuario que ingrese una lista de números
print("Ingrese una lista de números reales no nulos. Para terminar ingrese 0")
# *True en este caso permite que la sentencia se ejecute hasta que el usuario ingrese 0
while True:
    numero = float(input("Ingrese número: "))
    if numero == 0:
        break
    list_num.append(numero)
# Contamos cuantos numeros ingresó el usuario
cant_num = len(list_num)
# Calculamos el promedio de los números postivos y la suma de los negativos
# Inicializo un contador
i = 0
while i < cant_num:
    if list_num[i] > 0:
        positivos.append(list_num[i])
    else:
        negativos.append(list_num[i])
        sum_negativos += list_num[i]
    i += 1  # * Su propósito es asegurar que el while avance a traves de cada elemento de la lista sin eso se ejecuta infinitamente
# Verifico si hay números positivos para evitar la división por cero
if len(positivos) > 0:
    prom_positivos = sum(positivos)/len(positivos)
else:
    prom_positivos = 0
print("La lista ingresada es: ", list_num)
print("El promedio de los números positivos de la lista ingresada es: ", prom_positivos)
print("La suma de los números negativos de la lista ingresada es: ", sum_negativos)
