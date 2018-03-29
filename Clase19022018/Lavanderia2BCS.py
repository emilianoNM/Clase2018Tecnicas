#Benjamin Cruz Sarmiento

class Lavanderia2BCS():

	tipodelavado=None
	tipodeprenda=None
	color=None
	costo=None
	material=None

####################### Lavadora 1 #####################
	
class Lavadora1(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 1 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")


####################### Lavadora2 #####################
	
class Lavadora2(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 2 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora3 #####################
	
class Lavadora3(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 3 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora 4 #####################
	
class Lavadora4(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 4 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora 5 #####################
	
class Lavadora5(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 5 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora 6 #####################
	
class Lavadora6(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 6 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora 7 #####################
	
class Lavadora7(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 7 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")


####################### Lavadora 8 #####################
	
class Lavadora8(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 8 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")


####################### Lavadora 9 #####################
	
class Lavadora9(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 9 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")

####################### Lavadora 10 #####################
	
class Lavadora10(Lavanderia2BCS):
	
	detergente=None
	niveldeagua=None
	temperatura=None
	Nolavadora=None
	Servicio1=None
	Servicio2=None
	Servicio3=None
	
	
	def __init__(self,tipodeprenda,material,tipodelavado,color,costo,detergente,niveldeagua,temperatura,Nolavadora,Servicio1,Servicio2,Servicio3):
		
		self.tipodeprenda=tipodeprenda
		self.material=material
		self.tipodelavado=tipodelavado
		self.color=color
		self.costo=costo
		self.detergente=detergente
		self.niveldeagua=niveldeagua
		self.temperatura=temperatura
		self.Nolavadora=Nolavadora
		self.Servicio1=Servicio1
		self.Servicio2=Servicio2
		self.Servicio3=Servicio3

		print("#################### Lavadora 10 ####################")
		print("")
		print("")

 	def __str__(self):

		return self.tipodelavado 

	def Articulo1(self):

		print("Usted esta en la "+str(self.Nolavadora))
		print("Tipo de prenda a lavar: "+str(self.tipodeprenda))
		print("Costo lavar esa prenda: "+str(self.costo))		
		print("")
		print("")

	def Especificaciones(self):

		print("Especificaciones para esta prenda")
		print("")
		print("Material: "+str(self.material))
		print("Tipo de lavado: "+str(self.tipodelavado))
		print("Color de la prenda: "+str(self.color))
		print("tipo de detergente a emplear: "+str(self.detergente))
		print("Nivel de agua para la prenda: "+str(self.niveldeagua))
		print("Temperatura del agua: "+str(self.temperatura))
		print("")
		print("")

	def Servicio(self):


		print("Seleccione alguno de los servicios adicionales: ")
		print("")
		print("Usted ha solicitado los siguientes servicios extras: ")
		print(str(self.Servicio1))
		print(str(self.Servicio2))
		print(str(self.Servicio3))
		print("")
		print("")


