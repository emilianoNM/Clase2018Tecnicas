#Benjamin Cruz Sarmiento

import pickle


class Territorio():

	Estado=None
	Capital=None
	Poblacion=None
	Territorio=None
	Clima=None
##############Clase1###############
class Guadalajara(Territorio):

	def __init__(self,Estado,Capital,Poblacion,Territorio,Clima):
		
		self.Estado=Estado
		self.Capital=Capital
		self.Poblacion=Poblacion
		self.Territorio=Territorio
		self.Clima=Clima


 	def Save(self, archivo):
		fichero=file("datos.dat","w")
		fichero.close()

	def Load(self, archivo):
		fichero=file("datos.dat","r")
		fichero.close()
    

##############Clase2###############
class Monterrey(Territorio):

	def __init__(self,Estado,Capital,Poblacion,Territorio,Clima):
		
		self.Estado=Estado
		self.Capital=Capital
		self.Poblacion=Poblacion
		self.Territorio=Territorio
		self.Clima=Clima


 	def Save(self, archivo):
		fichero2=file("datos2.dat","w")
		fichero2.close()

	def Load(self, archivo):
		fichero2=file("datos2.dat","r")
		fichero2.close()
    
##############Clase 3###############
class Colima(Territorio):

	def __init__(self,Estado,Capital,Poblacion,Territorio,Clima):
		
		self.Estado=Estado
		self.Capital=Capital
		self.Poblacion=Poblacion
		self.Territorio=Territorio
		self.Clima=Clima


 	def Save(self, archivo):
		fichero3=file("datos3.dat","w")
		fichero3.close()

	def Load(self, archivo):
		fichero3=file("datos3.dat","r")
		fichero3.close()
    



