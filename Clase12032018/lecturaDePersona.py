import pickle
import persistenciaPersona
fichero=file("datos.dat","r")

persona=pickle.load(fichero)

print persona.nombre

persona2=pickle.load(fichero)

print persona2.nombre
