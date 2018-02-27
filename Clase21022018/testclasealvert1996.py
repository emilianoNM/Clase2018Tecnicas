import Clase

#Creamos un elemento
alberto=Clase.Alumno("Alberto","21","1.69",["Lu","Ma","Mi","Ju","Vi"])

#Muestra los metodos de EL ELEMENTO CREADO, ['__metodos__','atributos']
print (dir(alberto))  #['__doc__', '__init__', '__module__', 'asistencia', 'calificacion', 'edad', 'estatura', 'horario', 'nombre', 'tareas']

#Nos dice que tipo de modulo es
print(type(alberto))  #<type 'instance'>

#Creamos otro elemento
emiliano=Clase.Profesor("Emiliano","29","1.79")

#imprimimos desde el metodo

print(emiliano.tienehambre())


emiliano.asignarTarea(alberto,"Tecnicas de Programacion")

alberto.tareas[0].setCalificacion(9)
alberto.tareas[0].dimeTarea()

emiliano.asignarTarea(alberto,"Tecnicas de Programacion")

alberto.tareas[1].setCalificacion(10)
alberto.tareas[1].dimeTarea()



