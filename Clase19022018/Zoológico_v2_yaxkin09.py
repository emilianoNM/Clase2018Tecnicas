#Hernández Alvarado Miguel Kam Yaxkin

class Especie:
  Nombre=None
  Habitad=None
  Edad=None
  
class Lince(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Duerme(self):
    print("\nUn lince de nombre", str(self), " esta durmiendo")
    
  def Oculta(self):
    print("\n",str(self), " asecha")
    
  def Salta(self):
    print("\nDesde un arbol ", str(self), " salta hacia aca")
     
class Zorro(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Excavar(self):
    print("\n", str(self), " excava demasiados hoyos")
    
  def Olfatear(self):
    print("\n", str(self), " olfatea algo")
    
  def Jugar(self):
    print("\n", str(self), " juega con las piedras")
      
class Pingüino(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Nada(self):
    print("\n", str(self), " caza en el agua")
    
  def Tropieza(self):
    print("\n", str(self), " suele tropezar al caminar")
    
  def Desliza(self):
    print("\nObservad cuando ", str(self), " se deslice")
      
class Murcielago(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Duerme(self):
    print("\nPor ahora ", str(self), " duerme")
    
  def Escucha(self):
    print("\n", str(self), " busca una presa")
    
  def Vuela(self):
    print("\nSobre nuestras cabezas ", str(self), " vuela")
      
class Condor(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Reposa(self):
    print("\n", str(self), " reposa frente a nosotros")
    
  def Observa(self):
    print("\Desde al aire ", str(self), " vigila")
    
  def Vuela(self):
    print("\n", str(self), " vuela hacia un terreno alto")
      
class Puma(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Oculta(self):
    print("\n", str(self), " se oculta cerca")
    
  def Trepa(self):
    print("\nPor estas rocas", str(self), " suele trepar")
    
  def Salta(self):
    print("\nSobre nosotros ", str(self), " salta")
      
class Lobo(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Guia(self):
    print("\nAquel lobo de nombre ", str(self), " es el lider")
    
  def Olfatea(self):
    print("\n", str(self), " revisa su alimento")
    
  def Corre(self):
    print("\n", str(self), " correrá hacia los arboles")
      
class Pulpo(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Imita(self):
    print("\nAquella estrella de mar es ", str(self), ", es un pulpo")
    
  def Escapa(self):
    print("\n", str(self), " dejo esta nube de tinta")
    
  def Sujeta(self):
    print("\n", str(self), " no soltará tu mano")
      
class Tortuga(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Duerme(self):
    print("\nNo lo parece, pero ", str(self), " esta durmiendo")
    
  def Come(self):
    print("\n", str(self), " recibe fruta para comer")
    
  def Muerde(self):
    print("\n", str(self), " no muerde")
      
class Tarantula(Especie):
  def __init__(self, Nombre, Habitad, Edad):
    self.Habitad=Habitad
    self.Nombre=Nombre
    self.Edad=Edad
    
  def __str__(self):
    return self.Nombre
  
  def Construye(self):
    print("\nLa especie a la que pertenece ", str(self), " construye trampas en el suelo")
    
  def Mueve(self):
    print("\n", str(self), " no se moverá mucho")
    
  def Caza(self):
    print("\n", str(self), " sólo caza de noche")