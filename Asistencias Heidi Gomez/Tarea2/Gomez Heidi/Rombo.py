#Laura Gomez
#Colorear un rombo con ascii

print (" ^^^^^^^^^^^^ROMBO^^^^^^^^^^^ ")
print ("\nEste programa imprime un rombo")
print ("\n Sera impreso con simbolos *")
print ("\n Podras introducir cuantos simbolos quieres que mida por lado\n")

n=int(input("Introduce el valor del lado: "))

for i in range(n+1):
     for j in range(n-i):
               print(" ",end="")
     for k in range(2*i-1):
               print("*",end="")
     print("")

for i in range(n-1,0,-1):
     for j in range(n-i):
	       print(" ",end="")
     for k in range(2*i-1):
	       print("*",end="")
     print("")
