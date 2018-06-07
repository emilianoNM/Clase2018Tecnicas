print ("DIBUJO DE UN CUADRADO")
lado=input("\n Dame la longitud de un lado del cuadrado: ")
mode=input("\n Presiona 1 para dibujar el contorno o 2 para dibujarlo solido: ")
print ""

if mode==1:
	for i in range(lado):
		if i==0 or i==lado-1:
			print "D "*(lado)
		else: 
			print "D "+"  "*(lado-2)+"D"
	i=0

if mode==2:
	for i in range(lado):
		print "D "*(lado)
	i=0
print ""
