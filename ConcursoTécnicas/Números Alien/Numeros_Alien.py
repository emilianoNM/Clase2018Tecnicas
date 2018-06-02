from math import pow

archivo_entrada = open ("A-small-practice.in", 'r' )
archivo_salida = open ("Descifrado " + "A-small-practice.in", 'w' )
primero = 1

for datos in archivo_entrada:
    if (primero == 1):
        primero = 0
        conteo = 1
    else:
        datos = datos.split(' ' )
        base0 = len(str(datos[1]))
        base1 = len(str(datos[2].strip()))
        longitud = len(str(datos[0]))

        numero = 0

        for i in str(datos[0]):
            numero += datos[1].index(i) * pow(base0,longitud - 1)
            longitud -= 1
        numero = int(numero)

        nuevo_numero = ""

        while numero > 0:
            nuevo_numero = str(datos[2].strip())[numero%base1] + nuevo_numero
            numero = numero/base1

        archivo_salida.write('Caso #'+str(conteo) + ': '+nuevo_numero + '\n' )
        conteo +=1

archivo_entrada.close()
archivo_salida.close()
    
