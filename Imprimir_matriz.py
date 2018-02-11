i=0
j=0

print('\f Imprimir matriz ')

row=int(input("\n\nNúmero de filas: "))
column=int(input("\nNúmeo de columnas: "))

matriz=[None]*row
for i in range(row):
  matriz[i]=[None]*column
  pass

for i in range(row):
  for j in range(column):
    matriz[i][j]=0
  
for i in range(row):
  print("\n")
  for j in range(column):
    print('%f\t' %(matriz[i][j]), end="")
    
print("\n")
  
  



