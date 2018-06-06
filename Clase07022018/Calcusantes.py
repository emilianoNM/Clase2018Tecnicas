# Santes Mejia Antonio
print(" Tecnicas de programcaion")
print("Presiona A para suma:")
print("Presiona B para la division:")
print("Prsiona C para la multiplicacion")
print("Presione D para la resta")

op=input('Indique la operacion que desea realizar;')

if opcion=="A":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    suma= a+b
    print ("El resultado es:", suma)
if opcion=="B":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    div=a/b
    print ("El resultado es:",div)

if opcion=="C":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    mult=a*b
    print ("El resultado es:",mult)
if opcion=="D":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    resta=a-b
    print ("El resultado es:",resta)

