# Escriba un script que verifique si las componentes de un arreglo son distintas de cero. Si existe alguna
# componente igual a cero, indique su posicion (ındice) en el arreglo.


import numpy as np

arreglo = np.array([2, 5, 8, 9, 1, 0, 8, 5, 0])

for i in range(len(arreglo)):
    if arreglo[i] == 0:
        print(f"La posición {i} del arreglo es igual a cero.")
    else:
        print(f"La posición {i} del arreglo es distinta de cero.")

# ejemplo sin uso de la libreria numpy

# arreglo = [2, 5, 6, 0, 1, 0]
# indices = []
# for i in arreglo:
#     if i == 0:
#         indices.append(arreglo.index(i))
# if len(indices) != 0:
#     print(f'Hay ceros en la posicion {indices}')
# else:
#     print('No hay ceros en el arreglo')

arreglo = [2, 5, 8, 9, 1, 0, 8, 5, 0]
indice = []  # inicializo una lista vacia que se llenaran con elementos mas tarde
for i in arreglo:  # creo un for que me recorrera elementos x elemento la la lista creada
    if i == 0:  # aqui utilizo este control de flujo para que que se cumpla tal condicion
        # aqui agrego los elementos a la lista vacia recorriendo uno x uno a la lista de arreglos
        indice.append(arreglo.index(i))
if len(indice) >= 0:  # utilizo len para verificar si la lista indices no esta vacia
    print(f'Hay ceros en la posicion {indice}')
else:
    print('No hay ceros en el arreglo')
