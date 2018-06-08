#Heidi Gomez

import Lavado

Ciclo1 = Lavado.remojado("remojado","1 ciclo","3","Con cloro","Blanco","Blanca")

print("*****Informacion***** \n")
print("Su nombre es: "+Ciclo1.nombre)
print("Tiene una duracion de: "+Ciclo1.duracion)
print("Detergente de lavado: " +Ciclo1.detergente)

Ciclo1.duración='2 ciclos'

print("\nTiene una duracion de: "+Ciclo1.duracion)
