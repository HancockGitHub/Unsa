'''Dado un punto (x,y) en el plano, determinar el cuadrante al que pertenece.'''
# Asigno las variables a valores númericos
x, y = map(float, input(
    "Ingrese las coordenadas del punto (x,y) separados por una coma:").split(","))
# !En el .split() en realidad uno puede poner el carácter que desee adentro del paréntesis
# Creo un condicional en primera línea
caudrante = (
    "El punto está en el primer cuadrante. " if x > 0 and y > 0 else
    "El punto está en el segundo cuadrante. " if x < 0 and y > 0 else
    "El punto está en el tercer cuadrante. " if x < 0 and y < 0 else
    "El punto está en el cuarto cuadrante. " if x > 0 and y < 0 else
    "El punto está sobre el eje X."if y == 0 else
    "El punto está sobre el eje Y."if x == 0 else
    "El punto está en el origen."
)
print(caudrante)
