#Heidi Gomez
#Ejercicio de sudoku 
 
from numpy import *
 
def solucion_es_correcta(sudoku):
    
    for i in range(1,10):
        for fil in range(3):
            for col in range(3):
                mov = range(0,10,3)     
                subcuadrado = sudoku[mov[fil]:mov[fil+1], mov[col]:mov[col+1]]
 
                if i not in subcuadrado or i not in sudoku[:,i-1] or i not in sudoku[i-1,:]:
                    return False
    
    return True
