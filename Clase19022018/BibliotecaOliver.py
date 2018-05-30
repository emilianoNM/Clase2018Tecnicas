class Libro:
    Titulo=""
    Autor=""
    Editorial=""
    Edicion=""
class Ciencia_Ficcion(Libro):

    def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
    def imaginar(self):
        print("hacen imaginar otros mundos")
    def desarrollo(self):
        print("desarollan creatividad en el lector")
class Cientifico(Libro):
     def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
     def enseñar(self):
        print("permite adquirir conocimientos")
     def paciencia(self):
        print("si te esfuerzas adquieres paciencia para leerlos")
class Lit__Clásica(Libro):
     def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
     def historia(self):
        print("permite conocer la situacion de la epoca")
     def cultura(self):
        print("")
class Terror(Libro):
     def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
     def asustar(self):
        print("crean terror en lsa personas")
     def suspenso (self):
        print("mantienen en suspenso al lector")
     def entretener (self):
        print("da entretenimiento al lector")
     def enseñar(self):
        print("enseña historias para contar")
class Viaje(Libro):
     def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
     def consultar(self):
        print("consultar rutas")
     def guia(self):
        print("sirve de guia para  turistas")
class Poeticos(Libro):
     def __init__(self,Titulo,Autor,Editorial,Edicion):
        self.titutlo=Titulo
        self.autor=Autor
        self.editorial=Editorial
        self.edicion=Edicion
     def dedicar(self):
        print("aprender poemas para dedicar")    
     def aprender(self):
         print("enseñana a hacer versos")
    

