
print"...Tecnicas de programacion..."
print".........Calculadora..........\n\n"

print"Elige la operacion que desee realizar:\n\n"

print ("Presione 1 para suma: \n ")
print ("Presione 2 para multiplicacion: \n  ")
print ("Presione 3 para la division: \n ")
print ("Presione 4 para la resta: \n ")
print ("Presione 5 para obtener informacion del programa: \n  ")

op = input("Indique la operacion que desea realizar: \n ")

if op == 1:
    print"Suma\n"
    print"Proporcione primer valor"
    a=input("      ")
    print"Proporcione segundo valor"
    b=input("     ")
    c=a+b
    print "El resultado es:  ",c

if op == 2:
    print"Multiplicacion\n"
    print"Proporcione primer valor"
    a=input("      ")
    print"Proporcione segundo valor"
    b=input("     ")
    c=a*b
    print "El resultado es:  ",c

if op == 3:
    print"Division\n"
    print"Proporcione primer valor"
    a=input("      ")
    print"Proporcione segundo valor"
    b=input("     ")
    c=a/b
    print "El resultado es:  ",c
    
if op == 4:
    print"Resta\n"
    print"Proporcione primer valor"
    a=input("      ")
    print"Proporcione segundo valor"
    b=input("     ")
    c=a-b
    print "El resultado es:  ",c

if op == 5:
    print "\n Informacion acerca del programa\n" 

    print "Esta es una calculadora en la cual el usuario puede seleccionar"
    print "entre las operaciones basicas de la misma como:"
    print "Suma, resta, multiplicacion y division de dos numeros cualesquiera."
    print "Este programa solo acepta numero enteros positivos.\n\n"


    print "Universidad Nacional Autonoma de Mexico." 
    print "Facultad de ingenieria UNAM."
if op <=0:
    print "Esta opcion es incorrecta debe ser un numero entero del 1 al 5"
if op >=6:
    print "Esta opcion es incorrecta debe ser un numero entero del 1 al 5"
