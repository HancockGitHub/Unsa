# Escriba una funcion que calcule el factorial de un numero natural dado. El calculo del factorial debe incluir for
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado


# def factorial(n):
#     if n < 0:
#         r0 = 0
#     elif n > 2:
#         resultado = 1
#         r0 = 1
#     else:
#         N = 0
#         resultado = 1
#         while N < n:
#             resultado *= (N+1)
#             N += 1
#         r0 = 1
#     if r0 == 1:
#         salida = [r0, resultado]
#     else:
#         salida = [r0, 0]
#     return salida


d = factorial(1)
print(d)
