#Carracedo Sotelo Eduardo
lado = int(input("introduce un numero: "))
interior = lado - 2
print ('*' * lado)
for i in range(interior):
    print ('*' + ' ' * interior + '*')
print ('*' * lado)
