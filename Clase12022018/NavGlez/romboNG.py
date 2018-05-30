n = int(input('introduce la mitad del D mayor: '))
x = int(input('ASCII'))
if n<20:
 for i in range(n+1):
 	for j in range (n-i):
 		print(" ", end="")
 	for k in range(2*i-1):
 		s=chr(x)
 		print (s ,end="")
 	print("")
 for i in range(n-1,0,-1):
 	for j in range (n-i):
 		print(" ", end="")
 	for k in range (2*i-1):
 		print (s,end="")
 	print("")
else:
	print ("Dimension muy grande")
