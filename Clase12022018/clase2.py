#
print ("Hola Mundo" )

print ("Tipos de Datos primitivos")

Numero=12

Flotante=12.0

Cadena="hola juan"
print(type(Numero))
 
print(type(Flotante)) 

print(type(Cadena))

#Cadena=Flotante 

Flotante=14.05

print(Cadena)

print(Flotante)

print(Cadena[1:6:2]) 

arreglo=[1,2,3,4,5,6,7]

print(type(arreglo))

print (arreglo[3])


print("Sentencias de flujo")

x=str(input("por favor ingrese un entero: "))
b=raw_input("Ask user for something.")


if x <0:
	print("segunda linea")
	print ("numero negativo")
elif x==0:
   print("es cero ")
elif x==1:
  print("es uno ")
else : 
   print ("mayor que uno")

for ab in Cadena :
	print (ab)
for j in range(10,0,-2):
        print (j)
for cadenas in ["hola","Emiliano", "feliz" "cumpleanos"]:
	print ("entro")
 	continue	
 	print (cadenas)
	














