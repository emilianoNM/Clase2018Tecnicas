import pickle

class SeleccionesMundial():

	NomSeleccion=None
	Campeonatos=None
	Estadio=None
	Participaciones=None
	ColorUniforme=None
	Confederacion=None

class Alemania(SeleccionesMundial):

	def __init__(self,NomSeleccion,Campeonatos,Estadio,Participaciones,ColorUniforme,Confederacion):
		self.NomSeleccion=NomSeleccion
		self.Campeonatos=Campeonatos
		self.Estadio=Estadio
		self.Participaciones=Participaciones
		self.ColorUniforme=ColorUniforme
		self.Confederacion=Confederacion

	def save(self, archivo):
			fI=file("datosI.dat","w")
			fI.close()

	def load(self, archivo):
			fI=file("datosI.dat","r")
			fI.close()
class Brasil(SeleccionesMundial):

	def __init__(self,NomSeleccion,Campeonatos,Estadio,Participaciones,ColorUniforme,Confederacion):
		self.NomSeleccion=NomSeleccion
		self.Campeonatos=Campeonatos
		self.Estadio=Estadio
		self.Participaciones=Participaciones
		self.ColorUniforme=ColorUniforme
		self.Confederacion=Confederacion

	def save(self,archivo):
		fII=file("datosII.dat","w")
		fII.close()

	def load(self,archivo):
		fII=file("datosII.dat","r")
		fII.close()

class Mexico(SeleccionesMundial):

	def __init__(self,NomSeleccion,Campeonatos,Estadio,Participaciones,ColorUniforme,Confederacion):
		self.NomSeleccion=NomSeleccion
		self.Campeonatos=Campeonatos
		self.Estadio=Estadio
		self.Participaciones=Participaciones
		self.ColorUniforme=ColorUniforme
		self.Confederacion=Confederacion

	def save(self,archivo):
		fIII=file("datosIII.dat","w")
		fIII.close()

	def load(self,archivo):
		fIII=file("datosIII.dat","r")
		fIII.close()
		
