'''Dadas las edades de tres personas, determinar la mayor'''
# Asigno tres variables distintas para tres valores numéricos
x = int(input("Ingrese edad 1:"))
y = int(input("Ingrese edad 2:"))
z = int(input("Ingrese edad 3:"))
# Creo un condiconal if elif else para ejecutar el código
if x > y and x > z:
    print(f"De las tres personas la mayor es la que tiene la edad de {x} años")
elif y > x and y > z:
    print(f"De las tres personas la mayor es la que tiene la edad de {y} años")
else:
    print(f"De las tres personas la mayor es la que tiene la edad de {z} años")
#! f es un formato de string
