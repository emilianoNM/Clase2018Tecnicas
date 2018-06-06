# Santes Mejia Antonio
print "...Tecnicas de programacion.."


import pickle
class Ventas():
 Nombre=None
  Marca=None
  Modelo=None
  Precio= None

class Aveo(Ventas):
  def __init__(self, Nombre, Marca, Modelo, Precio):
    self.Nombre=Nombre
    self.Marca=Marca
    self.Modelo=Modelo
    self.Precio=Precio
  def Save(self, archivo):
    SAM=file("datos.dat","a")
    SAM.close()  
  def Load(self, archivo):
      SAM=file("datos.dat","r")
      SAM.close()


class Versa(Ventas):  
  def __init__(self, Nombre, Marca, Modelo, Precio):
    self.Nombre=Nombre
    self.Marca=Marca
    self.Modelo=Modelo
    self.Precio=Precio
  def Save(self, archivo):
    SAM2=file("datos.dat","a")
    SAM2.close()
  def Load(self, archivo):
      SAM2=file("datos.dat","r")
      SAM2.close()

class Vento(Ventas):  
  def __init__(self, Nombre, Marca, Modelo, Precio):
    self.Nombre=Nombre
    self.Marca=Marca
    self.Modelo=Modelo
    self.Precio=Precio
  def Save(self, archivo):
    SAM3=file("datos.dat","a")
    SAM3.close()
  def Load(self, archivo):
      SAM3=file("datos.dat","r")
      SAM3.close()

    

    

    
  

