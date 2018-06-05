import pickle

class Perro():
    raza=None
    nombre=None
    edad=None
    tamano=None
    genero=None
    pelaje=None
class Labrador(Perro):
    def __init__(self,raza,nombre,edad,tamano,genero,pelaje):
        self.raza=raza
        self.nombre=nombre
        self.edad=edad
        self.tamano=tamano
        self.genero=genero
        self.pelaje=pelaje
        
    def save(self,archivo):
        dato=file("datos.dat","w")
        dato.close()
        
    def load(self,archivo):
        dato=file("datos.dat","r")
        dato.close()

class Pastor_Aleman(Perro):
    
    def __init__(self,raza,nombre,edad,tamano,genero,pelaje):
        self.raza=raza
        self.nombre=nombre
        self.edad=edad
        self.tamano=tamano
        self.genero=genero
        self.pelaje=pelaje
    def save(self,archivo):
        dato1=open("datos1.dat","w")
        dato1.close()
        
    def load(self,archivo):
        dato1=open("datos1.dat","r")
        dato1.close()


class Pug(Perro):
    
    def __init__(self,raza,nombre,edad,tamano,genero,pelaje):
        self.raza=raza
        self.nombre=nombre
        self.edad=edad
        self.tamano=tamano
        self.genero=genero
        self.pelaje=pelaje
    def save(self,archivo):
        dato2=open("datos2.dat","w")
        dato2.close()
    def load(self,archivo):
        dato2=open("datos2.dat","r")
        dato2.close()
