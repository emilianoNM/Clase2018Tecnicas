a = int(input('Introduce un numero: '))
b = int(input('Introduce otro numero: '))
 
print ('¿Que operacion desea hacer?')
print ('a) Sumar')
print ('b) Restar')
print ('c) Multiplicar')
print ('d) Dividir')
 
 
opcion = input('Elija una opcion ---> ')
if opcion == 'a':
    suma = a + b
    print ('El resultado es ', suma)
 
if opcion == 'b':
    resta = a - b
    print ('El resultado es ', resta)
 
if opcion == 'c':
    multi = a * b
    print ('El resultado es ', multi)
 
if opcion == 'd':
    divi = a / b
    print ('El resultado es ', divi)

     
