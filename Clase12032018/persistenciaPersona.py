import pickle

fichero=file("datos.dat","w")



class Persona():
    def __init__(self,nombre,edad,sexo,altura):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.altura=altura
    def save(self,Archivo):
        pass
    def load(self,Archivo):
        pass

persona1=Persona("Emiliano",29,"Masculino",1.75)

persona2=Persona("Lucia",25,"Femenino",1.65)

pickle.dump(persona1,fichero)

pickle.dump(persona2,fichero)

fichero.close()

