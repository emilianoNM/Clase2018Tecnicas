print "Imprimir una matriz\n"
print "Tecnicas de programacion\n"
matriz=[]


filas = int(raw_input("Cantidad de Filas\n"))
columnas = int(raw_input("Cantidad de Columnas\n"))

for i in range(filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for  c in range(columnas):
        matriz[f][c] = int(raw_input("Elementos de la matriz %d,%d\n"%(f,c)))

print (matriz)
