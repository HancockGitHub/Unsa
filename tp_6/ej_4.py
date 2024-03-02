# Escriba una funcion que realice las cuatro operaciones aritmeticas basicas. La misma debe poseer
# tres parametros de entrada: dos numericos relacionados con los operandos y un caracter relacionado con el operador
# La salida de la funcion debe ser el valor resultado de la operacion.


# def operaciones_aritmeticas(num1, num2, operador):
#     if operador == '+':
#         resultado = num1 + num2
#     elif operador == '-':
#         resultado = num1 - num2
#     elif operador == '*':
#         resultado = num1 * num2
#     elif operador == '/':
#         resultado = num1 / num2
#     else:
#         print('Operador inválido')
#         return None
#     return resultado

# resultado = operaciones_aritmeticas(5, 3, '+')
# print(resultado)

def operacion(num1, num2, operador):
    if operador == '+':
        resultado = num1+num2
    elif operador == '-':
        resultado = num1-num2
    elif operador == '*':
        resultado = num1*num2
    elif operador == '/':
        resultado = num1/num2
    else:
        print('Operador no valido.')
        return None  # *Valor especial que se utiliza para denotar la ausencia de un valor valido
    return resultado


x1 = float(input('Ingrese un numero para operar: '))
x2 = float(input('Ingrese otro numero para operar: '))
print('Elija una operacion llamando a su signo')
print('+.Suma')
print('-.Resta')
print('*.Producto')
print('/.División')
op = input('Escojo: ')
print(f'La operacion elegida es {op}')
print('El resultado será:\n', operacion(x1, x2, op))
