class Jugador():
  def __init__(self, puntuacion, equipo, nombre, coopera="no"):
    self.puntuacion=puntuacion
    self.equipo=equipo
    self.nombre=nombre
    self.coopera=coopera
    print (str(self))
    
  def __str__(self):
    return self.nombre+" se unio a la sala de juego"
    
  def gesto(self):
    print ("\n", self.nombre, " saluda")
    
  def objetivo(self):
    print("\nEl equipo", self.equipo, "juega el objetivo")
    
  def ayuda(self):
    if self.coopera=="no":
      print("\nEl jugador ha sido bloqueado\n")
      raise Bloqueo()
    
      
    
class mapa():
  def __init__(self,lugar,habitaciones, size):
    self.lugar=lugar
    self.habitaciones=habitaciones
    self.size=size
    print("\nSe esta cargando el mapa ", str(self))
    
  def __str__(self):
    return self.lugar
    
  def favorito(self):
    if self.size=="grande":
      print("\n", self.lugar, " es un mapa muy grande")
      print(Derrota)
    else:
      pass
    
  def atajos(self):
    print("\nEl otro equipo no conoce todas las entradas\n")


      
class modo():
  def __init__(self, tipo, vacantes, competitivo, popular):
    self.tipo=tipo
    self.vacantes=vacantes
    self.competitivo=competitivo
    self.popular=popular
    print("\nSe esta cargando el modo",str(self))
    
  def __str__(self):
    return  self.tipo
    
  def gusto(self):
    if self.competitivo=="si":
      print("\nLa comunidad odia el modo ", self.tipo)
    elif self.competitivo=="no":
      print("\nLa comunidad es indiferente al modo ", self.tipo)
	
  def cooperativo(self):
    if self.popular=="no":
      print("\nNo hay individualismos en el equipo\n")
    else:
      raise Enojo()
    
class Enojo(Exception):
  pass

class Derrota(Exception):
  pass

class Bloqueo(Exception):
  pass

