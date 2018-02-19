#Albrto Garcia Salazar
print ("Vamos a dibujar un circulo")
mode=input("\n Presiona 1 para dibujar por sus elementos en radio o 2 para dibujarlo con diametro: ")
if mode==1:
	radio=input("\n Dame el valor de elementos de radio: ")
	diametro=radio*2
if mode==2:
	diametro=input("\n Dame el valor de elementos de diametro: ")

dibuja=input("\n Presiona 1 para dibujar el contorno o 2 para dibujarlo solido: ")
print ""
if mode==1:
	for i in range(diametro):
		if i==0 or i==diametro-1:
			print "  "+"# "*(diametro-2)
		else: 
			print "# "+"  "*(diametro-2)+"# "
	i=0

if mode==2:
	for i in range(diametro):
		if i==0 or i==diametro-1:
			print "  "+"# "*(diametro-2)
		else:
			print "# "*(diametro)
	i=0
print ""
