print ("Calculadora")
print("Escoge una accion")
print("1 = suma")
print("2 = resta")
print("3 = multiplicacion")
print("4 = division")
opcion=input("Accion: ")

if opcion ==1:
    numero1 = input("Introduce un valor: ")
    numero2 = input("Introduce un segundo valor a sumar: ")
    resultado = numero1+numero2
    print "El resultado es: ",resultado

if opcion ==2:
    numero1 = input("Introduce el primer valor: ")
    numero2 = input("Introduce lo que se va a restar: ")
    resultado = numero1-numero2
    print "El resultado es: ",resultado

if opcion ==3:
    numero1 = input("Introduce el primer valor a multiplicar: ")
    numero2 = input("Introduce el segundo valor: ")
    resultado = numero1*numero2
    print "El resultado es: ",resultado

if opcion ==4:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo valor que dividira: ")
    resultado = numero1/numero2
    print "El resultado es: ",resultado
