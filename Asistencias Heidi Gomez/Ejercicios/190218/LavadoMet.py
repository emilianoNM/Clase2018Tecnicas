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
        def remojar(self,enjuague):
                self.enjuague=enjuague
        def desmanchar(self,condetergente):
                self.condetergente=condetergente
        def desecheagua(self,completa):
                self.completa=completa
        pass
class lavado(Servicios):

        def __init__(self,nombre,duracion,cantidad,detergente,color,ropa):
                Servicios.__init__(self,nombre,duracion, cantidad)
                self.detergente = detergente
                self.color = color
                self.ropa = ropa
        def lavado(self,detergente):
                self.detergente=detergente
        def desmanchar(self,concloro):
                self.concloro=concloro
        def completar(self,sucio):
                self.sucio=sucio
        pass

class enjuagado(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,enjuague,ropa):
                Servicios.__init__(self,nombre,duracion,cantidad)
                self.ciclo = ciclo
                self.enjuague = enjuague
                self.ropa = ropa
        def enjuagar(self,agua):
                self.agua=agua
        def completar(self):
                self.
        pass

class exprimido(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,color,ropa):
                Serivicios.__init__(self,nombre,duracion, cantidad)
                self.ciclo = ciclo
                self.color = color
                self.ropa = ropa
        def exprimir(self):
                self.
        def completar(self):
                self.
        pass
class secado(Servicios):

        def __init__(self,nombre,duracion,cantidad,ciclo,ropa, intensidad):
                Servicios.__init__(self,nombre,duracion, cantidad)
                self.ciclo = ciclo
                self.ropa = ropa
                self.intensidad = intensidad
        pass
