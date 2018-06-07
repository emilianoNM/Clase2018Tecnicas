#python 2.7
#idioma1 e idioma2 son el lenguaje fuente y el lenguaje objetivo respectivamente
#con base1 y base2 fijamos el lenght del "lenguaje fuente" y el "lenguaje objetivo " 
#numeros1 son los numeros en el lenguaje fuente
#numeros2 es la lista en donde almacenaremos los numeros a convertir en el lenguaje objetivo 
#n es el entero a calcular

import sys
def idiomasx (numeros1, idioma1, idioma2):
    numeros2 = []
    res = []
    largo1 = len(idioma1)
    largo2 = len(idioma2)

    for d in idioma2:
        numeros2.append(d)
   #enumero  con la funcion enumerate
    n = 0
    for elemento, d in enumerate(reversed(numeros1)):
        n += idioma1.index(d) * (largo1 ** elemento)
    while n > 0:
        res.append(n % largo2)
        n /= largo2
    #me regresa un true por lo que evalua como falso
    if not res:
        res = [0]
    return ''.join([numeros2[d] for d in reversed(res)])

if __name__ == "__main__":
    numero_de_casos = int(sys.stdin.readline())

    #enumero los casos y leo mi entrada
    for elemento in xrange(1, numero_de_casos + 1):
        numeros1, idioma1, idioma2 = sys.stdin.readline().split()
        print ('Caso #{0}: {1}'.format(elemento, idiomasx(numeros1, idioma1, idioma2)))