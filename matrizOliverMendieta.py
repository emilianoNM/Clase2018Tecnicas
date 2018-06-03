print('Imprimir matriz')
i=0
j=0
renglones = int(input("\nIngrese numero de renglones\n"))
columnas = int(input("\nIngrese numero de columnas\n"))

matriz=[None]*renglones

for i in range(renglones):
    
    matriz[i]=[None]*columnas
    pass
for i in range(renglones):
    for j in range(columnas):
        matriz[i][j]=0
for i in range(renglones):
    print("\n")
    for j in range(columnas):
     print("%f\t" %(matriz[i][j]), end="")
        
print("\n")
