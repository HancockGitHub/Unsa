# Un productor de leche lleva el registro de produccion en litros, pero el comprador le paga en galones.
# Realice un algoritmo que indique al productor cuanto dinero recibira por la venta de su produccion de
# leche en un dia


# Datos de entrada
produccion_litros = float(input("Ingrese la producción de leche en litros: "))
precio_por_galon = float(input("Ingrese el precio por galón: "))

# Convertir producción de litros a galones (1 galón = 3.78541 litros)
produccion_galones = produccion_litros / 3.78541

# Calcular el dinero recibido por la venta (precio_por_galon * produccion_galones)
dinero_recibido = precio_por_galon * produccion_galones

# Mostrar el resultado
print("El productor recibirá ${:.2f} por la venta de su producción de leche en un día.".format(
    dinero_recibido))
