print ("Calculadora basica")
num1=int(input("Escribe el primer numero: "))
op=input("Operacion: 1 para +, 2 para -, 3 para *, 4 para /")
num2=int(input("Escribe el segundo numero: "))

if op==1:
	res=num1+num2
	print(res)
else:
	pass

if op==2:
	res=num1-num2
	print(res)
else:
	pass

if op==3:
	res=num1*num2
	print(res)
else:
	pass

if op==4:
	res=num1/num2
	print(res)
else:
	pass
