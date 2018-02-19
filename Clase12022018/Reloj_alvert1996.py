#Alberto Garcia Salazar
print ("\nEste programa e dira la hora despues de 'h' horas posterior a la que se introduce")
t=input("dame el numero de minutos de la hora actual: ")
t1=input("dame el numero de horas de la hora actual: ")
h=input("dame un numero de horas ")

if t1>12:
	if t1>24:
		print "\n",t1," no es un numero valido de horas"
	else:
		t2=t1+h
		if t2>24:
			t2=t2-24
			print "\nEn ",h," hora(s) seran las ",t2,":",t," horas"
		else:
			print "\nEn ",h," hora(s) seran las ",t2,":",t," horas"

else:
	t2=t1+h
	if t2>12:
		print "\nEn ",h," hora(s) seran las ",t2,":",t," horas o"
		t2=t2-12
		print "En ",h," hora(s) seran las ",t2,":",t
	else:
		print "\nEn ",h," hora(s) seran las ",t2,":",t
