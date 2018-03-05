print ("Palindromo\n")
print ("Tecnicas de programacion\n")
print ("Este programa le dice si una secuencia de numeros, frase o palabra\n")
print ("es palindroma o no, osea, que significa lo mismo si se lee de\n ")
print ("derecha a izquierda y viceversa\n")

palabra1 = raw_input("Ingrese la palabra\n\n")

#.lower hace que todas las letras se hagan minuculas
#.replace quita los espacio y junta la frase
palabra1 = palabra1.lower().replace(' ','')

#invirte la palabra con [::-1]
palabra2 = palabra1[::-1]



if palabra2 == palabra1:
    print "La frase que ingreso es palindroma"


else:
    print"La frase que ingreso no es palindroma"


