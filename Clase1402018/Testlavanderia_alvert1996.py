#ALberto Garcia SAlazar

import lavanderia_alvert1996

s2102=lavanderia_alvert1996.lavado("gris","electronica","$7,500 pesos","13 litros","azul","'borrego'")

print("\nElementos: "+str(s2102))
print("Esta lavadora es "+s2102.color+" es "+s2102.tipo+" con un costo de "+s2102.costo)
print("Ocupa "+s2102.agua+" de agua, detergente "+s2102.detergente+" y suavizante de marca"+s2102.suavizante)

banca=lavanderia_alvert1996.espera("cafe","descanso","$1,300 pesos","4 personas","3","afuera")

print("\nElemento: "+str(banca))
print("Esta banca es "+banca.color+" es para "+banca.tipo+" con un costo de "+banca.costo)
print("Tiene una capacidad para "+banca.capacidadp+", hay "+banca.elementos+" y se encuentran "+banca.ubicacion)

recepcion=lavanderia_alvert1996.atencion("blanco","atencion al usuario","$3,500 pesos","3 personas","1")

print("\nElemento: "+str(recepcion))
print("Este mobiliario es "+recepcion.color+" es para "+recepcion.tipo+" con un costo de "+recepcion.costo)
print("Estan presentes "+recepcion.personas+" y solo hay "+recepcion.elementosa+" en el lugar")

sillon=lavanderia_alvert1996.espera("negro","descanso","$4,500 pesos","3 personas","2","adentro")

print("\nElemento: "+str(sillon))
print("Este sillon es "+sillon.color+" es para "+sillon.tipo+" con un costo de "+sillon.costo)
print("Tiene una capacidad para "+sillon.capacidadp+", hay "+sillon.elementos+" y se encuentran "+sillon.ubicacion+" del lugar")

sle21=lavanderia_alvert1996.secado("blanca","electronica","$6,400 pesos","10 kilos","30 minutos","automaico")

print("\nElemento: "+str(sle21))
print("Esta secadora es "+sle21.color+", "+sle21.tipo+" con un costo de "+sle21.costo)
print("Tiene una capcidad de "+sle21.capacidad+" y su tiempo de trabajo es de "+sle21.tiempo+" con su modo "+sle21.modo)
