import pickle
import clases_persistencia_yaxkin09

Magnolia=clases_persistencia_yaxkin09.Lince("Magnolia", "Bosque", 8)
Yew=clases_persistencia_yaxkin09.Zorro("Yew", "Tundra", 10)
Edea=clases_persistencia_yaxkin09.Pinguino("Edea", "Glaciar", 9)

Magnolia.Save("datos_yaxkin09.dat")
Yew.Save("datos_yaxkin09.dat")
Edea.Save("datos_yaxkin09.dat")

Magnolia.Load("datos_yaxkin09.dat")
Yew.Load("datos_yaxkin09.dat")
Edea.Load("datos_yaxkin09.dat")