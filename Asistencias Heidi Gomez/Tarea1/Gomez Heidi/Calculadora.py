#Heidi Gomez
#Caluladora
print (" \n **********CALCULADORA********** \n")

print ("Este programa es una caluladora basica, solo tendras opcion de realizar Sumas, Restas, Multiplicaciones y Divisiones\n")
print ("Instrucciones \n" )
print ("Solo puedes introducir dos numeros")
print ("No puedes dividir entre cero")

def Menu():

    """Funcion que Muestra el Menu"""

    print ("""************
Calculadora
************

Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")

def Calculadora():

    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese el primer numero\n"))
        y = int(input("Ingrese el segundo numero\n"))
        if (opc==1):
            print ("La Suma es:", x+y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print ("La Resta es:",x-y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:", x/y)
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Selecione Opcion\n"))
Calculadora()
