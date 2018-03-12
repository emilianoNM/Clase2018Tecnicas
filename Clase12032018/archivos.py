#Escrbir en un archivo 
File=open("archivo.txt","w")
File2=open("archivo2.txt","a")
print File 

File.write("Hola Mundo \n")
File.writelines("linea 1 \n")
File.writelines("linea 2 \n")
File2.write("Segundo archivo")

File.close()
File.close()

#Diferentes metodos de escritura 
print(dir(File))

#Leer en un archivo 
archivo=open("archivo.txt","r")


#for  linea in archivo:
#  print linea 

#print archivo.read(3)

listaDeLineas= archivo.readlines()

print listaDeLineas

archivo.close()

#Diferentes Metodos de Lectura 

