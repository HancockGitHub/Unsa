prec_inicial = float(input('Ingrese precio: '))
print('1) Torrontés')
print('2) Malbec')
op = int(input('Elija una opcion: '))
if op == 1:
    print('Usted escogió Torrontés, por favor seleccione la calidad')
    print('Calidad 1')
    print('Calidad 2')
    print('Calidad 3')
    cal = int(input('Elija la calidad: '))
    if cal == 1:
        venta = prec_inicial+0.1*prec_inicial
        print(f'La venta sera de {venta}')
    elif cal == 2:
        venta = prec_inicial
        print(f'La venta sera de {venta}')
    else:
        venta = prec_inicial-0.5*prec_inicial
        print(f'La venta sera de {venta}')
else:
    print('Usted escogió Malbec, por favor seleccione la calidad')
    print('Calidad 1')
    print('Calidad 2')
    print('Calidad 3')
    cal = int(input('Elija la calidad: '))
    if cal == 1:
        venta = prec_inicial+0.1*prec_inicial
        print(f'la venta sera de {venta}')
    elif cal == 2:
        venta = prec_inicial
        print(f'la venta sera de {venta}')
    else:
        venta = prec_inicial-0.05*prec_inicial
        print(f'la venta sera de {venta}')
