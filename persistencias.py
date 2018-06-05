import pickle
import Persistencias

fichero=file("datos.dat","wb")

persona=Persistencias.Daniel("Daniel","22","masculino","1.73")

persona.Save("persona.dat")
pickle.dump(persona,fichero)


datospersona.Load("persona.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)




fichero2=file("datos2.dat","w")

persona2=Persistencias.Mauricio("Mauricio","15","masculino","1.78")

persona2.Save("persona2.dat")
pickle.dump(persona2,fichero2)


persona2.Load("pesona.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)


fichero3=file("datos3.dat","w")

persona3=Persistencias.Eduardo("Eduardo","58","masculino","1.72")

persona3.Save("persona.dat")
pickle.dump(persona3,fichero3)


persona3.Load("persona3.dat")
print(persona.Nombre)
print(persona.Edad)
print(persona.sexo)
print(persona.Altura)
