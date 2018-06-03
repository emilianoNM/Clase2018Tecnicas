#hernandez quintana luis eduaardo
class Persona:
	
	Nombre=None
	edad=None
	estatura=None

	
	def __init__(self,nombre,edad,estatura):
		print("\ncreando persona")
		self.nombre=nombre
		self.edad=edad
		self.estatura=estatura
		print("\nPersona",self)
	
	def __str__(self):
		print(self.nombre)



class Alumno(Persona):
	
	asistencia=30
	calificacion=10
	horario=[]
	tareas=[]

    
	def __init__(self,nombre,edad,estatura,horario):
	
		Personas.__init__(self,nombre,edad,estatura)	
		print("alumno es ",self)
		self.tareas=[]

		
	def __str__(self):
		print(self.nombre)
		return self.nombre


class Profesor(Personas):
	sueldo=None
	estacionamiento=False
	hambre=False
	
	
	def __init__(self,nombre,edad,estatura,sueldo=1000):
		self.nombre=nombre
		self.edad=edad
		self.estatura=estatura
		self.sueldo=sueldo
	
	def tienehambre(self):
		print("el profesor "+str(self)+" tiene hambre y tiene "+str(self.edad)+" anos")  #va a convertir en cadena a self
		
	def __str__(self):

            return self.nombre+" Mecatrónico" 
        
	def asignarTarea(self,alumno,tipo):
		tarea1=Tareas(alumno,self,tipo)
		alumno.tareas.append(tarea1)
		print("\nTarea Asignada\n")

class Tareas(Personas):
	

	def __init__(self,alumno,profesor,tipo="programacion"):
		self.alumno=alumno
		self.profesor=profesor
		self.calificacion=0
		self.tipo=tipo
		print ("\nTareas")

	def setCalificacion(self,Calificacion):
		if Calificacion>=0 and Calificacion <=10:
			self.Calificacion=Calificacion
			
		else:
			print("Error calificacion invalida")
	
	def sesimprimetarea(self):
		print("El alumno: "+str(self.alumno)+" con profesor: "+str(self.profesor)+" realizo la tarea de: "+str(self.tipo)+" y obtuvo una calificacion de: "+str(self.Calificacion))
