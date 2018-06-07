class Persona():
  nombre=None
  edad=None
  estatura=None
  
  def __init__(self, nombre, edad, estatura):
    print ("\nCreando persona\n")
    self.nombre=nombre
    self.edad=edad
    self.estatura=estatura
    print("\nPersona: ", str(self))
   
  def __str__(self):
    print (str(self.nombre))
    
class Alumno(Persona):
  asistencia=30
  calificacion=10
  horario=[]
  tareas=[]
  
  def __init__(self, nombre, edad, estatura, horario):
    Persona.__init__(self, nombre, edad, estatura)
    self.tareas=[]
    print ("Alumno creado: ", self, "\n")
    
  def __str__(self):
    print (self.nombre)
    return self.nombre

class Profesor(Persona):
  estacionamiento=False
  sueldo=None
  hambre=False
  
  def __init__(self, nombre, edad, estatura, sueldo=1000):
    self.nombre=nombre
    self.edad=edad
    self.sueldo=sueldo
    
  def tienehambre(self):
    print ("\nEl profesor ", str(self), " tiene hambre")
    
  def __str__(self):
    return self.nombre+" Mecatrónico"  
  
  def asignarTarea(self,Alumno,tipo):
    tarea1=Tareas(Alumno,self,tipo)
    Alumno.tareas.append(tarea1)
    print ("\nTarea asignada\n")
    
  #def asignarCalificacion(self, Alumno, calificación)

class Tareas():
  def __init__(self, Alumno, Profesor, tipo="Programación"):
    self.Alumno=Alumno
    self.Profesor=Profesor
    self.calificacion=0
    self.tipo=tipo
    print ("\nTareas")
    
  def setCalificacion(self,calificacion):
    if calificacion>0 and calificacion<=10:
      self.calificacion=calificacion
    else:
      print("\nError\n")
      
  def imprimirTarea(self):
print("\nLa calificación de ",str(self.Alumno), "sobre ",self.tipo, "asignada por ", str(self.Profesor), "es ", self.calificacion, "\n")
