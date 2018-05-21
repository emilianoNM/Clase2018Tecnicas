numero = int(input('Introduce un numero ---> '))
numero2 = int(input('Introduce otro numero ---> '))
 
print ('Que operacion desea hacer?')
print ('a) Sumar')
print ('b) Restar')
print ('c) Multiplicar')
print ('d) Dividir')
 
 
opcion = input('Elija una opcion ---> ')
if opcion == 'a':
    suma = numero + numero2
    print ('Calculando...')
    print ('El resultado es ', suma)
 
if opcion == 'b':
    resta = numero - numero2
    print ('Calculando...')
    print ('El resultado es ', resta)
 
if opcion == 'c':
    multi = numero * numero2
    print ('Calculando...')
    print ('El resultado es ', multi)
 
if opcion == 'd':
    divi = numero / numero2
    print ('Calculando...')
    print ('El resultado es ', divi)