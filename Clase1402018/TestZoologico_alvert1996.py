#Alberto Garcia Salazar

import Zoologico_alvert1996

pancho=Zoologico_alvert1996.tucan("vivo","2","negro","Pancho","largo","largas","moderado")

print("\n"+str(pancho))
print("Nuevo integrante es: "+pancho.nombre)
print("se encuentra: "+pancho.estado)
print("edad: "+pancho.edad)
print("Caracteristicas: pico "+pancho.pico+", plumas "+pancho.pluma+" y canto "+pancho.canto)

fifi=Zoologico_alvert1996.tucan("vivo","3","negro y verde","Fifi","regular","largas","fuerte")

print("\n"+str(fifi))
print("Nuevo integrante es: "+fifi.nombre)
print("Se encuentra: "+fifi.estado)
print("Edad: "+fifi.edad)
print("Caracteristicas: pico "+fifi.pico+", plumas "+fifi.pluma+" y canto "+fifi.canto)

pupa=Zoologico_alvert1996.elefante("vivo","10","gris","Pupa","regular","aspera","hembra")

print("\n"+str(pupa))
print("Nuevo integrante es: "+pupa.nombre)
print("Se encuentra: "+pupa.estado)
print("Edad: "+pupa.edad)
print("Caracteristicas: tamano "+pupa.tamano+", piel "+pupa.piel+" y sexo "+pupa.sexo)

dumbo=Zoologico_alvert1996.elefante("vivo","23","gris","Dumbo","grande","aspera","macho")

print("\n"+str(dumbo))
print("Nuevo integrante es: "+dumbo.nombre)
print("Se encuentra: "+dumbo.estado)
print("Edad: "+dumbo.edad)
print("Caracteristicas: tamano "+dumbo.tamano+", piel "+dumbo.piel+" y sexo "+dumbo.sexo)

tiller=Zoologico_alvert1996.cocodrilo("vivo","27","verde","Tiller","regular","","")

print("\n"+str(tiller))
print("Nuevo integrante es: "+tiller.nombre)
print("Se encuentra: "+tiller.estado)
print("Edad: "+tiller.edad)
print("Caracteristicas: tamano "+tiller.tamano+", piel "+tiller.piel+" y se alimenta de "+tiller.comida)

piti=Zoologico_alvert1996.jirafa("vivo","7","amarilla y negro","Piti","yerba","suave","hembra")

print("\n"+str(piti))
print("Nuevo integrante es: "+piti.nombre)
print("Se encuentra: "+piti.estado)
print("Edad: "+piti.edad)
print("Caracteristicas: Se alimenta de "+piti.comida+", su pelaje es "+piti.piel+" y es "+piti.sexo)

mike=Zoologico_alvert1996.cocodrilo("vivo","4","verde","Mike","pequeno","","")

print("\n"+str(mike))
print("Nuevo integrante es: "+mike.nombre)
print("Se encuentra: "+mike.estado)
print("Edad: "+mike.edad)
print("Caracteristicas: tamano "+mike.tamano+", piel "+mike.piel+" y se alimenta de "+mike.comida)

elsa=Zoologico_alvert1996.hipopotamo("vivo","15","gris","Elsa","fuerte","hostil","hembra")

print("\n"+str(elsa))
print("Nuevo integrante es: "+elsa.nombre)
print("Se encuentra: "+elsa.estado)
print("Edad: "+elsa.edad)
print("Caracteristicas: Produce un sonido "+elsa.sonido+", es de caracter "+elsa.caracter+" y es "+elsa.sexo)
