class Lavanderia:
    Nombre=""
    Direccion=""
    Personal=""
    costo=None
    
class Ropa:
    color=""
    tipo=""
    tamano=""
    peso=None
    def __init__(self,color,tipo,tamano,peso):
        self.color=color
        self.tipo=tipo
        self.tamano=tamano
        self.peso=peso
class Lavadora(Lavanderia):
    marca=None
    tamano=None
    color=None
    agua=None
    detergente=None
    suavizante=None
    estado="funcional"

    def __init__(self,marca,tamano,color,agua,detergente,suavizante,estado="funcional"):
        self.marca=marca
        self.tamano=tamano
        self.color=color
        self.agua=agua
        self.detergente=detergente
        self.suavizante=suavizante
        self.estado=estado
    def lavar(self):
        print("La lavadora","tiene",str(self.agua),"puede lavar ropa")
    def estado(self):
        print("la lavadora es",str(self.estado))
    def agregar(self):
        print("Por favor agregue",str(self.detergente),"y",str(self.suavizante))

class Secadora(Lavanderia):
    marca=None
    tamano=None
    color=None
    capacidad=None
    estado="Funcional"
    def __init__(self,marca,tamano,color,capacidad,estado="Funcional"):
        self.marca=marca
        self.tamano=tamano
        self.color=color
        self.capacidad=capacidad
        self.estado="Funcional"
    def secado(self):
        print("La secadora",str(self.estado),"puede agregar ropa")
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
    
        
