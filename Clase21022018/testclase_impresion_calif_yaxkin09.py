import clase_5

Oliver=clase_5.Alumno("Oliver", 21, 169, ["L","M","Mi","J","V"])
#print(dir(Oliver))
#print(type(Oliver))

Emiliano=clase_5.Profesor("Emiliano", 29, 175)
print(Emiliano.tienehambre())

Emiliano.asignarTarea(Oliver, "Matematicas")

Oliver.tareas[0].setCalificacion(8)

Oliver.tareas[0].imprimirTarea()