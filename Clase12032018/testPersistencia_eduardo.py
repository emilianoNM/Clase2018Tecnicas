#Hernandez Quinatna Luis Eduardo
import pickle
import Persistencia_eduardo

fichero=file("datos.dat","wb")

persona=Persistencia_eduardo.Eduardo("Eduardo","22","masculino","1.70")

persona.Save("persona.dat")
pickle.dump(persona,fichero)


Elestado.Load("persona.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)




fichero2=file("datos2.dat","w")

persona2=Persistencia_eduardo.Raul("Raul","16","masculino","1.80")

persona2.Save("persona2.dat")
pickle.dump(persona2,fichero2)


persona2.Load("pesona.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)




fichero3=file("datos3.dat","w")

persona3=Persistencia_eduardo.Carlos("Raul","16","masculino","1.80")

persona3.Save("persona.dat")
pickle.dump(persona3,fichero3)


persona3.Load("persona3.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)
