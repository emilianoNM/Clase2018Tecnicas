print("Cuadro en ASCII")

a = int (input("dimension de los lados"))
x = int (input("ASCII"))
if a<20:
 for i in range (1,a+1):
	for j in range (1,1+a):
		n=chr(x)
		print n,

	print " "
else:
    print "Dimension muy grande"