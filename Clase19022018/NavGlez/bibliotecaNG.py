class Libro:
    Titulo=""
    Autor=""
    Editorial=""
    Publicacion=""
    Edicion=""
class Historia(Libro):

    def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
    def aprender(self):
        print("aprender del pasado")
    def desarrollar(self):
        print("desarollan la critica del lector")

class Matematicas(Libro):
     def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
     def desarollar(self):
        print("la habilidad matematica")
     def logica(self):
        print("las matematicas contienen mucha logica")

class Biologia:
     def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
     def mundo(self):
        print("te mustra un nuevo mundo, el mundo de la celula")
     def desarollar(self):
        print("la celula lleva a cabo distintos procesos")

class Civismo(Libro):
     def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
     def ensenar(self):
        print("ensenar los valores que tenemos como ser humanos")
     def moral(self):
        print("que es lo bueno y lo malo")
     
class Geografia(Libro):
     def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
     def desar(self):
        print("desarrollas una buena memoria si aprendes cada rio, capital, etc")
     def cultura(self):
        print("te muestra la cultura de cada pais")

class Fisica(Libro):
     def __init__(self,Titulo,Autor,Editorial,Publicacion,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.publicacion=Publicacion
        self.edicion=Edicion
     def desarrolar(self):
        print("va de la mano con la habilidad matematica")    
     def aprender(self):
         print("como es el mundo y las leyes que lo rigen(fisica)")
    

