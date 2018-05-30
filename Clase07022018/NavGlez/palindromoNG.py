print('Es o no es palindromo')

f = input ('Ingresa un numero:')
f_s_e = f.replace(" ","")

if f_s_e.islower()==False:
	f_s_e = f_s_e.lower()

n_i = f_s_e[::-1]

if n_i == f_s_e:
	print("El numero es:" +f+" es un palindromo")

else:
	print("el numero: "+str(f)+" no es palindromo")