chain=input("\n\nEscribe una palabra o secuencia de letras\n>")

if chain==chain[::-1]:
  print('\n%s es un palindromo' %(chain))
else:
    print('\n%s no es un palindromo' %(chain))
pass    
  
print('\n\n')