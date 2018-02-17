d=int(input("\n ¿Mitad del número de caracteres en la diagonal vertical?'\n>"))

for i in range(d+1):
  for j in range(d-i):
    print(" ", end="")
  for k in range(2*i-1):
    print("%", end="")
  print("")
  
for i in range(d-1, 0, -1):
  for j in range(d-i):
    print(" ", end="")
  for k in range(2*i-1):
    print("%", end="")
  print("")

print("\n")

