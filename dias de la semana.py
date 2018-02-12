print("==Dias de la semana==")
Dia=["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
d=int(input("ingresa un numero\n"))
if(d >= 1 and d <= 7):
 print("el dia " + str(d) + " es " + Dia[d - 1])
else:
print("No es un dia de la semana")
