#Benjamin Cruz Sarmiento

import claseBCS

Oliver=claseBCS.Alumno("Oliver","21","1.69",["L","M"])
print(dir(Oliver))
print(type(Oliver))


Emiliano=claseBCS.Profesor("Emiliano","29","1.75")
print(Emiliano.tieneHambre())
print(Emiliano)
Emiliano.asignarTarea(Oliver,"Matematicas")


Oliver.tareas[0].setCalificacion(8)
Oliver.tareas[0].imprimirTarea()
