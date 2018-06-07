#python 2.7
import collections
import sys
import itertools

caminar_norte = (0, 1)
caminar_sur = (0, -1)
caminar_oeste = (-1, 0)
caminar_este = (1, 0)
haycamino_norte = 0x01
haycamino_sur = 0x02
haycamino_oeste = 0x04
haycamino_este = 0x08

def caminar_laberinto(laberinto, trayectoria, posicion, direccion):
  x, y = posicion
  for c in trayectoria:
    coordenada = (x, y)
    if c == 'R':
        direccion = (direccion[1], -direccion[0])
    if c == 'L':
        direccion = (-direccion[1], direccion[0])
    if c == 'W':
      if direccion == caminar_norte:
          chance_de_avanzar = haycamino_norte
      elif direccion == caminar_oeste:
          chance_de_avanzar = haycamino_oeste
      elif direccion == caminar_sur:
          chance_de_avanzar = haycamino_sur
      elif direccion == caminar_este:
          chance_de_avanzar = haycamino_este

      laberinto[coordenada] |= chance_de_avanzar
      x += direccion[0]
      y += direccion[1]
  return direccion, coordenada

def funcion (entrada, salida):
    solucion = []
    laberinto = collections.defaultdict(lambda: 0)
    direccion, posicion = caminar_laberinto(laberinto, entrada[1:], (0, -1), (0, -1))
    caminar_laberinto(laberinto, salida[1:], posicion, (-direccion[0], -direccion[1]))

    ordenar = lambda ((x, y), chance_de_avanzar): (-y, x)
    agrupar = lambda ((x, y), chance_de_avanzar): y
    for key, group in itertools.groupby(sorted(laberinto.items(), key=ordenar), agrupar):
        solucion.append(''.join(['{0:x}'.format(chance_de_avanzar[1]) for chance_de_avanzar in group]))
    return '\n'.join(solucion)


if __name__ == "__main__":
    numero_de_casos = int(sys.stdin.readline())
    for elemento in xrange(1, numero_de_casos + 1):
        entrada, salida = sys.stdin.readline().split()
        print 'Case #{0}:\n{1}'.format(elemento, funcion(entrada, salida))