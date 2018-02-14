print("Identificador de palindromos")

frase = input("Por favor ingrese una frase: ")

frase_sin_espacios = frase.replace(" ","")

if frase_sin_espacios.islower() == False:
	frase_sin_espacios = frase_sin_espacios.lower()

frase_invertida = frase_sin_espacios[::-1]

if frase_invertida == frase_sin_espacios:
	print("La frase: "+str(frase)+" es un palindromo.")

else:
	print("La frase: "+str(frase)+" no es un palindromo.")
