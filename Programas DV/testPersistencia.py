import pickle
import Persistencia

dato=file("datos.dat","w")
Nina=Persistencia.Chihuahua("Chihuahua","Nina","5","Mediana","Hembra","Largo")

Nina.save("nin.dat")
pickle.dump(Nina,dato)

Nina.load("nin.dat")

print(Nina.raza)
print(Nina.nombre)
print(Nina.edad)
print(Nina.tamano)
print(Nina.genero)
print(Nina.pelaje)
print("\n")


dato1=file("datos1.dat","w")
Peluche=Persistencia.Cruza("Cruza","Peluche","15","Mediano","Macho","Semilargo")
Peluche.save("pel.dat")
pickle.dump(Peluche,dato1)
Peluche.load("pel.dat")


print(Peluche.raza)
print(Peluche.nombre)
print(Peluche.edad)
print(Peluche.tamano)
print(Peluche.genero)
print(Peluche.pelaje)
print("\n")



dato2=file("datos2.dat","w")

Kivo=Persistencia.Cruza("Cruza","Kivo","5 años","Grande","Macho","Corto")
Kivo.save("Kiv.dat")
pickle.dump(Kivo,dato2)
Kivo.load("odi.dat")

print(Kivo.raza)
print(Kivo.nombre)
print(Kivo.edad)
print(Kivo.tamano)
print(Kivo.genero)
print(Kivo.pelaje)
print("\n")
