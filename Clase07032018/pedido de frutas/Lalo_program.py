print("\nArticulos disponibles:")
print("Naranja\nBrocoli\nPera\nFresa\nKiwi\nDurazno\nPlatano\nMango")
frutalista=[]

def Pedido(x):
  frutalista.append(x)

def Lista():
  print ("\nLista de articulos:\n", frutalista)

def Entrega():
  print("\nArticulo----Cantidad pedida")
  Na=frutalista.count("Naranja")
  print ("Naranjas\t", Na)
  Bro=frutalista.count("Brocoli")
  print ("Brocoli\t\t", Bro)
  Per=frutalista.count("Pera")
  print ("Pera\t\t", Per)
  Fre=frutalista.count("Fresa")
  print ("Fresa\t\t",Fre )
  Ki=frutalista.count("Kiwi")
  print ("Kiwi\t\t", Ki)
  Dur=frutalista.count("Durazno")
  print("Durazno\t\t", Dur )
  Pla=frutalista.count("Platano")
  print ("Platano\t\t", Pla)
  Man=frutalista.count("Mango")
  print ("Mango\t\t", Man)
  print("\n")
