# En Python una matriz se representa comunmente como una lista de listas. Cada lista interna representa una fila de la matriz
# necesitas utilizar dos bucles for anidados, uno para recorrer las filas y otro para recorrer los elementos dentro de cada fila
# El primer bucle for recorre las filas de la matriz,  ientras que el segundo bucle for recorre los elementos dentro de cada fila.
# esto es necesario porque una matriz puede tener diferentes longitudes de fila y columna, por lo que necesitas iterar sobre
# ambas dimensiones para acceder a cada elemento de la matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)
