def calcular_s(n):
    # n=int(input())
    suma = 0
    for valor in range(1, n+1):
        suma = suma + valor
        if valor < n:
            print(valor, end='+')
        else:
            print(valor, end='=')
    print(suma)


s = calcular_s(3)
print(s)


def calcular_s(m: int, n: int) -> float:
    s = 0
    for k in range(1, n+1):
        s += 1/(k**m)
    return s


resultado = calcular_s(4, 2)
print(resultado)


def sumatoria(m, n):
    s = 0
    # uso for por que ya conozco de antemano el numero de repeticiones si no fuera tal caso usaria while
    for k in range(1, n+1):
        s += 1/(k**m)
    return s


n = input('El numero de terminos en la sumatoria: ')
m = input('El exponente: ')
k = calcular_s(int(m), int(n))

print('El resultado es ', k)
