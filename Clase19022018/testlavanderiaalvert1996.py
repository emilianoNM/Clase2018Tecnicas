#ALberto Garcia SAlazar

import lavanderiaalvert1996

S210=lavanderiaalvert1996.Lavadora("S210","gris","electronica","$7,500 pesos","13 litros","azul","'borrego'")
S321=lavanderiaalvert1996.Lavadora("S321","gris","electronica","$8,600 pesos","13 litros","azul","'borrego'")
L234=lavanderiaalvert1996.Secadora("L234","gris","electronica","$4,5000 pesos","10 kilogramos","30 minutos","automatico")

Carlos=lavanderiaalvert1996.usuario("Carlos","25 anos")
Carlos.accionalav(S210,"gris")


S210.elemento3[0].tiempo(10)
S210.elemento3[0].caracteristica()

Marian=lavanderiaalvert1996.usuario("Marian","29 anos")
Marian.accionalav(S321,"gris")

S321.elemento3[0].tiempo(29)
S321.elemento3[0].caracteristica()

Paola=lavanderiaalvert1996.usuario("Paola","32 anos")
Paola.accionasec(L234,"gris")

L234.elemento2[0].tiempo(30)
L234.elemento2[0].caracteristica()


