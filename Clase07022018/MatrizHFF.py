print("Impresion de una matriz")

Matriz = []

Columnas=int(raw_input("Por favor ingresa el numero de columnas: "))
Filas=int(raw_input("Por favor ingresa el numero de filas: "))
	
for i in range(Filas):
	Matriz.append([0]*Columnas)

for l in range(Filas):
	for m in range(Columnas):
		Matriz[l][m]=int(raw_input("Agrega el valor %d,%d de la matriz: " % (l,m)))

print Matriz
