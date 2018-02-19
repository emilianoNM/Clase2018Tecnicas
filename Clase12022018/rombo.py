# creado por Hernandez Quintana Luis Eduardo
import time
print ("\n\nEste programa es para dibujar un rombo a partir de las dimensiones dadas por el usuario")
time.sleep(5)
input("Pulse enter para continuar")
print ("\n\nIngresa el valor medio del rombo:")
print ("************************")
n = int (input(""))
#en esta parte hacemos la primera mitad de nuestro bombo
for i in range(n+1):
  for j in range(n-i):
    print(" ", end="")
  for k in range(2*i-1):
    print("*", end="")
  print("")
  
  # en esta parte hacemos la segunda mitad de nuetro rombo
for i in range(n-1, 0, -1):
  for j in range(n-i):
    print(" ", end="")
  for k in range(2*i-1):
    print("*", end="")
  print("")

print("\n")

