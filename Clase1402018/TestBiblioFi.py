###Programa creado por Mario Molina
# -*- coding: Windows-1252 -*-
 
import sys
print sys.stdout.encoding


import BiblioFi

print("")

Libro1=BiblioFi.Libros()
Libro1.Nombre="It"
Libro1.Prestamo="Disponible"
Libro1.Tipo="Horror"
print ("Libro consultado: " + Libro1.Nombre)
print ("Género: " + Libro1.Tipo)
print ("Disponibilidad para prestamo: " + Libro1.Prestamo)

print("")

Libro2=BiblioFi.Libros()
Libro2.Nombre="Cien años de soledad"
Libro2.Prestamo="Disponible"
Libro2.Tipo="Realismo mágico"
print ("Libro consultado: " + Libro2.Nombre)
print ("Género: " + Libro2.Tipo)
print ("Disponibilidad para prestamo: " + Libro2.Prestamo)

print("")

Libro3=BiblioFi.Libros()
Libro3.Nombre="Ensayo sobre la ceguera"
Libro3.Prestamo="No disponible"
Libro3.Tipo="Novela"
print ("Libro consultado: " + Libro3.Nombre)
print ("Género: " + Libro3.Tipo)
print ("Disponibilidad para prestamo: " + Libro3.Prestamo)


print("")

Libro4=BiblioFi.Libros()
Libro4.Nombre="El nombre de la rosa"
Libro4.Prestamo="No disponible"
Libro4.Tipo="Novela"
print ("Libro consultado: " + Libro4.Nombre)
print ("Género: " + Libro4.Tipo)
print ("Disponibilidad para prestamo: " + Libro4.Prestamo)

print("")

Libro5=BiblioFi.Libros()
Libro5.Nombre="Crimen y castigo"
Libro5.Prestamo="Disponible"
Libro5.Tipo="Drama"
print ("Libro consultado: " + Libro5.Nombre)
print ("Género: " + Libro5.Tipo)
print ("Disponibilidad para prestamo: " + Libro5.Prestamo)

print("")

Libro6=BiblioFi.Libros()
Libro6.Nombre="El amante"
Libro6.Prestamo="No disponible"
Libro6.Tipo="Erotismo"
print ("Libro consultado: " + Libro6.Nombre)
print ("Género: " + Libro6.Tipo)
print ("Disponibilidad para prestamo: " + Libro6.Prestamo)

print("")

Libro7=BiblioFi.Libros()
Libro7.Nombre="La guerra de los mundos"
Libro7.Prestamo="Disponible"
Libro7.Tipo="Ciencia ficción"
print ("Libro consultado: " + Libro7.Nombre)
print ("Género: " + Libro7.Tipo)
print ("Disponibilidad para prestamo: " + Libro7.Prestamo)

print("")

Libro8=BiblioFi.Libros()
Libro8.Nombre="A sangre fría"
Libro8.Prestamo="Disponible"
Libro8.Tipo="Novela"
print ("Libro consultado: " + Libro8.Nombre)
print ("Género: " + Libro8.Tipo)
print ("Disponibilidad para prestamo: " + Libro8.Prestamo)

print("")

Libro9=BiblioFi.Libros()
Libro9.Nombre="La sonrisa de Mandela"
Libro9.Prestamo="No disponible"
Libro9.Tipo="Biografía"
print ("Libro consultado: " + Libro9.Nombre)
print ("Género: " + Libro9.Tipo)
print ("Disponibilidad para prestamo: " + Libro9.Prestamo)

print("")

Libro10=BiblioFi.Libros()
Libro10.Nombre="Gerónimo de Stilton"
Libro10.Prestamo="Disponible"
Libro10.Tipo="Infantil"
print ("Libro consultado: " + Libro10.Nombre)
print ("Género: " + Libro10.Tipo)
print ("Disponibilidad para prestamo: " + Libro10.Prestamo)
