import pickle
import PersistenciaOliverMendieta

dato=file("datos.dat","w")
Liona=PersistenciaOliverMendieta.Labrador("Labrador","Liona","5","Mediana","Hembra","Largo")

Liona.save("lio.dat")
pickle.dump(Liona,dato)

Liona.load("lio.dat")

print(Liona.raza)
print(Liona.nombre)
print(Liona.edad)
print(Liona.tamano)
print(Liona.genero)
print(Liona.pelaje)
print("\n")


dato1=file("datos1.dat","w")
Caramelo=PersistenciaOliverMendieta.Pastor_Aleman("Pastor Aleman","Caramelo","15","Grande","Hembra","Semilargo")
Caramelo.save("car.dat")
pickle.dump(Caramelo,dato1)
Caramelo.load("car.dat")


print(Caramelo.raza)
print(Caramelo.nombre)
print(Caramelo.edad)
print(Caramelo.tamano)
print(Caramelo.genero)
print(Caramelo.pelaje)
print("\n")



dato2=file("datos2.dat","w")

Odin=PersistenciaOliverMendieta.Pug("Pug","Odin","3 meses","Pequeno","Macho","Corto")
Odin.save("odi.dat")
pickle.dump(Odin,dato2)
Odin.load("odi.dat")

print(Odin.raza)
print(Odin.nombre)
print(Odin.edad)
print(Odin.tamano)
print(Odin.genero)
print(Odin.pelaje)
print("\n")
