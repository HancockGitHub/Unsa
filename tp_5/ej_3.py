# En el calendario gregoriano un año bisiesto es aquel que es divisible por 4, a excepcion de aquellos que
# sean divisibles por 100, a menos que sean tambien divisibles por 400. Escriba un script que determine si un año es
# bisiesto o no.


import calendar

# Sin usar ningun comando
año = int(input('Ingrese el año:'))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f'{año} es un año bisiesto')
        else:
            print(f'{año} no es un año bisiesto')
    else:
        print(f'{año} es un año bisiesto')
else:
    print(f'{año} no es un año bisiesto')


# otro ejemplo mas corto

año = int(input("Introduce un año: "))

if not año % 4 and (año % 100 or not año % 400):
    print(año, "es un año bisiesto")
else:
    print(año, "no es un año bisiesto")


# usando el comando calendar


año = int(input("Introduce un año: "))

if calendar.isleap(año):
    print(año, "es un año bisiesto")
else:
    print(año, "no es un año bisiesto")
