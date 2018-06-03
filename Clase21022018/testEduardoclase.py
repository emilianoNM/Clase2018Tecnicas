import clase

eduardo=clase.Alumno("eduardo", 21, 169, ["L","M","Mi","J","V"])
print (dir(eduardo))  #['__doc__', '__init__', '__module__', 'asistencia', 'calificacion', 'edad', 'estatura', 'horario', 'nombre', 'tareas']
print(type(eduardo)) 

Emiliano=clase.Profesor("Emiliano", 29, 175)
print(Emiliano.tienehambre())

Emiliano.asignarTarea(eduardo, "tecnicas de programacion")

eduardo.tareas[1].setCalificacion(8)

eduardo.tareas[1].imprimirTarea()
