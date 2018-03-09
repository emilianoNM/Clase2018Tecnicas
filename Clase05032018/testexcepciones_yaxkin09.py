import excepciones_yaxkin09

try:
  control=excepciones_yaxkin09.modo("control", 12, "no", "no")
except:
  print("\nEste modo es dificil")
finally:
  print("\nSe esta preparando la partida\n")
  
control.gusto()
control.cooperativo()

eliminacion=excepciones_yaxkin09.modo("eliminacion", 6, "si", "si")

eliminacion.gusto()
try:
  eliminacion.cooperativo()
except:
  print("\nEste modo es dificil")
finally:
  print("\nSe esta preparando la partida\n")
  
Caldero=excepciones_yaxkin09.mapa("Caldero", 4, "grande")

Caldero.favorito()
Caldero.atajos()

try:
  SuperPro52=excepciones_yaxkin09.Jugador(400,"Azul","SuperPro52","si")
except:
  print("\nSe perdio la conexion a la sala de juego")
finally:
  print("\nUn jugador intento unirse")
  
try:
  Misipleled=excepciones_yaxkin09.Jugador(800,"Misipleled")
except:
  print("\nSe perdio la conexion a la sala de juego")
finally:
  print("\nUn jugador intento unirse")
  
SuperPro52.gesto()
SuperPro52.objetivo()

xX_DarkShadow_Xx=excepciones_yaxkin09.Jugador(650,"Rojo","xX_DarkShadow_Xx","no")

xX_DarkShadow_Xx.ayuda()