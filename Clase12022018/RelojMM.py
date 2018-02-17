#Programa hecho por Mario Molina

print("")
print ("Calculemos que hora sera en x numero de horas a partir de la hora actual")
print("")

hora_actual_t = float(input("Cual es la hora actual: "))
print("")
horas_transcurren_h = int(input("Cantidad de horas que trascurren: "))

hora_futura = (hora_actual_t + horas_transcurren_h) % 24

print("")
print "En "+str(horas_transcurren_h)+" horas, el reloj marcara las "+str(hora_futura)
