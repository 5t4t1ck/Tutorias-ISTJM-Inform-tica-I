import tkinter
#from tkinter import *

ventana = tkinter.Tk()

"""def saludo():
    print("Hola a todos")"""

def saludo(nombre):
    print("Hola "+nombre)

#boton1 = tkinter.Button(ventana, text="Presionar", padx=50, pady=50)
boton1 = tkinter.Button(ventana, text="Presionar", padx=50, pady=50, command=lambda: saludo("Diego"))
boton1.pack()

ventana.mainloop()