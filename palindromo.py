print("===Identificador de palindromos===")
class Cadenas:

    def __init__ (self, cad1):

        self.cad1=cad1

 

    def Pal(self):

        cad1 = self.cad1

        c,i,nom,cad,x = 0,0,'','',''

        i = len(cad1)

        nom = cad1.lower()

        while i != c:

            for x in nom:

                cad = x + cad

                c=c+1

            if nom==cad:

                #print (cad1, " Es Palindromo")

                return str(cad1 + " Es Palindromo")

            else:

                #print (cad1, " No es Palindromo")

                return str(cad1 + " No es Palindromo")

 

cad1 = input('Dame una palabra: ')

op1=Cadenas(cad1)

 

#op1.Pal()#Impresion de la funcion

print(op1.Pal())
