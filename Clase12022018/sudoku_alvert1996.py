#Alberto Garcia Salazar
print("\nEste programa que un Sudoku de 9x9 este resuelto")
print("\nLas reglas son que agregaras los 9 numeros por cada renglon separados por ',' (comas) y presionaras 'enter'")
print("hasta que logres llenar los nueve renglones con 9 numeros")

M=[]
for i in range(9):
	M.append([0]*9)

for i in range(9):
	for j in range(9):
		M[i][j]=raw_input("[%d][%d]: "%(i,j))
i=0
j=0
n=0
#imprimimos la matriz
print "\nLa solucion de tu sudoku se observa: \n"
for i in range(9):
	while j<9:
		a=M[i][j]
		if j>0:
			if j % 3==0:
				print "|",
		print ""+str(a)+"",
		if j==8:
			print "|",			
		j=j+1
	print ""
	n=n+1
	if n % 3==0:
		print "____"*(6)
	j=0

i=0
j=0
a=0
m=0
#Analisis de cada elento de la matriz 
for i in range(9):
	for j in range(9):
		a=M[i][j]
		for k in range(9):
			b=M[i][k]
			if j != k:
				if a==b:
					print "Hay un numero repetido en la solucion [i][k] [",i,"][",k,"] y [i][j] [",i,"][",j,"]"
					print "Numero repretido:",a,"",b
					b=0
					m=1
					break
			if b==0:
				break
		if b==0:
			break
		for h in range(9):
			c=M[h][j]
			if i != h:
				if a==c:
					print ("Hay un numero repetido en la solucion [h][j] [%d][%d] y [i][j] [%d][%d]"%(h,j,i,j))
					print "Numero repetido",a,"",c
					c=0
					m=1
					break
			if c==0:
				break
		if c==0:
			break

if m==0:
	print ("\n        ¡FELICIDADES TU SUDOKU ES CORRECTO!\n")


