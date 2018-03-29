#Benajamin Cruz Sarmiento

class Persona():
    nombre=None
    edad = None
    estatura=None
    def __init__(self,nombre,edad,estatura):
        print("Creando Persona")
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        print("Persona",str(self))

    def __str__(self):
            print(str(self.nombre))
	
class Alumno(Persona):
        asistencia=30
        calificacion=10
        horario=[]
        tareas=[]
        def __init__(self,nombre,edad,estatura,horario):
           Persona.__init__(self,nombre,edad,estatura)
           self.tareas=[]
           print("Alumno es ",str(self))
        def __str__(self):

  #          print(self.nombre)
            return self.nombre
        
class Profesor(Persona):
    estacionamiento=False
    sueldo=None
    hambre=False
    def __init__(self,nombre,edad,estatura,sueldo=1000):
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        self.sueldo=sueldo
    def tieneHambre(self):
        print("El profesor",str(self.nombre),"tiene hambre")

        
    def __str__(self):
        return self.nombre + " mecatronico"
    def asignarTarea(self,alumno,tipo):
        tarea1=Tareas(alumno,self,tipo)
        alumno.tareas.append(tarea1)
        
        print("tarea asignada")
   
#Composicion
#tareas

class Tareas():
#constructor y adentro a lo que se le adjudica
    def __init__(self,alumno,profesor,tipo="Programacion"):
        self.alumno=alumno
        self.profesor=profesor
        self.calificacion = 0
        self.tipo=tipo
        print("Tarea")

    def setCalificacion(self,calificacion):
        if calificacion >= 0 and calificacion <=10:
            self.calificacion = calificacion


        else:
            print("Error calificacion invalida")

    def imprimirTarea(self):


	print("")
	print("")
	print("$$$$$$$$$$$$$$$ Tarea $$$$$$$$$$$$$$")
	print("")
	print("El profesor: "+str(self.profesor))
	print("Dejo una tarea al alumno: "+str(self.alumno))
	print("Sobre: "+str(self.tipo))
	print("En la cual obtuvo: "+str(self.calificacion))

