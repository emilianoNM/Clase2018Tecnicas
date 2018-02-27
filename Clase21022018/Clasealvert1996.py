

#Creamos la clase
class Personas:
	#Creamos el atributo
	nombre=None
	edad=None
	estatura=None
	##Creamos su metodo
	def __init__(self,nombre,edad,estatura):
		print("creando persona")
		self.nombre=nombre
		self.edad=edad
		self.estatura=estatura
		print("Persona",self)
	
	def __str__(self):
		print(self.nombre)


#Creamos un subclase
class Alumno(Personas):
	#Creamos su atributo
	asistencia=30
	calificacion=10
	horario=[]
	tareas=[]
	#creamos su metodo, solo se pone lo que puede ya estar definido como el horario
	def __init__(self,nombre,edad,estatura,horario):
	#Llamamos los atributos de la clase padre con clase._init_(self,nombre,edad,estatura) solo los elementos incluidos en el metodo de la clase padre
		Personas.__init__(self,nombre,edad,estatura)	
		print("alumno es ",self) #imprime en donde esta ubicado alumno "('alumno es ', <Clase.Alumno instance at 0xb70d88cc>)"
		self.tareas=[]  # como tareas es un atributo de la clase general alumno, se crea un self para solo asignarselo a un alumno mandando esa orden a la clase de tareas
	def __str__(self):
		print(self.nombre)
		return self.nombre


class Profesor(Personas):
	#Creamos atributos
	sueldo=None
	hambre=False
	estacionamiento=False
	#Creamos su metodo
	def __init__(self,nombre,edad,estatura,sueldo=1000):
		self.nombre=nombre
		self.edad=edad
		self.estatura=estatura
		self.sueldo=sueldo
	#Creamos otro metodo
	def tienehambre(self):
		print("el profesor "+str(self)+" tiene hambre y tiene "+str(self.edad)+" anos")  #va a convertir en cadena a self
		
	def __str__(self):  #convierte el valor de self a string
		#se puede agregar algo mas del elemento con return self.nombre="algo"
		return self.nombre	#manda a llamar en valor str(self) solo el valor de nombre o algun atributo

	def asignarTarea(self,alumno,tipo):
		tarea1=Tareas(alumno,self,tipo) #self toma el valor de la cadena de la clase donde esta ubicada
		alumno.tareas.append(tarea1)  #append va agregando archivos en forma de lista, se ve si el atributo con dir(clase)		
		print("Tarea Asignada")

class Tareas(Personas):
	#Creamos atributos

	def __init__(self,alumno,profesor,tipo="programacion"):
		self.alumno=alumno
		self.profesor=profesor
		self.calificacion=0
		self.tipo=tipo

	def setCalificacion(self,Calificacion):
		if Calificacion>=0 and Calificacion <=10:
			self.Calificacion=Calificacion
			
		else:
			print("Error calificacion invalida")
	
	def dimeTarea(self):
		print("El alumno: "+str(self.alumno)+" con profesor: "+str(self.profesor)+" realizo la tarea de: "+str(self.tipo)+" y obtuvo una calificacion de: "+str(self.Calificacion))
	
