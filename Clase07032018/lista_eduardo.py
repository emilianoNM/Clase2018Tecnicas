print("\nArticulos Disponibles:")
print("\Guanabana\nCiruela\nPapaya\nFrambuesa\nZarzamora\nHigo\nUva\nMelocoton\nKaki")

lista_de_frutas=[]

def Pedido(x):
  lista_de_frutas.append(x)
pass

def Lista():
  print ("\nLista de articulos:\n", lista_de_frutas)
pass

def Entrega():
  print("\nArticulo\nPedido\n")
  G=lista_de_frutas.count("Guanabana")
  print ("\nGuanabana\t\t", G)
  C=lista_de_frutas.count("Ciruela")
  print ("\nCiruela\t\t", C)
  P=lista_de_frutas.count("Papaya")
  print ("\nPapaya\t\t", P)
  F=lista_de_frutas.count("Frambuesa")
  print ("\nFrambuesa\t\t", F)
  Z=lista_de_frutas.count("Zarzamora")
  print ("\nZarzamora\t\t", Z)
  H=lista_de_frutas.count("Higo")
  print ("\nHigo\t\t", H )
  U=lista_de_frutas.count("Uva")
  print ("\nUva\t\t", U)
  M=lista_de_frutas.count("Melocoton")
  print ("\nMelocoton\t\t", M)
  Key=lista_de_frutas.count("Kaki")
  print ("\nKaki\t\t", Key)
  print("\n")
