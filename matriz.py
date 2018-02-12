print("===Imprimir una matriz===")


a=0
b=0

print('\f Imprimir matriz ')

row=int(input("\n\nNúmero de filas: "))
column=int(input("\nNúmeo de columnas: "))

matriz=[None]*row
for a in range(row):
  matriz[a]=[None]*column
  pass

for a in range(row):
  for b in range(column):
    matriz[a][b]=0
  
for a in range(row):
  print("\n")
  for b in range(column):
    print('%f\t' %(matriz[a][b]), end="")
    
print("\n")