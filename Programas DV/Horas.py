print ("\nEste programa e dira la hora despues de 'h' horas posterior a la que se introduce")
t=input("Dame la hora actual en minutos: ")
t1=input("Dame la hora real: ")
h=input("Dame un numero de hora ")

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
