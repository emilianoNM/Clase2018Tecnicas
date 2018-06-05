class Personal:
	nombre = []
	estatura = None
	edad = None
	puesto = None
	def __init__(self,nombre,edad,puesto,estatura):
		self.nombre=nombre
		self.edad=edad
		self.estatura=estatura
		self.puesto=puesto
pass

class Ropa:
	color = None
	talla = None
	genero = None
	propietario =[]
	def __init__(self,color,talla,genero,propietario,marca):
		self.color=color
		self.talla=talla
		self.genero=genero
		self.propietario=propietario
		self.marca=marca
pass

class Detergente:
	marca = None
	tipoderopa = None
	costo = None
	def __init__(self,marca,tipoderopa,costo):
		self.marca=marca
		self.tipoderopa=tipoderopa
		self.costo=costo
pass

class Lavadora:
	marca = None
	capacidad = None
	tipoderopa = None
	costo = None
	def __init__(self,marca,capacidad,tipoderopa,costo):
		self.marca=marca
		self.capacidad=capacidad
		self.tipoderopa=tipoderopa
		self.costo=costo
pass

	

