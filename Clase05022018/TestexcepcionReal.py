import  excepcionReal

try:
    Persona1=excepcionReal.Persona("Emiliano2")
except Exception:
    print "Persona 1 no se pudo crear"
finally:
    print "siempre se ejecuta"
try:
    Persona2=excepcionReal.Persona("Emiliano","profesor")
except Exception:
    print "persona 2 no se pudo crear "
finally:
    print "siermpre se ejecuta"

print Persona2

try:

    print Persona1
    print Persona2, Persona1
except Exception, e:

    print e

