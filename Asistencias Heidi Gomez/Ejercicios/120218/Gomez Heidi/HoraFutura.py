#Heidi Gomez
#Ejercicio de Hora Futura

print "****Programa que calcula la hora futura****"
print "\n Deberas escribir la hora actual separados los digitos pur un punto en vez de dos\n"


hora_actual = float(input("Escribe la hora actual: "))
print("")

cantidad_horas = int(input("Cantidad de horas que trascurren: "))

hora_futura = (hora_actual + cantidad_horas) % 24

print("")
print "En "+str(cantidad_horas)+" horas, el reloj marcara las "+str(hora_futura)
