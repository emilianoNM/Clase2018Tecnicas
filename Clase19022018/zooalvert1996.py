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
	def vuelamucho(self):
		print("Se agrego una caracteristica del tucan "+str(self))
		print(str(self.edad)+" anos, con pico "+str(self.pico)+", plumas "+str(self.pluma)+" y canto "+str(self.canto))
	def vuelapoco(self):
		print("se agrego una caracteristica del tucan "+str(self))
		print(str(self.edad)+" anos, con pico "+str(self.pico)+", plumas "+str(self.pluma)+" y canto "+str(self.canto))
	def __str__(self):
		return self.nombre
	pass

class cocodrilo(Especies):
	tamano=None
	piel="escamosa"
	comida=None
	def __init__(self,estado,edad,color,nombre,tamano,piel,comida="Carne"):
		Especies.__init__(self,estado,edad,color,nombre)
		self.tamano=tamano
		self.comida="carne"
		self.dia=[]
	def __str__(self):
		return self.nombre
	def nadar(self,modo):
		self.modo=modo
		print("se registro una caracteristica del cocodrilo "+str(self))
	def caracteristicas(self):
		print(str(self)+" tiene "+str(self.edad)+ " anos y nada "+self.modo)
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
	def __str__(self):
		return self.nombre
	def come(nombre,self,modo):
		self.modo=modo
	def duerme(nombre,self,horas):
		self.horas=horas
	def caracteristica(self):
		print("\n"+str(self)+" es un elefante "+str(self.sexo)+" tiene "+str(self.edad)+" anos, es "+str(self.tamano)+", come "+str(self.modo)+" y duerme "+str(self.horas)+" horas al dia")
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
	def __str__(self):
		return self.nombre
	def come(self,modo):
		self.modo=modo
	def duerme(self,horas):
		self.horas=horas
	def caracteristica(self):
		print("\n"+str(self)+" es una jirafa "+str(self.sexo)+" tiene "+str(self.edad)+" anos, es  de piel "+str(self.piel)+", come "+str(self.comida)+" de forma "+str(self.modo)+" y duerme "+str(self.horas)+" horas al dia")
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
	def __str__(self):
		return self.nombre
	def nada(self,nada):
		self.nada=nada
	def duerme(self,horas):
		self.horas=horas
	def caracteristica(self):
		print("\n"+str(self)+" es un hipopotamo "+str(self.sexo)+" tiene "+str(self.edad)+" anos, es de caracter "+str(self.caracter)+", su sonido es "+str(self.sonido)+", nada al dia "+str(self.nada)+" horas y duerme "+str(self.horas)+" horas al dia")
	pass
