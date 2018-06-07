#python 2.7
import pdb
carga = open("multi-base-small-practice.in")

#aplico la iteracion
def iteracion(numero, reemplazo):
  numero_cuenta = numero
  cuenta = 0
  while numero_cuenta > 0:
    cuenta += (numero_cuenta % reemplazo)**2
    numero_cuenta /= reemplazo
  return cuenta

def happy(numero, reemplazo, parametro_nuevo):
  if numero in parametro_nuevo:
    return parametro_nuevo[numero]
  if numero == 1:
    return True
  else:
    pass
  parametro_nuevo[numero] = False
  funcion_nueva = iteracion(numero,reemplazo)

  if happy(funcion_nueva, reemplazo, parametro_nuevo):
    parametro_nuevo[numero] = True
  return parametro_nuevo[numero]

for elemento, case in enumerate(list(carga)[1:]):
  bases = map(int, case.split())
  lista=[]
  for i in range(11):
    lista.append({})
  for numero in range(2,10000000):
    if all([happy(numero, reemplazo, lista[reemplazo]) for reemplazo in bases]):
      break
  print ("Case #",elemento+1,":",numero )