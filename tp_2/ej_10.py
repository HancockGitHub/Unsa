'''Los ingresantes de un equipo de trabajo miden individualmente la masa de un cuerpo en el laboratorio
escolar obteniedo k resultados. Calcular el valor promedio de las mediciones.'''
k = int(input("Ingresar el número de mediciones tomadas: "))
suma_mediciones = 0
for i in range(k):
    masa = float(input(f"Ingrese la masa medida {i+1}: "))
    suma_mediciones += masa
promedio = suma_mediciones/k
print("El valor promedio de las mediciones es: ", promedio)
