#the_last_word

#python 2.7
with open('the_last_word-small-practice.in','r') as f:
    numero_de_casos=int(f.readline())
    carga=f.readlines()

def palabraFinal(d):
  if len(d) == 0:
    return ''
  ultimaLetra = 'A'
  posicionUltima = 0
  palabra = palabraFinal(d[:posicionUltima])
  
  for i in range(len(d)):
    if d[i] > ultimaLetra:
      ultimaLetra = d[i]
      posicionUltima = i

  for i in d[posicionUltima:]:
    if i == ultimaLetra:
      palabra = i + palabra
    else:
      palabra = palabra + i
  return palabra

for i in range(numero_de_casos):
  print "Caso #" + str(i+1) + ": " + palabraFinal(carga[i].strip())