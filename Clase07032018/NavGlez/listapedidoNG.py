print("\nREFRESCOS")
print("\nArticulos Disponibles: ")
print("Pepsi\nManzanita\nSidral\nYoli\nFanta\nFresca\nCocaCola\nMirinda\n7Up")
milista=[]

def Agregar(a): #Agregar un articulo a la lista de pedido
	milista.append(a)
pass

def Lista():
	print("\nLista de Pedido",milista) # Tu lista de pedido, muestra los articulos de tu lista de pedidos
pass

def Entrega(): #Muestra la cantidad de un articulo pedido
	print("\nArticulo\tCantidad\n")
	b=milista.count("Pepsi")
	print("\nPepsi\t",b)
	c=milista.count("Manzanita")
	print("\nManzanita\t",c)
	d=milista.count("Sidral")
	print("\nSidral\t",d)
	e=milista.count("Yoli")
	print("\nYoli\t",e)
	f=milista.count("Fanta")
	print("\nFanta\t",f)
	g=milista.count("Fresca")
	print("\nFresca\t",g)
	h=milista.count("CocaCola")
	print("\nCocaCola\t",h)
	i=milista.count("Mirinda")
	print("\nMirinda\t",i)
	j=milista.count("7Up")
	print("\n7Up\t",j)



