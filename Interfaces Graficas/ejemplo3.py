import tkinter
#from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("800x600")

#Caja de Texto
#cajaDeTexto = tkinter.Entry(ventana)
#cajaDeTexto = tkinter.Entry(ventana, font="Arial 50")
cajaDeTexto = tkinter.Entry(ventana)

etiqueta = tkinter.Label(ventana)

cajaDeTexto.pack()
etiqueta.pack()

def textoCajadeTexto():
    textoA = cajaDeTexto.get()
    print(textoA)
    etiqueta["text"]=textoA

boton = tkinter.Button(ventana, text="click", command=textoCajadeTexto)
boton.pack()

textoCajadeTexto()

ventana.mainloop()