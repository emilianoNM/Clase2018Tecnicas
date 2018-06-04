import sys

Nombre_Archivo = "C-small-practice.in"
Archivo_Entrada= open ("C-small-practice.in", 'r' )
Archivo_Salida= open ("Calculos " + Nombre_Archivo, 'w')
Entrada = int(Archivo_Entrada.readline().strip())

Caidas = 100
Rotos = 100
MaxPosibilidad =21474836470
Fuera_Piso = MaxPosibilidad 

Piso = [[-1 for i in range(Rotos+1)] for j in range(Caidas+1)]

def Inicio():

    FF(Caidas, Rotos)

def FF(D, B):
       
    for d in range(1, D+1):
        b = 1; Piso[ d ][ b ] = d
        b = 2; Piso[ d ][ b ] = d * (d + 1) / 2
        b = 3; Piso[ d ][ b ] = d * (d * (d + 0) + 5) / 6
        b = 4; Piso[ d ][ b ] = d * (d * (d * (d - 2) + 11) + 14) / 24
        for b in range(b+1, B+1):
            sibPiso = Piso[ d - 1 ][ b - 1 ]
            nobPiso = Piso[ d - 1 ][ b ]
            
            if (sibPiso == Fuera_Piso) | (nobPiso == Fuera_Piso):
                Piso[ d ][ b ] = Fuera_Piso
                continue
            
            Siguiente_Piso = 0
            if (b < d):
                Siguiente_Piso = sibPiso + nobPiso + 1
            elif (b == d):
                Siguiente_Piso = (1 << d) - 1
            else:
                Siguiente_Piso = Piso[ d ][ b - 1 ]

            if (Siguiente_Piso >= MaxPosibilidad):
                Siguiente_Piso = Fuera_Piso
                
            Piso[ d ][ b ] = Siguiente_Piso
    
    return Piso[ d ][ b ]

def Factores(n):
    n = abs(int(n))
    if (n == 0 | n == 1):
        return 1
    if (n == 2):
        return 2
    if (n == 3):
        return 6

    x = 1
   
    for i in range(n, 1, -1):
        x *= i
    
    return x

def Cambiar(n, r):
    n = abs(int(n))
    r = abs(int(r))
    if (n < r):
        return 0
    if (n == 0 | n == 1):
        return 1
    if (r == 0):
        return 1
    if (r == 1):
        return n
    if (r == n-1):
        return Factores(n)
    if (r == n):
        return Factores(n)

    x = 1

    for i in range(n, n-r, -1):
        x *= i    
    
    return x

def Combinar(n, r):
    n = abs(int(n))
    r = abs(int(r))
    if (n < r):
        return 0
    if (n == 0 | n == 1):
        return 1
    if (r == 0 | r == n):
        return 1
    if (r == 1 | r == n - 1):
        return n

    if (r > n / 2):
        r = n - r

    return Cambiar(n, r) / Factores(r)

def F_max(D, B):
    maxF = 0

    if (D > Caidas):
        return 0
    if (B > Rotos):
        B = Rotos

    if (B == 0):
        return 0
    if (B == 1):
        return D
    if (B == 2):
        return D * (D + 1) / 2
    if (B == 3):
        return D * (D * (D + 0) + 5) / 6
    if (B == 4):
        return D * (D * (D * (D - 2) + 11) + 14) / 24

    maxF = Piso[ D ][ B ]

    return maxF

def D_min(F, maxD, B):
    if (B == 1):
        return F

    min = 0
    max = maxD
    while (max - min > 1):
        mid = int((max + min) / 2)
        maxF = F_max(mid, B)

        if (F > maxF):
            min = mid
        else:
            max = mid
    minD = max
   
    return minD

def B_min(F, D, maxB):

    min = 0
    max = maxB
    while (max - min > 1):
        mid = int((max + min) / 2)
        maxF = F_max(D, mid)

        if (F > maxF):
            min = mid
        else:
            max = mid

    minB = max

    return minB

if (__name__ == "__main__"):
    Inicio()

for i in range(1, Entrada+1):
    Fila = Archivo_Entrada.readline().strip()
    F, D, B = map(int, Fila.split())
    FMAX =str(F_max(D, B))
    DMIN =str(D_min(F, D, B))
    BMIN =str(B_min(F, D, B))
    I = str(i)
        
    print ("Caso {}: {}   {}   {}".format(I, FMAX, DMIN, BMIN))
    Archivo_Salida.write("Caso {}: {}   {}   {} \n".format(I, FMAX, DMIN, BMIN))

Archivo_Entrada.close()
Archivo_Salida.close()
