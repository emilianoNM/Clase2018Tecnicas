# Calculadora 07 Febrero 2018
print('Diana Laura Vega Soto')

print('CALCULADORA')
print('Elige una opcion')
print('1.-Suma')
print('2.-Resta')
print('3.-Multiplicacion')
print('4.-Division')
print('5.-Potencia')
print('6.-Salir')

a = input('Escribe tu eleccion:')
b = float(a)

if (b==1):
     x =input('Introduce un numero\n')
     y =input('Introduce otro numero\n')
     x2=float(x)
     y2=float(y)
     res= x2+y2
     print('El resultado de la suma es:', res)

elif(b==2):
     x =input('Introduce un numero\n')
     y =input('Introduce otro numero\n')
     x2=float(x)
     y2=float(y)
     res= x2-y2
     print('El resultado de la resta es:', res)

elif(b==3):
     x =input('Introduce un numero\n')
     y =input('Introduce otro numero\n')
     x2=float(x)
     y2=float(y)
     res= x2*y2
     print('El resultado de la Multiplicacion es:', res)

elif(b==4):
     x =input('Introduce un numero\n')
     y =input('Introduce otro numero\n')
     x2=float(x)
     y2=float(y)
     res= x2/y2
     print('El resultado de la division es:', res)

elif(b==5):
     x =input('Introduce un numero\n')
     y =input('Introduce el valor de la potencia\n')
     x2=float(x)
     y2=float(y)
     res= x2**y2
     print('El resultado es:', res)

elif(b==6):
     print('Adios')

else:

    print('Numero Invalido')
     
