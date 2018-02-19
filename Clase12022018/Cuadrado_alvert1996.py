#Albrto Garcia Salazar
print ("Vamos a dibujar un cuadrado")
lado=input("\n Dame el valorde elementos por lado: ")
mode=input("\n Presiona 1 para dibujar el contorno o 2 para dibujarlo solido: ")
print ""

if mode==1:
	for i in range(lado):
		if i==0 or i==lado-1:
			print "# "*(lado)
		else: 
			print "# "+"  "*(lado-2)+"#"
	i=0

if mode==2:
	for i in range(lado):
		print "# "*(lado)
	i=0
print ""
