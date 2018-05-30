matriz= []

fi = int(input('Cantidad de filas: '))
co = int(input('Cantidad de columnas'))

for i in range (fi):
	matriz.append([0]*co)

for f in range(fi):
	for c in range(co):
		matriz[f][c] = int(input("elemento %d,%d :" % (f,c)))

print(matriz)