print("Palindromo")

palindromo = input("Dame una palabra")

frase=palindromo.replace(" ","")
if frase.islower()==False:
    frase=frase.lower()
frase_invertida=frase[::-1]
if frase_invertida==frase:
    print("la frase:"+str(palindromo)+"es un palindromo")
else:
    print("la frase:"+str(palindromo)+"no es palindromo")

  
