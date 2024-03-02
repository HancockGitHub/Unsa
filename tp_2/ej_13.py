'''Obtener el producto de dos números naturales, mediante sumas sucesivas'''
print("Ingrese el producto de dos números naturales de la forma a*b")
a, b = map(int, input().split("*"))
producto = 0
for i in range(b):
    producto += a
print("El resultado es:", producto)
# TODO Mejorar el codigo de forma que salte un error si ingresaan numeros que no son naturales
