print("Bienvenido, este programa imprime una matriz")

matriz=[]

print("ingresa una matriz de tipo mxn")
filas=int(raw_in("Por favor introduce el numero de filas que contiene tu matriz:")
columnas=int(raw_input("Por favor introduce el numero de columnas que contiene tu matriz:")

for a in range(filas):
     matriz.append([0]*columnas) 

for b in range(filas):
    for c in range(columnas):
          matriz[a][b]=int(raw_input("posicion %d,%d": %(b,c)))   

print matriz
          
