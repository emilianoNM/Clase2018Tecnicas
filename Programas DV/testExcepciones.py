import Excepciones

try:
  control=Excepciones.modo("control", 12, "no", "no")
except:
  print("\nEste modo es dificil")
finally:
  print("\nSe esta preparando la partida\n")
  
control.gusto()
control.cooperativo()

eliminacion=Excepciones.modo("eliminacion", 6, "si", "si")

eliminacion.gusto()
try:
  eliminacion.cooperativo()
except:
  print("\nEste modo es dificil")
finally:
  print("\nSe esta preparando la partida\n")
  
Caldero=Excepciones.mapa("Caldero", 4, "grande")

Caldero.favorito()
Caldero.atajos()

try:
  Nevada01=Excepciones.Jugador(360,"verde","Nevada01","si")
except:
  print("\nSe perdio la conexion a la sala de juego")
finally:
  print("\nUn jugador intento unirse")
  
try:
  Misipleled=Excepciones.Jugador(800,"Misipleled")
except:
  print("\nSe perdio la conexion a la sala de juego")
finally:
  print("\nUn jugador intento unirse")
  
Nevada01.gesto()
Nevada01.objetivo()

lithium=Excepciones.Jugador(590,"azul","lithium","no")

lithium.ayuda()
