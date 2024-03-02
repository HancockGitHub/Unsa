# Obtener todas las potencias de un numero a desde a^1 hasta a^k, donde a y k son valores de entrada
# a es un numero real y k un entero positivo. Defina usted cual debe ser el parametro de salida.

def potencias(a, k):
    potencias = []
    for i in range(1, k+1):
        potencia = a ** i
        # append agrego un elemento al final de la lista
        potencias.append(potencia)
    return potencias


# a = float(input('ingrese las base de las potencias:'))
# k = int(input('ingrese el maximo exponente:'))
# c, d = potencias(a, k)
# print('las potencias obtenidas son:', c)
# print('las potencias obtenidas son:', d)

# a = potencias(2, 4)
# print(a)
