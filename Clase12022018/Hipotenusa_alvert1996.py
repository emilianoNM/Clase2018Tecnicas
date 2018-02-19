#Alberto Garcia Salazar
print("Vamos a utilizar el teorema de pitagoras, recuerda que para su aplicacion debe ser un trignaulo rectangulo")
print "  # "
print "  ##"
print "a # # c"
print "  #"+" "*(2)+"#"
print "  "+"#"*(5)
print " "*(4)+"b"
a=float(input("\ndame el valor del cateto a: "))
b=float(input("dame el valor del cateto b: "))

c=(pow(a,2)+pow(b,2))**0.5

print "\nLa hipotenusa o valor de c es: ",c 

print "     # "
print "     ##"
print "",round(a,1),"# # ",round(c,3)
print "     #"+" "*(2)+"#"
print "     "+"#"*(5)
print " "*(4)+" ",round(b,1)
