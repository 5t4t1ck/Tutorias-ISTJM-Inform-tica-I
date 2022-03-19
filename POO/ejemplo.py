"""Objeto Perro

Propiedades: Color, Edad, raza, tamaño, peso, vacunas
Métodos: Comer, Ladrar, Jugar, Correr"""

class Perro:
    
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
        
    def __str__(self):
        return f"Yo soy un perro llamado {self.nombre}, soy de {self.raza} y tengo {self.edad} años"
    
    
    def ladrar(self):
        return f"Yo soy {self.nombre} y puedo Ladrar, Guauuuuuu"
    
    def comer(self):
        return f"Yo tengo hambre y como comida"
    
Firulais = Perro("Firulais",7,"mestizo")
#print(Firulais.nombre)
#print(Firulais.edad)
#print(Firulais.raza)

print(Firulais)
print(Firulais.comer())
print("----------------------------")

Perlita = Perro("Perlita", 2, "Pitbull")
print(Perlita)
print(Perlita.ladrar())