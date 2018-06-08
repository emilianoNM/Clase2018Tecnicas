#Heidi Gómez 
#Crear un zologico con 10 especies 3 atributos cada especie / con constructor

class Especie:

        def __init__(self,nombre,edad,alimento):
            self.nombre = nombre
            self.edad = edad
            self.alimento = alimento        
        
        pass

class Aves(Especie):

        def __init__(self,nombre,edad,alimento,pico,plumas,color):
                Especie.__init__(self,nombre,edad,alimento)
                self.pico = pico
                self.plumas = plumas
                self.color = color
        pass

class Anfibios(Especie):

        def __init__(self,nombre,edad,alimento,piel,color,tamaño):
                Especie.__init__(self,nombre,edad,alimento)
                self.piel = piel
                self.color = color
                self.tamaño = tamaño
        pass

class Mamiferos(Especie):

        def __init__(self,nombre,edad,alimento,pelo,tamaño,estancia):
                Especie.__init__(self,nombre,edad,alimento)
                self.pelo = pelo
                self.tamaño = tamaño
                self.estancia = estancia
        pass

class Reptiles(Especie):

        def __init__(self,nombre,edad,alimento,color,tamaño,cola):
                Especie.__init__(self,nombre,edad,alimento)
                self.color = color
                self.tamaño = tamaño
                self.cola = cola
        pass

class Tunicados(Especie):

        def __init__(self,nombre,edad,alimento,clase,color,tamaño):
                Especie.__init__(self,nombre,edad,alimento)
                self.clase = clase
                self.color = color
                self.tamaño = tamaño
        pass

class Aracnidos(Especie):

        def __init__(self,nombre,edad,alimento,color,respiracion,patas):
                Especie.__init__(self,nombre,edad,alimento)
                self.color = color
                self.respiracion = respiracion
                self.patas = patas
        pass

class Peces(Especie):

        def __init__(self,nombre,edad,alimento,color,tamaño,estancia):
                Especie.__init__(self,nombre,edad,alimento)
                self.color = color
                self.tamaño = tamaño
                self.estancia = estancia
        pass

class Insectos(Especie):

        def __init__(self,nombre,edad,alimento,color,patas,tamaño):
                Especie.__init__(self,nombre,edad,alimento)
                self.color = color
                self.patas = patas
                self.tamaño = tamaño
        pass

class Agnatos(Especie):

        def __init__(self,nombre,edad,alimento,color,caracter,tamaño):
                Especie.__init__(self,nombre,edad,alimento)
                self.color = color
                self.caracter = caracter
                self.tamaño = tamaño
        pass

class Crustaceos(Especie):

        def __init__(self,nombre,edad,alimento,tamaño,patas,color):
                Especie.__init__(self,nombre,edad,alimento)
                self.tamaño = tamaño
                self.patas = patas
                self.color = color
        pass
