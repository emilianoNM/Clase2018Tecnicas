import pickle


class Especie:
  Nombre=None
  Habitad=None
  Edad=None

class Lince(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def Save(self, archivo):
    storage=file(archivo,"w")
    pickle.dump(Lince,storage)
    storage.close()
    
  def Load(self, archivo):
    storage=file(archivo,"r")
    Lince=pickle.load(storage)
    print("Nombre: ", self.Nombre, "Habitad: ",self.Habitad,"Edad: ",self.Edad)
    storage.close()
  
class Zorro(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def Save(self, archivo):
    storage=file(archivo,"w")
    pickle.dump(Zorro,storage)
    storage.close()
    
  def Load(self, archivo):
    storage=file(archivo,"r")
    Zorro=pickle.load(storage)
    print("Nombre: ", self.Nombre, "Habitad: ",self.Habitad,"Edad: ",self.Edad)
    storage.close()
  
class Pinguino(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def Save(self, archivo):
    storage=file(archivo,"w")
    pickle.dump(Pinguino,storage)
    storage.close()
    
  def Load(self, archivo):
    storage=file(archivo,"r")
    Pinguino=pickle.load(storage)
    print("Nombre: ", self.Nombre, "Habitad: ",self.Habitad,"Edad: ",self.Edad)
    storage.close()