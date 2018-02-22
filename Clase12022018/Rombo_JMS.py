#Meneses Silva Maximino Javier
print("Este programa imprime un Rombo")
print ("")
dim=int(input("introduce un numero:"))
if dim<=2:
 print("El rombo no puede ser dibujado, es muy pequeño")

else:
 for i in range (dim,0,-1):
    for j in range(dim,(dim-(i+1)),-1):
        print(" ",end= "")
    for k in range (i+1,dim+1):
        print("*",end= "") 
    print("")
 for i in range(0,dim):

     for j in range(dim,(dim-(i+1)),1):

          print(" ", end="")
 
     for k in range(i+1,dim+1):

          print("*",end="")

     print("")
