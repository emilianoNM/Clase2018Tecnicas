#Eduardo Daniel Batta Gonzalez

from Tkinter import *

  root = Tk()
  root.title('tecnicas de programacio')
#nombre del alumno
   nombre_label = Label(root,text="Alumno :")
   nombre_label.grid(row=1,column=1)
   nombre_str = StringVar()
   nombre_entry = Entry(root,textvariable=nombre_str)
   nombre_entry.grid(row=1,column=2)
#semestre
   producto_label= Label(root,text="semestre : ")
   producto_label.grid(row=2,column=1)
   producto_str = StringVar()
   producto_entry = Entry(root,textvariable=semestre_str)
   producto_entry.grid(row=2,column=2)
#carrera
   cantidad_label = Label(root,text="carrera en curso : ")
   cantidad_label.grid(row=3,column=1)
   cantidad_str = StringVar()
   cantidad_entry = Entry(root,textvariable=carrera_str)
   cantidad_entry.grid(row=3,column=2)
#email
   mail_label = Label(root,text="Email : ")
    mail_label.grid(row=4,column=1)
    mail_str = StringVar()
    mail_entry = Entry(root,textvariable=mail_str)
    mail_entry.grid(row=4,column=2)
#final
   finish = Button(root,text="finalizar",relief=FLAT)
    finish.grid(row=5,column=2)
     root.mainloop()
