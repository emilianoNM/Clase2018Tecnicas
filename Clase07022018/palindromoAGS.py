print("Palindromo")

frase=raw_input("Deme algo para validar como palindromo: ")

#.replace reemplaza los valores de 1 por 2 .replace('1','2')

frase1=frase.lower().replace(' ','')

letras=len(frase1)
b=0

if letras % 2 == 0:
	print("La validacion concluye que '"+str(frase)+"' NO es un palindromo")

else:
	for i in range(letras):
		num=(letras-1)-i
		if frase1[i] == frase1[num]:
			b=b+1
		else:
			print("La validacion concluye que '"+str(frase)+"' NO es un palindromo")
			break
	if letras==b:
		print("La validacion concluye que '"+str(frase)+"' SI es un palindromo")

