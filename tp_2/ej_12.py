'''Se requiere determinar cuánto ahorra una persona en un año, si al final de cada mes deposita cantidades variables de dinero. 
Además, debe informarse cuánto dinero lleva ahorrando mes a mes.'''
ahorro_anterior = float(input("Ingresar ahorro anterior. "))
ahorro_total = 0
for c in range(1, 12):
    deposito = float(input("Ingresar depósito: "))
    ahorro_mes = ahorro_anterior+deposito
    ahorro_total += ahorro_mes
    print("Ahorro del mes: ", ahorro_mes)
    print("Ahorro total: ", ahorro_total)
# TODO necesito mejorar este código
