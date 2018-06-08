#Laura Gomez
#Creando una biblioteca

class Libros:

        def __init__(self,autor,editorial,pasillo):
            self.autor = autor
            self.editorial = editorial
            self.pasillo = pasillo        
        
        pass

class Novelas(Libros):

        def __init__(self,autor,editorial,pasillo,titulo,paginas,pais):
                Libros.__init__(self,autor,editorial,pasillo)
                self.titulo = titulo
                self.paginas = paginas
                self.pais = pais
        pass

class Cuentos(Libros):

        def __init__(self,autor,editorial,pasillo,tema,clasificacion,paginas):
                Libros.__init__(self,autor,editorial,pasillo)
                self.tema = tema
                self.clasificacion = clasificacion
                self.paginas = paginas
        pass

class Enciclopedias(Libros):

        def __init__(self,autor,editorial,pasillo,tema,paginas,titulo):
                Libros.__init__(self,autor,editorial,pasillo)
                self.tema = tema
                self.paginas = paginas
                self.titulo = titulo
        pass

class Poesia(Libros):

        def __init__(self,autor,editorial,pasillo,tema,clasificacion,titulo):
                Libros.__init__(self,autor,editorial,pasillo)
                self.tema = tema
                self.clasificacion = clasificacion
                self.titulo = titulo
        pass
