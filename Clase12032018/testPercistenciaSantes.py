# Santes Mejia Antonio
print "...Tecnicas de programacion.."

import pickle
import Persistencia

Santes=file("datos.dat","a")

Ventas=Persistencia.Aveo("Aveo","Chevrolet","2013","$60,000")

Ventas.Save("Santes.dat")
pickle.dump(Ventas,Santes)


Ventas.Load("Santes.dat")
print(Ventas.Nombre)
print(Ventas.Marca)
print(Venetas.Modelo)
print(Ventas.Precios)


Santes2=file("datos.dat2","a")

Ventas2=Persistencia.Versa("Versa","Nissan","2016","$110,000")

Ventas2.Save("Santes2.dat")
pickle.dump(Ventas2,Santes2)


Ventas2.Load("Santes.dat")
print(Ventas.Nombre)
print(Ventas.Marca)
print(Venetas.Modelo)
print(Ventas.Precios)


Santes3=file("datos.dat3","a")

Ventas3=Persistencia.Vento("Vento","WV","2014","$95,000")

Ventas3.Save("Santes3.dat")
pickle.dump(Ventas3,Santes3)


Ventas3.Load("Santes.dat")
print(Ventas.Nombre)
print(Ventas.Marca)
print(Venetas.Modelo)
print(Ventas.Precios)



