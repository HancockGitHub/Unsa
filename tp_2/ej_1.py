# Una modista compra las telas en el extranjero y debe realizar el pedido en pulgadas cuando
# ella realiza sus calculos en metros. Realice un algortimo en pseudocodigo que ayude a la
# modista a realizar su compra

precio_galon = 4.50
cantidad_litros = float(
    input("Ingrese la cantidad de leche producida en litros: "))
cantidad_galones = cantidad_litros / 3.78541
dinero_recibido = cantidad_galones * precio_galon
# print("El productor recibirá $" + str(dinero_recibido) +
#       " por la venta de su producción de leche.")
print('El productor recibira $ %.3f' %
      (dinero_recibido)+' por la venta de su produccion de leche.')
