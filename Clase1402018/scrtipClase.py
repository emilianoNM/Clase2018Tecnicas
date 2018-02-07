#Funciones

def  fib(n=-1):
     	if n<0:
		print (" n ,No puede ser negativo")
		pass
	a, b = 0,1
	while a < n :
	  print (a, ' ')
	  a, b = b, a+b
      	print() 


