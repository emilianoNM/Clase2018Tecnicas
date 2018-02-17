print("Este programa imprime un cuadro y un rectangulo.\n")
print("Tecnicas de programacion.\n")
print("Benjamin Cruz Sarmiento.\n")
print("El numero 1 para imprimir un cuadrado o rectangulo.\n")
print("El numero 2 para proporcionar un informacion del programa.\n")

n=int(input("Ingrese su eleccion\n"))

if n==1:

    
    r=int(input("Indique el numero de renglones\n"))
    c=int(input("Indique el numero de columnas\n"))
    
#Se va a utilizar dos ciclos for anidados
#Este maneja los renglones

    for i in range(1,r+1):
        #Este manejas las columnas

        for j in range(1,c+1):
        #Para imprimir la figura.
        #Esto sirve para que python imprima un asterisco tras otro sin saltar de columna
        
            print ("*",end="")
            
        #Este sirve para que cambie de renglon
        print("") 
#Da informacion acerca del programa
elif n==2:
    print("Este programa imprime un cuadrado o un rectangulo segun las dimensiones\n")
    print("que el usuario le ingrese y unicamente deben de ser numeros enteros.\n")
    print("Universidad Nacional Autonoma de Mexico\n")
    print("Facultad de ingenieria")

else:
    print("Esta opcion no es valida debe elegir 1 o 2")
