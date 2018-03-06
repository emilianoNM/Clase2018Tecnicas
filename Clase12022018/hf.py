print "Tecnicas de programacion"
print "Mendieta Montoya Oliver Salvador"
print "Usuario github OliverMendieta\n"

print "Hora futura"

import time
import datetime


print ("La hora actual es\n")
formato = "%X"
Hora_Actual = time.strftime (formato)
print (Hora_Actual)

print("Ingresa la hora que deseas sumar \n ")
hora = int(input("Dame una hora"))
mi = int(input("Dame los minutos"))
seg = int(input("Dame los segundos"))

Hora = datetime.timedelta(hours=hora,minutes=mi,seconds=seg)
print (Hora)

Hora_futura = Hora_Actual + timedelta(hours=hora,minutes=mi,seconds=seg)
print (Hora_futura)
