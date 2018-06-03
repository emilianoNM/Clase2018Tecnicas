print("Bienvenido a la calculadora, las opciones son las sigueientes")
print("\n(a) Para sumar\n")
print("\n(b) Para restar\n")
print("\n(c) Para multiplicar\n")
print("\n(d) Para dividir\n")

opcion=input('Elija una opción')

if opcion=="a":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    suma= a+b
    print ("El resultado es:", suma)
if opcion=="b":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    resta=a-b
    print ("El resultado es:",resta)
if opcion=="c":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    mult=a*b
    print ("El resultado es:",mult)
if opcion=="d":
    a=float(input("Ingrese un numero"))
    b=float(input("Ingrese un numero"))
    div=a/b
    print ("El resultado es:",div)
