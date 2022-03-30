""" 
Mostrar con la libreria tkinter un boton, una etiqueta y una caja de texto

El boton va a decir nombre

La caja de texto recibe un nombre

y la etiqueta almacena el valor del nombre que se asigne en la caja de texto
"""
import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")

etiqueta = tkinter.Label(ventana)
cajaDeTexto = tkinter.Entry(ventana)

def mostrar():
    text = cajaDeTexto.get()
    print(text)
    etiqueta["text"]=text

boton = tkinter.Button(ventana, text="nombre", command= lambda:mostrar())

"""etiqueta.pack()
cajaDeTexto.pack()
boton.pack()"""

cajaDeTexto.grid(row=5, column=3)
etiqueta.grid(row=3,column=3)
boton.grid(row=4, column=3)

ventana.mainloop()