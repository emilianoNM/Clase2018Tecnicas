#Programacion Orientada a Objetos

class Animal:
	organos=["Corazon", "Pulmones", "Estomago" ]
	estado="vivo"
# Contructor __init__
	def __init__(self,estado="vivo"):
		self.estado=estado
		self.organos=["Corazon", "Pulmones", "Estomago" ]
	  	print "Creando Objeto"
       
class Gato(Animal):
	pass

class Perro(Animal):
	pass
