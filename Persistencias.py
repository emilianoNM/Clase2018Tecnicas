#Eduardo Daniel Batta González
#Clase utilizada: Personas

import pickle


class Persona():
  Nombre=None
  Edad=None
  sexo=None
  Altura= None

class Daniel(Persona):

    
  def __init__(self, Nombre, Edad, sexo, Altura):
    self.Nombre=Nombre
    self.Edad=Edad
    self.sexo=sexo
    self.Altura=Altura
    
  def Save(self, archivo):
    fichero=file("datos.dat","w")
    fichero.close()
    
  def Load(self, archivo):
      fichero=file("datos.dat","r")
      fichero.close()

  
class Mauricio(Persona):

    
  def __init__(self, Nombre, Edad, sexo, Altura):
    self.Nombre=Nombre
    self.Edad=Edad
    self.sexo=sexo
    self.Altura=Altura
    
  def Save(self, archivo):
    fichero=file("datos1.dat","w")
    fichero.close()
    
  def Load(self, archivo):
      fichero=file("datos1.dat","r")
      fichero.close()

class Eduardo(Persona):

    
  def __init__(self, Nombre, Edad, sexo, Altura):
    self.Nombre=Nombre
    self.Edad=Edad
    self.sexo=sexo
    self.Altura=Altura
    
  def Save(self, archivo):
    fichero=file("datos2.dat","w")
    fichero.close()
    
  def Load(self, archivo):
      fichero=file("datos2.dat","r")
      fichero.close(
