print "1.-SUMA"
print "2.-RESTA"
print "3.-MULTIPLICACION"
print "4.-DIVISION"

opcion = input("Elije una opcion: ")

if opcion == 1:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    resultado = numero1+numero2
    print "El resultado es: ",resultado

if opcion == 2:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    resultado = numero1-numero2
    print "El resultado es: ",resultado

if opcion == 3:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    resultado = numero1*numero2
    print "El resultado es: ",resultado

if opcion == 4:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    resultado = numero1/numero2
    print "El resultado es: ",resultado
