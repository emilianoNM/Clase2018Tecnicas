#Programa creado por Mario Molina
import math

print ("")
print ("Calculemos el largo de una hipotenusa a traves de sus catetos")
print ("")
try:
	input = raw_input
except NameError:
	pass

def get_numeric_value(prompt):

	while True:
        	value = input(prompt)
        	if not value:
            		return None
        	try:
            		value = int(value)
        	except ValueError:
			print ("")
            		print("Debe ingresar un valor numerico")
        	else:
            		break
	return value

def main():
	
	catetoa = get_numeric_value("Ingresa el cateto ayacente: ")
	print ("")

	catetob = get_numeric_value("Ingresa el cateto opuesto: ")
	print ("")

	hipotenusa2 = (catetoa**2 + catetob**2)

	hipotenusa = math.sqrt(hipotenusa2)

	print ("El largo de la hipotenusa es: "),hipotenusa
	
	return 0

if __name__ == '__main__':
    main()
