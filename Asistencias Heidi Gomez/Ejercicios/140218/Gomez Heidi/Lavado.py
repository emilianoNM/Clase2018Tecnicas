#Laura Gomez
#Creando un cuarto de lavado

class Servicios:

        def __init__(self,nombre,duracion,cantidad):
            self.nombre = nombre
            self.duracion = duracion
            self.cantidad = cantidad        
        
        pass

class remojado(Servicios):

        def __init__(self,nombre,duracion,cantidad,detergente,color,ropa):
                Servicios.__init__(self,nombre,duracion, cantidad)
                self.detergente = detergente
                self.color = color
                self.ropa = ropa
        pass
class lavado(Servicios):

        def __init__(self,nombre,duracion,cantidad,detergente,color,ropa):
                Servicios.__init__(self,nombre,duracion, cantidad)
                self.detergente = detergente
                self.color = color
                self.ropa = ropa
        pass

class enjuagado(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,enjuague,ropa):
                Servicios.__init__(self,nombre,duracion,cantidad)
                self.ciclo = ciclo
                self.enjuague = enjuague
                self.ropa = ropa
        pass

class exprimido(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,color,ropa):
                Serivicios.__init__(self,nombre,duracion, cantidad)
                self.ciclo = ciclo
                self.color = color
                self.ropa = ropa
        pass
class secado(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,ropa, intensidad):
                Servicios.__init__(self,nombre,duracion, cantidad)
                self.ciclo = ciclo
                self.ropa = ropa
                self.intensidad = intensidad
        pass
