#Funcional en python, no python3

print("\nArticulos disponibles:\nMandarina\nSandia\nNaranja\nManzana\nUva\nMelon\nDurazno\nToronja\nMango\n")

lista=[]

def Pedido(x):
  lista.append(x)
pass

def Lista():
  print "\nLista de articulos:\n", lista
pass

def Entrega():
  print("\nArticulo\tCantidad pedida\n")
  Ma=lista.count("Mandarina")
  print "\nMandarina\t", Ma
  San=lista.count("Sandia")
  print "\nSandia\t\t", San
  Nar=lista.count("Naranja")
  print "\nNaranjas\t", Nar
  Man=lista.count("Manzana")
  print "\nManzanas\t", Man
  Uv=lista.count("Uva")
  print "\nUva\t\t", Uv
  Mel=lista.count("Melon")
  print "\nMelon\t\t", Mel 
  Dur=lista.count("Durazno")
  print "\nDurazno\t\t", Dur
  Tor=lista.count("Toronja")
  print "\nToronja\t\t", Tor
  Mng=lista.count("Mango")
  print "\nMango\t\t", Mng
  print("\n")
