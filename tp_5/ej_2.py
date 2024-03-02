# Escriba un script que dados los coeficientes a,b y c de la ecuacion cuadratica:
# A) Evalue el discriminante y por pantalla muestre un texto indicando el tipo de solucion
# B) Calcule sus raices y muestre el resultado por pantalla

##########################################################################

# usando el comando math

import numpy as np
import math

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Las raíces son", x1, "y", x2)
elif discriminante == 0:
    x = -b / (2*a)
    print("La raíz es", x)
else:
    print("No tiene solución real")

##########################################################################


# usando el comando numpy


a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + np.sqrt(discriminante)) / (2*a)
    x2 = (-b - np.sqrt(discriminante)) / (2*a)
    print("Las raíces son", x1, "y", x2)
elif discriminante == 0:
    x = -b / (2*a)
    print("La raíz es", x)
else:
    print("No tiene solución real")

###########################################################################

# practica1

# importo la libreria para hacer arreglos arrays

# entrada de datos ingresados por el usuario
a = int(input('Ingrese el coeficiente a: '))
b = int(input('Ingrese el coeficiente b: '))
c = int(input('Ingrese el coeficiente c: '))
# asigno una variable
discriminante = b**2-4*a*c
# agrego un condicional para ejecutar las distintas opciones
if discriminante > 0:
    # hago uso de la libreria numpy
    x1 = (-b+np.sqrt(discriminante))/(2*a)
    x2 = (-b-np.sqrt(discriminante))/(2*a)
    # si la condicion discriminante>0 se cumple imprimira x1 y x2
    print(f'las raices son {x1} y {x2}')
elif discriminante == 0:
    xx = -b/(2*a)
    # si la condicion discriminante==0 se cumple imprimira xx
    print(f'La raiz es {xx}')
else:
    print(f'No tiene solucion real')

###########################################################################

# practica2

# import numpy as np

# Entrada de datos ingresados por el usuario
a = int(input('Ingrese coeficiente a: '))
b = int(input('Ingrese coeficiente b: '))
c = int(input('Ingrese coeficiente c: '))
# Asigno una variable
discriminante = b**2-4*a*c
# Agrego un condicional para ejecutar las dif opciones
if discriminante > 0:
    # Asigno x1 y x2 como variables y hago uso de la libreria numpy
    x1 = (-b+np.sqrt(discriminante))/(2*a)
    x2 = (-b-np.sqrt(discriminante))/(2*a)
    # Muestro el resultado x1 y x2 cuando discriminante >0
    print(f'Las raices son {x1} y {x2}')
elif discriminante == 0:
    # Asigno xx como variable
    xx = -b/(2*a)
    # Muestro el resultado xx cuando discriminante ==0
    print(f'La raiz es {xx}')
else:
    print(f'No tiene solucion real')
