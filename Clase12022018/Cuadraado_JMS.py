#Meneses Silva Maximino Javier
print("Este programa imprime un Cuadrado LxL")
print ("")
largo=int(input("ingresa el valor de L: "))
ancho=int(input("ingresa el valor de L: "))

if largo==ancho:
 print("Elegiste dibujar un cuadrado de %d x %d:"%(largo,ancho))
 for a in range (1,ancho+1):
     for b in range (1, largo +1):
         print(" # ",end="")
     print("")    

else:
 print(" Los datos ingresados no corresponden a un cuadrado,es un rectangulo") 
 for a in range (1,ancho+1):
     for b in range (1, largo +1):
         print(" @ ",end="")
     print("")
