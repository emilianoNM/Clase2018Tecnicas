import lavanderiaNG

R1=lavanderiaNG.Ropa("AZUL","S","Masculino","Jorge Nava","ADIDAS")
print("Propietario: ",R1.propietario)
print("Color de la prenda: ",R1.color)
print("Talla de la prenda: ",R1.talla)
print("Marca:",R1.marca)

R2=lavanderiaNG.Detergente("PERSIL","Deportiva",95)
print("Utilizar el detergente",R2.marca)
print("Es ropa tipo ", R2.tipoderopa)
print("Costo del detergente",R2.costo,"Pesos")
print("")

R3=lavanderiaNG.Lavadora("MABE",10,"todo tipo de ropa",6999)
print("Contamos con lavadoras de la marca",R3.marca)
print("Con capacidad para",R3.capacidad,"kg")
print("Para ",R3.tipoderopa)
print("Con un costo de ",R3.costo)
