import math
from sympy import *
from sympy import solve

def resolver(destino, caballos):

    ordenar_caballos = sorted(caballos, key=lambda a:a[0], reverse=True)
    B, vB = ordenar_caballos[0]

    for A, vA in ordenar_caballos[1:]:
        if vB == vA:
            B, vB = A, vA
        else:
            
            x = (vB * A - vA * B)/ (vB - vA)

            if x > destino or x < A:
                B, vB = A, vA

    tB = (destino - B)/ vB
    vYo = destino / tB
    print (Vyo, ordenar_caballos)
    
    return vYo

def obtener_entrada(lines):
    salida=[]
    destino, otros=(0,0)
    caballos=[]
    caso_nr= 0

    for i in range(1, len(lines)):
        if not lines[i]:
            continue
        
        if otros == 0:
            destino, otros = map(int, lines[i].strip().split())
        else:
            pos_i, velocidad_i = map(int, lines[i].strip.split())
            caballos.append([pos_i, velocidad_i])
            otros -= 1

            if otros == 0:
                velocidad = resolver(destino, caballos)
                caso_nr += 1
                salida.append("Caso #{}: {}\n".format(caso_nr, velocidad))
                caballos = []
    return salida



fentrada_nombre = "A-small-1b.1.in"
fsalida_nombre = fentrada_nombre + ".out"


with open(fentrada_nombre) as fen:
    
    with open(fentrada_nombre, "w") as fsa:
        fsa.writelines(obtener_entrada(fen.readlines()))
        print ("Registrado en {}".format(fsalida_nombre))
