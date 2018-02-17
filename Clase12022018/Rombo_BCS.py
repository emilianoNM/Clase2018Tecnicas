print("Este programa imprime un rombo.\n")
print("Tecnicas de programacion.\n")
print("Benjamin Cruz Sarmiento.\n")
print("Presione 1 para imprimir el rombo\n")
print("Presione 2 para obtener informacion\n")

#Entrada
a=int(input("Ingrese un numero:\n"))
if a==1:
    #Operacion
    n=int(input("Ingrese el numero de la columna de enmedio"))
    #imprimir un rombo
    for i in range(n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("#",end="")
        print("")
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for k in  range(2*i-1):
            print("#",end="")
        print("")
elif a ==2:
    print("Este programa imprime la figura de un rombo\n")
    print("El usuario debe introducir un numero y debe ser un numero entero\n")
    print("entre 1 y 2  y el numero corresponde al segmento de enmedio.\n")

    print("Universidad Nacional Autonoma de Mexico \n")
    print("Facultad de ingenieria")
else:
    print("Opcion invalida.Ingrese un numero entero entre 1 y 2 ")
    
