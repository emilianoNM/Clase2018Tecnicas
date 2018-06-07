print ("DIBUJAR UN CIRCULO")
mode=input("\n Presiona 1 para dibujar por radio o 2 para dibujar con diametro: ")
if mode==1:
	radio=input("\n Dame el valor del radio: ")
	diametro=radio*2
if mode==2:
	diametro=input("\n Dame el valor del diametro: ")

dibuja=input("\n Presiona 1 para dibujar el contorno o 2 para dibujar un circulo solido: ")
print ""
if mode==1:
	for i in range(diametro):
		if i==0 or i==diametro-1:
			print "  "+"o "*(diametro-2)
		else: 
			print "o "+"  "*(diametro-2)+"o "
	i=0

if mode==2:
	for i in range(diametro):
		if i==0 or i==diametro-1:
			print "  "+"o "*(diametro-2)
		else:
			print "o "*(diametro)
	i=0
print ""
