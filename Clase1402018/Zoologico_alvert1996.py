#Alberto Garcia Salazar

class Especies:
	estado=[]	
	edad=[]
	color=[]
	nombre=[]


	def __init__(self,estado,edad,color,nombre):
		self.estado=estado
		self.edad=edad
		self.color=color		
		self.nombre=nombre

class tucan(Especies):
	pico=None
	pluma=None
	canto=None
	def __init__(self,estado,edad,color,nombre,pico,pluma,canto):
		Especies.__init__(self,estado,edad,color,nombre)
		self.pico=pico
		self.pluma=pluma
		self.canto=canto
	pass

class cocodrilo(Especies):
	tamano=None
	piel="escamosa"
	comida=None
	def __init__(self,estado,edad,color,nombre,tamano,piel,comida="Carne"):
		Especies.__init__(self,estado,edad,color,nombre)
		self.tamano=tamano
		self.comida="carne"
	pass

class elefante(Especies):
	tamano=None
	piel=None
	sexo=None
	def __init__(self,estado,edad,color,nombre,tamano,piel,sexo):
		Especies.__init__(self,estado,edad,color,nombre)
		self.tamano=tamano
		self.piel=piel
		self.sexo=sexo
	pass

class jirafa(Especies):
	comida=None
	piel=[]
	sexo=[]
	def __init__(self,estado,edad,color,nombre,comida,piel,sexo):
		Especies.__init__(self,estado,edad,color,nombre)
		self.comida=comida
		self.piel=piel
		self.sexo=sexo
	pass

class hipopotamo(Especies):
	sexo=[]
	sonido=[]
	caracter=[]
	def __init__(self,estado,edad,color,nombre,sonido,caracter,sexo):
		Especies.__init__(self,estado,edad,color,nombre)
		self.sonido=sonido
		self.caracter=caracter
		self.sexo=sexo
	pass
