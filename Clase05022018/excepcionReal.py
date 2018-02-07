class PersonaNoGrata(Exception):
    pass

class Persona():
     def __init__(self,Nombre,Trabajo="politico"):
         
         self.Nombre=Nombre
         
         if(Trabajo=="politico"):
             raise PersonaNoGrata()
         
         self.Trabajo=Trabajo

         print ("hola ",self.Nombre, " Con el trabajo de " ,self.Trabajo)

