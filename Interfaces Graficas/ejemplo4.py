import tkinter
#from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("800x600")

boton1 = tkinter.Button(ventana, text="Boton 1", height=10, width=10)
boton2 = tkinter.Button(ventana, text="Boton 2", height=10, width=10)
boton3 = tkinter.Button(ventana, text="Boton 3", height=10, width=10)

boton1.grid(row=0, column=0)
boton2.grid(row=1, column=1)
boton3.grid(row=3, column=3)


ventana.mainloop()