import pickle
import persistenciaNG

#Clase Alemania
fI=file("datosI.dat","w")

SM=persistenciaNG.Alemania("Alemania","4","Olimpico de Berlin","19","Blanco","UEFA")

SM.save("osoI.dat")
pickle.dump(SM,fI)

SM.load("osoI.dat")

print(SM.NomSeleccion)
print(SM.Campeonatos)
print(SM.Estadio)
print(SM.Participaciones)
print(SM.ColorUniforme)
print(SM.Confederacion)
print("")

#Clase Brasil

fII=file("datosII.dat","w")
SM=persistenciaNG.Brasil("Brasil","5","Maracana","21","Amarillo","CONMEBOL")

SM.save("osoII.dat")
pickle.dump(SM,fII)

SM.load("osoII.dat")

print(SM.NomSeleccion)
print(SM.Campeonatos)
print(SM.Estadio)
print(SM.Participaciones)
print(SM.ColorUniforme)
print(SM.Confederacion)
print("")

#Clase Mexico

fIII=file("datosIII.dat","w")
SM=persistenciaNG.Mexico("Mexico","0","Estadio Azteca","15","Verde","CONCACAF")

SM.save("osoIII.dat")
pickle.dump(SM,fIII)

SM.load("osoIII.dat")

print(SM.NomSeleccion)
print(SM.Campeonatos)
print(SM.Estadio)
print(SM.Participaciones)
print(SM.ColorUniforme)
print(SM.Confederacion)
print("")

#Nava Gonzalez 