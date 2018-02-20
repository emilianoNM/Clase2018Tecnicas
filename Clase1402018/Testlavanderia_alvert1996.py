#ALberto Garcia SAlazar

class Lavanderia:

	color=[None]
	tipo=[None]
	costo=[None]


	def __init__(self,color,tipo,costo):
		self.color=color
		self.tipo=tipo
		self.costo=costo

class lavado(Lavanderia):
	agua=None
	detergente=None
	suavizante=None
	def __init__(self,color,tipo,costo,agua,detergente,suavizante):
		Lavanderia.__init__(self,color,tipo,costo)
		self.agua=agua
		self.detergente=detergente
		self.suavizante=suavizante
	pass

class secado(Lavanderia):
	capacidad=None
	tiempo=None
	modo=None
	def __init__(self,color,tipo,costo,capacidad,tiempo,modo):
		Lavanderia.__init__(self,color,tipo,costo)
		self.capacidad=capacidad
		self.tiempo=tiempo
		self.modo=modo
	pass

class espera(Lavanderia):
	capacidadp=None
	elementos=None
	ubicacion=None
	def __init__(self,color,tipo,costo,capacidadp,elementos,ubicacion):
		Lavanderia.__init__(self,color,tipo,costo)
		self.capacidadp=capacidadp
		self.elementos=elementos
		self.ubicacion=ubicacion
	pass

class atencion(Lavanderia):
	personas=None
	elementosa=None
	def __init__(self,color,tipo,costo,personas,elementosa):
		Lavanderia.__init__(self,color,tipo,costo)
		self.personas=personas
		self.elementosa=elementosa
	pass
