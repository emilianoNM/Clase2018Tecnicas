#Benjamin Cruz Sarmiento

class BibliotecaBCS():

	Titulo=None
	Nodeedicion=None
	Nodepaginas=None
	Estado=None
######################Libro1###########################
class Mipadre(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 1 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

###############################Libro 2############################ 
class Elalquimista(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 2 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

################Libro 3####################

class Elalmohadon(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
	

		print("--------------------------- Libro 3 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("El libro esta siendo ocupado por: "+str(self.Nombre))
		print("")

##################Libro 4###################
class Elmonje(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 4 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

################## Libro 5 #####################

class Cerdo(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
	

		print("--------------------------- Libro 5 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("El libro esta siendo ocupado por: "+str(self.Nombre))
		print("")

############Libro 6#####################

class Laodisea(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 6 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

#############Libro 7###################

class Lailiada(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
	

		print("--------------------------- Libro 7 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("El libro esta siendo ocupado por: "+str(self.Nombre))
		print("")

#############Libro 8#################

class Batallas(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
	

		print("--------------------------- Libro 8 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("El libro esta siendo ocupado por: "+str(self.Nombre))
		print("")

################Libro 9 ############

class Psicomagia(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 9 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

#############Libro 10################

################Libro 9 ############

class Principito(BibliotecaBCS):
	Autor=None
	Editorial=None
	Nombre=None
	Nodecuenta=None
	Prestamo=None
	Devolucion=None

	def __init__(self,Titulo,Nodepaginas,Editorial,Autor,Estado,Nodeedicion,Nombre,Nodecuenta,Prestamo,Devolucion):
		self.Titulo=Titulo
		self.Nodepaginas=Nodepaginas
		self.Editorial=Editorial
		self.Autor=Autor
		self.Estado=Estado
		self.Nodeedicion=Nodeedicion
		self.Nombre=Nombre
		self.Nodecuenta=Nodecuenta
		self.Prestamo=Prestamo
		self.Devolucion=Devolucion

		print("--------------------------- Libro 10 ------------------------")
		print("---------------------------  "+self.Titulo+" ----------------------")
		print("")
		print("")

	def __str__(self):
		return self.Titulo	

	def Busqueda(self):
		print("INFORMACION ACERCA DE ESTE LIBRO")
		print("")
		print("Titulo del libro: "+str(self.Titulo))
		print("Autor principal: "+str(self.Autor))
		print("Editorial: "+str(self.Editorial))
		print("Numero de edicion: "+str(self.Nodeedicion))
		print("Numero de paginas: "+str(self.Nodepaginas))
		print("Estado del libro: "+str(self.Estado))
		print("")
		print("")

	def Libro(self):

		print("Usted ha solicitado el siguiente libro")
		print("")
		print("La persona: "+str(self.Nombre))
		print("Numero de cuenta: "+str(self.Nodecuenta))
		print("Tiene el libro: "+str(self.Titulo))
		print("Autor principal del libro: "+str(self.Autor))
		print("Fecha de solicitud: "+str(self.Prestamo))
		print("Fecha de entrega: "+str(self.Devolucion))
		print("")
		print("")

