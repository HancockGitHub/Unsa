'''Obtener el cociente y el resto de 2 números naturales mediante restas sucesivas'''
# TODO Buscar una forma de hacer que el código me lea que los números que ingrese sean exclusivamente naturales.
dividendo = int(input("Ingresar dividendo: "))
divisor = int(input("Ingresar divisor: "))
cociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1

resto = dividendo

print("El cociente de la división es:", cociente)
print("El resto de la división es:", resto)
