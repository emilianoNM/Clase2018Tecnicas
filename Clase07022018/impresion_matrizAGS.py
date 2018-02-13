print("Impresion de una matriz")

matriz = []

columnas=int(raw_input("elige el numero de columnas: "))
fila=int(raw_input("dame el numero de filas: "))
	
for i in range(fila):
	matriz.append([0]*columnas)

for l in range(fila):
	for m in range(columnas):
		matriz[l][m]=int(raw_input("Agrega el valor de %d,%d de la matriz: " % (l,m)))

print matriz

