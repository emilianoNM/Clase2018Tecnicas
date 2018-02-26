#Meneses Silva Maximino Javier

import ClaseMJMS
 
Oliver=ClaseMJMS.Alumno("Oliver",21,1.69,["L","M","Mi","J","V"])

print(dir(Oliver))

print(type(Oliver))

Emiliano=ClaseMJMS.Profesor("Emiliano",29,1.75)

print(Emiliano.tieneHambre())

Emiliano.asignarTarea(Oliver,"Matematicas")

Oliver.tareas[0].setCalificacion(8) 
Oliver.tareas[0].imprimirTarea()
