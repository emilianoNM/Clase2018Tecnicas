print "DIBUJAR UN ROMBO \n" 

print ("Opciones: \n")
print ("1. Altura y Ancho")
print ("2. Longitud de los lados")
opcion=input("Selecciona un modo: ")

if opcion==1:
	print ("El numero de elementos debe ser numeros impares y mayores a 1")
	ancho=input("Ingresa el numero de elementos para su rombo: ")
	if ancho % 2==0 or ancho==1:
		print ("El numero de elementos debe ser impar y mayor a 1 \n")
	else:
		print ("\n Se dibuja un rombo de "+str(ancho-ancho/2)+" elementos por lado,")
		print ("de "+str(ancho)+" elementos de ancho y "+str(ancho)+" elementos de alto")
		l=0

		for i in range(ancho):
			n=(ancho/2)-i
			j=0
			k=0			
			if l==0:			
				if n!=0:
					print " "+" "*(n-1)+"#"*(ancho-2*n) 
				else:
					print "#"+"#"*(ancho-2)+"#"
					l=1
			else:
				n=i-ancho/2
				print " "*(n)+"#"*(ancho-2*n)

if opcion==2:
	print ("El numero de elementos debe ser mayor a 1")
	lado=input("Ingresa el numero de elementos por lado para su rombo: ")
	if lado==1:
		print ("El numero de elementos debe ser a 1 \n")
	else:
		print ("\n Se dibuja un rombo de "+str(lado)+" elementos por lado,")
		print ("de "+str(lado+(lado-1))+" elementos de ancho y "+str(lado+(lado-1))+" elementos de alto")
		l=0
		ancho=lado+(lado-1)

		for i in range(ancho):
			n=(ancho/2)-i
			j=0
			k=0			
			if l==0:			
				if n!=0:
					print " "+" "*(n-1)+"#"*(ancho-2*n) 
				else:
					print "#"+"#"*(ancho-2)+"#"
					l=1
			else:
				n=i-ancho/2
print " "*(n)+"#"*(ancho-2*n)
