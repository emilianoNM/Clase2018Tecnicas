#Programa hecho por Mario Molina
print ("")
print ("Dibujemos un cuadrado")
print ("")

def dibujar(dimen): 

  if dimen<10:
    print("La dimension minima es 10")
  else:

    	for i in range(0,(dimen/2)): 

        		if i==0 or i==(dimen/2)-1: 

            			print "*"+"*"*(dimen-2)+"*" 

        		else: 

            			print "*"+" "*(dimen-2)+"*" 

cuadrado= int(input("Ingresa el ancho del cuadrado: "))

print ("")
 
dibujar(cuadrado) 
