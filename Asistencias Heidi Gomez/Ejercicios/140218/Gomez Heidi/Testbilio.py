#Heidi Gomez

import Biblioteca

Libro = Biblioteca.Novelas("Carlos Fuentes","Trillas","E3","Aura","87","Mexico")

print("*****Informacion***** \n")
print("El autor es: "+Libro.autor)
print("La editorial es: "+Libro.editorial)
print("Se encuentra en el pasillo :" +Libro.pasillo)
      

Libro.pasillo="E4"

print("Se encuentra en el pasillo :" +Libro.pasillo)
      
