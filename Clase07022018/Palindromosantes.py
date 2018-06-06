# Santes Mejia Antonio
print "...Tecnicas de programacion.."
print("Palindromo")

a = raw_input("Ingrese la palabra\n\n")

a = a.replace(" ","")
if a.islower()==False:
    a=a.lower()
b=a[::-1]
if b==a:
    print("a:"+str(palindromo)+"es un palindromo")
else:
    print("b:"+str(palindromo)+"no es palindromo")

  
