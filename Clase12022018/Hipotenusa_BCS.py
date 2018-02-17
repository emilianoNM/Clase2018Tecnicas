print("Pitagoras\n")
print("Tecnicas de programacion\n")
print("Benjamin Cruz Sarmiento\n")
print("Universidad N2acional Autonoma de Mexico\n")
print("Facultad de ingenieria\n")

#Ingrese los catetos
print("Bienvenido este programa realiza el calculo de la hipotenusa\n")

#Ingrese el valor de los catetos
#variables del tipo flotante
co = input("Ingrese el valor del cateto opuesto\n\n")
ca = input("Ingrese el valor del cateto adyacente\n\n")
#Es para atrapar los posibles errores y el programa no se quiebre
try:
    ca = float(ca)
    co = float(co)
    #Calculo de la hipotenusa
    #**es elevar a una potencia
    hi = (co ** 2 + ca**2) ** (1/2)
    ##El valor de la hipotenusa
    print("El valor de la hipotenusa es:  ", format(hi))
except ValueError:
    print("El dato que ingresaste no es el correcto. Intente de nuevo")
