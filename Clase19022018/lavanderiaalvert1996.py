#Alberto Garcia Salazar

class Lavanderia:

	color=[None]
	tipo=[None]
	costo=[None]
	nombre=None

	def __init__(self,nombre,color,tipo,costo):
		self.nombre=nombre
		self.color=color
		self.tipo=tipo
		self.costo=costo

class Lavadora(Lavanderia):
	agua=None
	detergente=None
	suavizante=None
	elemento=[]
	def __init__(self,nombre,color,tipo,costo,agua,detergente,suavizante):
		Lavanderia.__init__(self,nombre,color,tipo,costo)
		self.agua=agua
		self.detergente=detergente
		self.suavizante=suavizante
		self.elemento3=[]
	def __str__(self):
		return self.nombre
	

class Secadora(Lavanderia):
	capacidad=None
	tiempo=None
	modo=None
	def __init__(self,nombre,color,tipo,costo,capacidad,tiempo,modo):
		Lavanderia.__init__(self,nombre,color,tipo,costo)
		self.capacidad=capacidad
		self.tiempo=tiempo
		self.modo=modo
		self.elemento2=[]
	def __str__(self):
		return self.nombre

class Lavadero(Lavanderia):
	tamano=None
	textura=None
	altura=None
	def __init__(self,nombre,color, tipo, costo,capacidad,tiempo,modo):
		Lavanderia.__init__(self,nombre,color,tipo,costo)
		self.tamano=tamano
		self.textura=textura
		self.altura=altura
		self.elemento1=[]
	def __str__(self):
		return self.nombre
	

class usuario(Lavanderia):
	npersonas=None
	edad=None
	def __init__(self,npersonas,edad):
		self.npersonas=npersonas
		self.edad=edad
	def __str__(self):
		return self.npersonas
	def accionalav(self,lavadora,color):
		Elemento1=Lavado(lavadora,self,color)
		lavadora.elemento3.append(Elemento1)
	def accionasec(self,secadora,color):
		Elemento2=Secado(secadora,self,color)
		secadora.elemento2.append(Elemento2)
	def usalavadero(self,lavadero,color):
		Elemento3=Lavado1(lavadero,self,color)
		lavadero.elemento1.append(Elemento3)
		


class Lavado1():
	def __init__(self,lavadero,npersonas,color):
		self.lavadero=lavadero
		self.color=color
		self.npersonas=npersonas
	def tiempo(self,tiempo):
		self.tiempo=tiempo
	def caracteristica(self):
		print ("se esta usando el lavadero "+str(self.lavadero)+" por "+str(self.npersonas)+" por "+str(self.tiempo)+" minutos")
	

class Secado():
	def __init__(self,secadora,npersonas,color):
		self.secadora=secadora
		self.color=color
		self.npersonas=npersonas
	def tiempo(self,tiempo):
		self.tiempo=tiempo
	def caracteristica(self):
		print ("se activo la secadora "+str(self.secadora)+" por "+str(self.npersonas)+" por "+str(self.tiempo)+" minutos")

class Lavado():
	def __init__(self,lavadora,npersonas,color):
		self.lavadora=lavadora
		self.color=color
		self.npersonas=npersonas
	def tiempo(self,tiempo):
		self.tiempo=tiempo
	def caracteristica(self):
		print ("se activo la lavadora "+str(self.lavadora)+" por "+str(self.npersonas)+" por "+str(self.tiempo)+" minutos")
