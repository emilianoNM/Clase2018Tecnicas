class object:
  
    def __init__(self):
        opcion=str(input("desea consultar la lista de materiales? si/no"))
        if opcion == "si":
           import json
           f=open("productos.json","r")
           productos=f.read()
           c=json.loads(productos)
           self.productos=c
           self.output=[]
        else:
               pass   
    
    def imprimir(self):
        self.opcion1=str(input("Materiales y Piezas (MP)/ Suministros(SS):"))
        if self.opcion1 in self.productos:
           print("")
           print(self.opcion1,":",self.productos[self.opcion1])
           print("")
           
    def seleccion(self):
        self.opcion2=str(input("Ingrese el codigo del articulo que desea adquirir:"))
        #asignacion variable w
        w=(self.productos[self.opcion1][self.opcion2][2])
        if int(w)<= 0:
          print("No hay productos en existencia.")
          print("")
        else:
          print("usted adquirio:")
          if self.opcion2 in self.productos[self.opcion1]:
            print(self.opcion2,":",self.productos[self.opcion1][self.opcion2])
            self.output.append(self.productos[self.opcion1][self.opcion2])
            
            #read the document
            import json
            f=open("productos.json","r")
            productos=f.read()
            self.productos=json.loads(productos)
            
            #Modifies document
            #print the quantity of the stock before the selection
            print(self.productos[self.opcion1][self.opcion2][2])
            self.productos[self.opcion1][self.opcion2][2]=int(self.productos[self.opcion1][self.opcion2][2]) - 1
            #print the quantity of the stock after the selection
            print(self.productos[self.opcion1][self.opcion2][2])
            f.close()
            
            #writes and modify document
            f = open("productos.json","w")
            json = json.dumps(self.productos)
            f.write(json)
            f.close()
            
    #hace el listado de los elementos de la self.output
    def listado(self):
        print(self.output)
        print("lista total:")
        for elemento in self.output:
          print(elemento[0],elemento[1])        
          
    #calls all the functions
    def llamado(self):
        continua="s"
        while continua=="s":
          self.imprimir()
          self.seleccion()
          continua=input("Desea agregar otro producto[s/n]?")
          print("_______________________________________")
          print("")
        self.listado() 
  
    
    
# bloque principal
productos1=object()
productos1.llamado()