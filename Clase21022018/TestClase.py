import Clase
 
Oliver=Clase.Alumno("Oliver",21,1.69,["L","M","Mi","J","V"])

print(dir(Oliver))

print(type(Oliver))

Emiliano=Clase.Profesor("Emiliano",29,1.75)

print(Emiliano.tieneHambre())

Emiliano.asignarTarea(Oliver,"Matematicas")

Oliver.tareas[0].setCalificacion(8) 
Oliver.tareas[0].imprimirTarea()
