class Monster:
    
    def __init__(self, nombre, categoria):
        
        self.nombre = nombre
        self.categoria = categoria
        
    def myfunc(self):
        print("Hey, yo soy "+ self.nombre)
        
monstrito = Monster("Sullivan", "Asustador")
monstrito.myfunc()