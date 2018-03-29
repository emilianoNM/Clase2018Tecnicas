#Benjamin Cruz Sarmiento

class Zoo():

	Animal=None
	Edad=None
	Tamano=None
	Sexo=None
	Peso=None

class Animal(Zoo):
	Temperatura=None
	Ubicacion=None
	Clima=None
	Comida=None
	Agresividad=None
	Dias=None
	Hora=None
	Cantidad=None

	def __init__(self,Animal,Edad,Tamano,Sexo,Peso,Temperatura,Ubicacion,Clima,Comida,Agresividad,Dias,Hora,Cantidad):
	
		self.Animal=Animal
		self.Edad=Edad
		self.Tamano=Tamano
		self.Sexo=Sexo
		self.Peso=Peso
		self.Temperatura=Temperatura
		self.Ubicacion=Ubicacion
		self.Clima=Clima
		self.Comida=Comida
		self.Agresividad=Agresividad
		self.Dias=Dias
		self.Hora=Hora
		self.Cantidad=Cantidad


	def Info(self):
			
		print("Informacion sobre este animal: ")
		print("")
		print("Animal: "+str(self.Animal))
		print("Edad: "+str(self.Edad)+" anos")
		print("Tamano: "+str(self.Tamano)+" centimetros")
		print("Genero: "+str(self.Sexo))
		print("Peso: "+str(self.Peso)+" Kilogramos")
		print("Nivel de agresividad: "+str(self.Agresividad))
		print("Ejemplares en el zoologico: "+str(self.Cantidad))
		print("")
		

	def Horario(self):
		print("Horario del zoologico: ")
		print("")
		print("Dias: "+str(self.Dias))
		print("Hora: "+str(self.Hora))
		print("")

	def Habitat(self):

		print("Caracteristicas de su habitat")
		print("")
		print("Ubicacion natural: "+str(self.Ubicacion))
		print("Clima: "+str(self.Clima))
		print("Temperatura: "+str(self.Temperatura)+" Grados Celcius")
		print("Comida favorita: "+str(self.Comida))
		print("")









