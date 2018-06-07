import tkinter

#Agregar un boton
from tkinter import messagebox

top=tkinter.Tk()
def helloCallBack():
    messagebox.showinfo("Hello Python0","Hello Word")

#Creando un boton en la ventana (Constructor)
B=tkinter.Button(top,text="Hello",command=helloCallBack)

#Se pintara en la ventana
B.pack()

#Coordenadas
B.place(x=35, y=50)

top.mainloop()

