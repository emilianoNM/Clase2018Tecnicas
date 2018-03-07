import Queue 

cola=Queue.Queue()

print (cola)

print (dir(cola))

cola.put("Perro")
cola.put("Gato")
cola.put("Conejo")

print cola.get()

print cola.get()

cola.put("armadillo")
print cola.get()

print cola.get()

class  Producto():
    def __init__(self,Nombre,Precio):
        self.Nombre=Nombre
        self.Precio=Precio
    def __str__(self):
        return self.Nombre+" Precio " + str(self.Precio)
    def __repr__(self):
        return self.__str__()
ListaDeProductos=[]

ListaDeProductos.append(Producto("jamon",20))

ListaDeProductos.append(Producto("Pan",15))
ListaDeProductos.append(Producto("Salchicha",25))
ListaDeProductos.append(Producto("Pierna",16))

print ListaDeProductos

ultimoProducto=ListaDeProductos.pop()

print ultimoProducto.Nombre 

