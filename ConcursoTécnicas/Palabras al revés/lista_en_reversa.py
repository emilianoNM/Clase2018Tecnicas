def delimitadores(string):

    secuencia_lista = list()

    espacio = 0
    while string[espacio] == " ":
        espacio += 1

    ult_delimit = espacio - 1
    
    for i in range(espacio, len(string)):

        if i == len(string) - 1:
            secuencia_lista.append(string[ult_delimit + 1:i + 1])

        if string[i] == " ":
            secuencia_lista.append(string[ult_delimit + 1:i])
            ult_delimit = i

    return secuencia_lista


def intercambiar(l, a, b):

    
    tempo = l[a]
    l[a] = l[b]
    l[b] = tempo


secuencia_test = list()
secuencia_test.append("Programa para mostrar palabras en reversa")
secuencia_test.append("La puesta de sol fue maravillosa")
secuencia_test.append("Nada como una platica de noche en la playa")
secuencia_test.append("El maestro Yoda se queda corto")
secuencia_test.append("Hora de salvar el semestre")

for string in secuencia_test:

    l = delimitadores(string)
    L = len(l)
    Mitad = int(L/2)

    for i in range(0, Mitad):  

        intercambiar(l, i, L - i - 1)

    print (l)
