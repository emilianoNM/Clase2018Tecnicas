while True:
    try:
        x=int(input("dame un numero: "))
        break
    except  Exception ,e:
        print ("No es un numero")
        print type(e)

