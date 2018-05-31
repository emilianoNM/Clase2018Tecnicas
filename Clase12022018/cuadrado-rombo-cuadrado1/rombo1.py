#Carracedo Sotelo Eduardo
ancho = int(input("introduce el ancho: "))


for i in range(ancho *2):

    #primer mitad
    if i<=ancho:
        no_espacios = ancho - i
        no_estrellas = i
        print(" "*no_espacios +  "* "*no_estrellas) 

    #segunda mitad
    else:
        no_espacios = i - ancho
        no_estrellas = 2*ancho - i
        print(" "*no_espacios +  "* "*no_estrellas)
