#Batta Gonzalez Eduardo Daniel

class Lavanderia:
    Nombre=""
    Direccion=""
    Personal=""
    costo=None
    
class Ropa:
    color=""
    tipo=""
    tamano=None
    peso=None
    def __init__(self,color,tipo,tamanio,peso):
        self.color=color
        self.tipo=tipo
        self.tamanio=tamanio
        self.peso=peso
class Lavadora(Lavanderia):
    marca=None
    tamanio=None
    color=None
    agua=None
    detergente=None
    suavizante=None
    estado="activa"

    def __init__(self,marca,tamano,color,agua,detergente,suavizante,estado="activa"):
        self.marca=marca
        self.tamano=tamano
        self.color=color
        self.agua=agua
        self.detergente=detergente
        self.suavizante=suavizante
        self.estado=estado
    def lavar(self):
        print("La lavadora","tiene",str(self.agua),"puede lavar")
    def estado(self):
        print("la lavadora esta",str(self.estado))
    def agregar(self):
        print("Por favor agregue",str(self.detergente),"y",str(self.suavizante))
    def encender(self):
        print("La lavadora esta lista para usarse")
class Secadora(Lavanderia):
    marca=None
    tamano=None
    color=None
    capacidad=None
    estado="activa"
    def __init__(self,marca,tamanio,color,capacidad,estado="activa"):
        self.marca=marca
        self.tamanio=tamanio
        self.color=color
        self.capacidad=capacidad
        self.estado="activa"
    def secado(self):
        print("La secadora",str(self.estado),"puede comenzar a trabajar")
    def encendido(self):
        print("Encienda la secadora")
    def detener(self):
        print("Se ha terminado de secar la ropa")

class Plancha(Lavanderia):
    marca=None
    tamano=None
    temperatura=None
    estado="Funcional"
    def __init__(self,marca,tamano,temperatura,estado="Funcional"):
        self.marca=marca
        self.tamano=tamano
        self.temperatura=temperatura
        self.estado="Funcional"
    def encendido(self):
        print("La plancha esta encendida",str(self.estado))
    def planchado(self):
        print("la temperatura de la plancha",str(self.temperatura),"es optima para planchar")

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
