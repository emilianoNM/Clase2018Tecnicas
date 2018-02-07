class Persona():
    nombre=None
    edad=None
    estatura=None
    def __init__(self,nombre, edad,estatura):
        print ("creando Persona")
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        print ("Persona ",str(self))

    def __str__(self):
        print (str(self.nombre))
       
class Alumno(Persona):
        asistencia=30
        calficacion=10
        horario=[]
        tareas=[]
        def __init__(self,nombre,edad,estatura,horario):
           Persona.__init__(self,nombre,edad,estatura)
           print ( "Alumno es ",str(self))
        def __str__(self):
            
            print (self.nombre)
            return self.nombre
class Profesor(Persona):
    estacionamiento= False 
    sueldo=None 
    hambre=False 
    def __init_(self,nombre,edad,estatura,sueldo=1000):
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        self.sueldo=sueldo
    def tieneHambre(self):
        print ("El profesor ",str(self), " tiene hambre")
    def __str__(self):
        return self.nombre+" mecatronico"

