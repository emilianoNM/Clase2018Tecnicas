class Persona():
  
    def __init__(self):
      self.nombre=str(input("Ingrese nombre del alumno a calificar:"))
      self.edad=str(input("Ingrese su edad:"))
      self.estatura=str(input("Ingrese su estatura:"))
      
    def __str__(self):
      print("Datos del alumno a calificar:")
      return "Nombre:"+self.nombre + " " + "Edad:"+self.edad +" "+ "estatura"+self.estatura
    
    def imprimir(self):
      print (str(self))
  
class Alumno(Persona):
    tareas=[]
    
    def __init__(self):
      super().__init__()
      print("")
      
    def imprimirIngreso(self):
      super().imprimir()
      print("")
      
    def menu(self):
          opcion=0
          while opcion!=4:
              print(" Selecciona la tarea que deseas calificar:")
              print("1- Investigacion de Linux")
              print("2- Investigacion de Windows")
              print("3- Investigacion de Mac")
              opcion=int(input("Ingrese su opcion:"))
              if opcion==1:
                  self.cargarTarea1()
                  break
              elif opcion==2:
                  self.cargarTarea2()
                  break
              elif opcion==3:
                  self.cargarTarea3()
                  break
                  
    def cargarTarea1(self):
      tarea1="Investigacion de Linux"
      Alumno.tareas.append(tarea1)
    def cargarTarea2(self):
      tarea2="Investigacion de windows"
      Alumno.tareas.append(tarea2)
    def cargarTarea3(self):
      tarea3="Investigacion de Mac"
      Alumno.tareas.append(tarea3)
    def mostrarTarea(self):
      print("Tarea:",*Alumno.tareas)
  
  
class Tareas():
    calificacion=[]
      
    def __init__(self):
      self.cal=int(input("ingrese la calificacion de la tarea:"))
      if self.cal>0 and self.cal<=10:
        print("")
        print(self.cal,"calificacion valida.")
        Tareas.calificacion.append(self.cal)
        print("")
      else:
        print("\nError\n")
      
class Profesor(Tareas,Alumno):
  
  def __init__(self,nom,mat,su):
    #duda aqui
    super().calificacion
    super().tareas
    self.nombre=nom
    self.materia=mat
    self.sueldo=su
    
  def __str__(self):
    cadena= "Nombre del Profesor:" + self.nombre +"\n"+ "Materia:" +self.materia +"\n"+ "Paga por calificar esta materia: $"+ self.sueldo
    return cadena
    
  def resumen(self):
    print("----Tarea----")
    print(*Alumno.tareas)
    print("----Calificacion asignada----")
    print(*Tareas.calificacion)
    print("----Datos del profesor----")
    print(str(self))
    
    
#BlOQUE
print("___________________")
Alumno1=Alumno()
Alumno1.imprimirIngreso()
Alumno1.menu()
Alumno1.mostrarTarea()
Tarea1=Tareas()
profesor1=Profesor("Emiliano","Tecnicas de Programacion","5")
profesor1.resumen()
    