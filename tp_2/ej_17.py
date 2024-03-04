'''Un comercio del medio vende distintos tipos de articulos. Los de fabricacion propia (tipo "P") pagan una tasa de IVA del 10.5%, los importados (tipo "I") 
una tasa del 27% y el resto (tipo "R") una tasa del 21%. Se tiene un listado con codigos de articulos, tipo, cantidad e importe unitario de todas las ventas 
realizadas en el mes pasado. Determinar el importe total del IVA a pagar.'''
# Listado de ventas (codigo,tipo, cantidad e importe unitario)
ventas = [
    ("001", "P", 5, 10),  # Ejemplo:articulo de fabricacion propia
    ("002", "I", 3, 15),  # Ejemplo:articulo importado
    ("003", "R", 2, 20)  # Ejemplo:otro tipo de articulo
]
importe_total_IVA = 0
i = 0
# Mientras haya ventas por procesar
while i < len(ventas):
    venta = ventas[i]
    cod_art, tipo_art, cantidad, importe_unitario = venta
    # Determinamos la tasa de IVA segun el tipo de articulo
    if tipo_art == "P":
        tasa_IVA = 0.105  # 10.5%
    elif tipo_art == "I":
        tasa_IVA = 0.27  # 27%
    else:
        tasa_IVA = 0.21  # 21%
    # Calculamos el importe del IVA para esta venta
    importe_IVA = cantidad*importe_unitario*tasa_IVA
    # Sumamos el importe del IVA al total
    importe_total_IVA += importe_IVA
    # Pasamos a la siguiente venta
    i += 1
# Imprimo el importe total del IVA a pagar
print("El importe total del IVA a pagar es $ %.3f" % (importe_total_IVA))
