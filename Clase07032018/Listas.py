#Arreglo 

arreglo=[1,2,3,4,5,6,7,8]

arreglo2=range(1,10)

arreglo3=range(1,20,2)

arreglo4=range(10,-10,-1)

print (arreglo)

print (arreglo2)

print (arreglo3)

print (arreglo4)

print (dir(arreglo))
print (type(arreglo))

#Metodos de listas 

print(len(arreglo))

print (arreglo[2])

print ("Metodo sort")
print (arreglo4.sort())

print (arreglo4)

#Agregar un elemento 

arreglo4.append(1234)

print (arreglo4)

#Optener un elemento del arreglo 
b=arreglo4.pop()

print (b) 

print (arreglo4)
 
#Estructura de Pila

pila=[]

print(pila)

pila.append("Primer Objeto")

pila.append("Segundo Objeto")

pila.append("Tercer Objeto")

for i in range(0,19000):
    pila.append("Objecto "+str( i) )


print pila 

while(len(pila)>0):
    print (pila.pop())

print pila











