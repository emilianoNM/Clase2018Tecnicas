#Hernández Alvarado Miguel Kam Yaxkin

class Autor:
  Titulo=None
  Estado=None
  Genero=None
  
class Leon_Tolstoi(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Duracion(self):
    print("\n",str(self), " es un libro muy largo")
    
  def Personajes(self):
    print("\nHay cerca de 200 personajes en ",str(self))
    
  def Critica(self):
    print("\nEn ", str(self), " critica la situación de Rusia en la era de Napoleón")
     
class Victor_Hugo(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Critica(self):
    print("\n", str(self), " contiene varias crítica sobre la sociedad francesa")
    
  def Epoca(self):
    print("\nAl parecer la historia de ", str(self), " sucede en el siglo XIX")
    
  def Narrativa(self):
    print("\n", str(self), " utiliza una narrativa sencilla")
      
class Diana_Wynne_Jones(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Pelicula(self):
    print("\nEstudio Ghibli adapto ", str(self), " con muchos cambios, pero no perdi el sentido de la historia")
    
  def Comedia(self):
    print("\nLa versión original de ", str(self), " es mas cómica que la película")
    
  def Idea(self):
    print("\nLa idea original para ", str(self), " fue propuesta por un niño a la autora")
      
class Stephen_Hawking(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Solicitudes(self):
    print("\n", str(self), " es un libro muy solicitado")
    
  def Divulgacion(self):
    print("\n", str(self), " motiva la curiosidad de los lectores por la física")
    
  def Contemporaneo(self):
    print("\nAL igual que otros libros de Hawking, ", str(self), " es un excelente acercamiento a la física contemporanea")
      
class Isaac_Asimov(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Eventos(self):
    print("\n", str(self), "puede realizar cierta crítica sobre los eventos de la época en que se publicó")
    
  def Tiempo(self):
    print("\n", str(self), " es de agradao para aquellos con gusto por las historias futuristas")
    
  def Personajes(self):
    print("\nTodos los personajes de ", str(self), " son memorables y relevantes en toda la historia")
      
class Orson_Welles(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Estadistica(self):
    print("\n ", str(self), " Es una pequeña investigación sobre las reacciones ante una historia de cienca ficción por el radio")
    
  def Evento(self):
    print("\n", str(self), " describe la reacción de pánico generaizado por parte del publico")
    
  def Guion(self):
    print("\nEl libro ", str(self), " incluye el guion radiofónico que asusto a la gente")
      
class Eduardo_Galeano(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Microcuento(self):
    print("\nEl formato de  ", str(self), " es el microcuento")
    
  def Anecdotas(self):
    print("\nVarias narraciones incluidas en ", str(self), " son anecdotas del autor")
    
  def Contemporaneo(self):
    print("\n", str(self), " es característico de las últimas décadas del siglo XX")
      
class Michael_Spivak(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Formalidad(self):
    print("\n", str(self), "Es un excelente recurso para las matemáticas formales")
    
  def Lectores(self):
    print("\nLa mayoría de los lectores de ", str(self), " son estudiantes de matemáticas")
    
  def Popularidad(self):
    print("\nMuchos recuerdan ", str(self), " por dejar las demostraciones como ejercici para el lector")
      
class Jose_Emilio_Pacheco(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Contemporaneo(self):
    print("\n", str(self), " es una recopilación de poemas a lo largo de la carrera del autor")
    
  def Edicion(self):
    print("\nUna edición de ", str(self), " se publico como regalo con una revista científica")
    
  def Tematica(self):
    print("\nLos temas tratados en ", str(self), " son variados")
      
class Ovidio(Autor):
  def __init__(self, Titulo, Estado, Genero):
    self.Estado=Estado
    self.Titulo=Titulo
    self.Genero=Genero
    
  def __str__(self):
    return self.Titulo
  
  def Popularidad(self):
    print("\nPor algún motivo ", str(self), " es popular entre estudiantes de preparatoria")
    
  def Antiguedad(self):
    print("\nA pesar de que ", str(self), " se publico hace mucho tiempo, se considera vigente")
    
  def Escolar(self):
    print("\nVarios profesores de literatura incluyes ", str(self), " en sus programas")