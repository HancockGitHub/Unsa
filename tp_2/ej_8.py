'''Se desea calcular el salario neto semanal de un trabajador dado el número de horas trabajadas
y el precio que se paga por hora. Las primeras 40 horas se pagan a precio normal y las horas que
pasen de 40 se pagan a 1.5 veces la tarifa normal'''
# Asigno variables
cant_hs = int(input("Ingresar cantidad de horas trabajadas:"))
precio_x_hs = int(input("Ingresar precio que se paga por hora $:"))
# Aplico un condicional if else
if cant_hs <= 40:
    sal_normal = cant_hs*precio_x_hs
    print(f"Tu salario neto semanal sera de ${sal_normal}")
else:
    sal_bonificado = 40*precio_x_hs+(cant_hs-40)*precio_x_hs*1.5
    print("Haz recibido una bonificación")
    print(f"Tu salario neto semanal será de ${sal_bonificado}")
