#Hernández Alvarado Miguel Kam Yaxkin

class Inventario:
  Marca=None
  Disponible=None
  Mantenimiento=None
  
class Lavadora1(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Lava(self):
    print("\nLa primera lavadora, de marca ", str(self), " es eficaz para lavar")
    
  def Tiembla(self):
    print("\nA pesar de ser de la marca ",str(self), " vibra demasiado")
    
  def Seca(self):
    print("\nLa lavadora ", str(self), " incluye ciclo de secado")
     
class Lavadora2(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Fuga(self):
    print("\nLa máquina de marca ", str(self), " tiene una fuga en la compuerta")
    
  def Lava(self):
    print("\nA pesar de su estado, la lavadora ", str(self), " hace su trabajo")
    
  def Ruido(self):
    print("\nLa unidad ", str(self), " es curiosamente silenciosa")
      
class Secadora1(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Seca(self):
    print("\nLa máquina ", str(self), " sólo funcina como secadora")
    
  def Calienta(self):
    print("\nEste modelo de secadora de marca ", str(self), " se calienta con electricidad")
    
  def Completa(self):
    print("\nLa unidad ", str(self), " puede terminar en 20 minutos")
      
class Secadora2(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Enciende(self):
    print("\nHay un truco para encender la secadora ", str(self))
    
  def Abre(self):
    print("\nTambién hay un truco para abrir la secadora", str(self))
    
  def Contiene(self):
    print("\nLa unidad ", str(self), " tiene poca capacidad de carga")
      
class Plancha1(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Trabaja(self):
    print("\nLa mayoria de clientes usa la plancha", str(self))
    
  def Vaporiza(self):
    print("\nEl primer boton de la plancha ", str(self), " es para el vapor")
    
  def Almacena(self):
    print("\nLa plancha", str(self), " no almacena mucha agua")
      
class Vaporizador(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Ruido(self):
    print("\nEl vaporizador de ", str(self), " hace mucho ruido")
    
  def Vapor(self):
    print("\nSiendo un vaporizador de ", str(self), " no sabemos que tanto vapor genera")
    
  def Quema(self):
    print("\nEl vaporizador de ", str(self), " puede quemar la mano del usuario")
      
class Plancha2(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Enciende(self):
    print("\nPara encender la plancha  ", str(self), " simplemente se conecta")
    
  def Cae(self):
    print("\nDEido a una caida, la plancha", str(self), " tiene una carcasa suelta")
    
  def Salpica(self):
    print("\nAl usar la plancha", str(self), " tener en cuenta que salpica mas que vaporizar")
      
class Contenedor1(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Entrega(self):
    print("\nEl primer contenedor entrega", str(self),)
    
  def Sella(self):
    print("\nLa válvula del contenedor de ", str(self), " funciona bastante bién")
    
  def Recarga(self):
    print("\nEl contenedor de", str(self), " es recargado cada semana")
      
class Contenedor2(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Entrega(self):
    print("\nLa porción de ", str(self), " que este contenedor entrga es irregular")
    
  def Fuga(self):
    print("\nEl contenedor de", str(self), " presenta un par de fugas")
    
  def Limpieza(self):
    print("\nEl dispensador de ", str(self), " requiere limpieza")
      
class Contenedor3(Inventario):
  def __init__(self, Marca, Disponible, Mantenimiento):
    self.Disponible=Disponible
    self.Marca=Marca
    self.Mantenimiento=Mantenimiento
    
  def __str__(self):
    return self.Marca
  
  def Aroma(self):
    print("\nEl ", str(self), " tiene un aroma discreto")
    
  def Recarga(self):
    print("\nEl contenedor de ", str(self), " se recarga cada dos semanas")
    
  def Pulveriza(self):
    print("\nPara aplicar ", str(self), " sólo hay que pulverizar un par de veces")