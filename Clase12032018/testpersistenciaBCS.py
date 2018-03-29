#Benjamin Cruz Sarmiento

import pickle
import PersistenciaBCS

########## Clase 1#########
fichero=file("datos.dat","w")

Elestado=PersistenciaBCS.Guadalajara("Guadalajara","Jalisco","1,300,342","2,323,212 m2","Templado")

Elestado.Save("BCS.dat")
pickle.dump(Elestado,fichero)


Elestado.Load("BCS.dat")
print(Elestado.Estado)
print(Elestado.Capital)
print(Elestado.Poblacion)
print(Elestado.Territorio)
print(Elestado.Clima)
print("")

########## Clase 2#########
fichero2=file("datos2.dat","w")

Elestado2=PersistenciaBCS.Monterrey("Monterrey","Nuevo Leon","2,323,342","923,212 m2","Humedo")

Elestado2.Save("BCS2.dat")
pickle.dump(Elestado2,fichero2)


Elestado2.Load("BCS.dat")
print(Elestado2.Estado)
print(Elestado2.Capital)
print(Elestado2.Poblacion)
print(Elestado2.Territorio)
print(Elestado2.Clima)
print("")

########## Clase 3#########
fichero3=file("datos3.dat","w")

Elestado3=PersistenciaBCS.Colima("Colima","Colima","2,342,452","1,483,212 m2","Seco")

Elestado3.Save("BCS.dat")
pickle.dump(Elestado3,fichero3)


Elestado3.Load("BCS3.dat")
print(Elestado3.Estado)
print(Elestado3.Capital)
print(Elestado3.Poblacion)
print(Elestado3.Territorio)
print(Elestado3.Clima)
print("")
