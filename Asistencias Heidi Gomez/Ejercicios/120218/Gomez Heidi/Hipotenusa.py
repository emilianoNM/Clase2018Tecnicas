#Laura Gómez
#Calculo de hipotenusa

import math

print("Programa para el calculo de una hipotenusa")
print("\n Instrucciones:")
print("\nDeberá ingresar el valor de los dos catetos")
print("Pueden ser valores con punto decimal")

try:
    
    a=float(input("\nIngrese el valor de un cateto\n"))
    b=float(input("Ingrese el valor del otro cateto\n"))
    c=math.sqrt((a*a+b*b))


    print("El valor de la hipotenusa es: ",str(c))

except ValueError:
    print("El valor o dato de entrada es incorrecto")
