# Obtener el cociente de dos numeros naturales, mediante restas sucesivas.

dividendo, divisor = map(int, input(
    'Ingrese el dividendo y el divisor separados por un espacio: ').split())
cociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1
resto = dividendo
print('el cociente es: ', cociente)
print('el resto es: ', resto)
