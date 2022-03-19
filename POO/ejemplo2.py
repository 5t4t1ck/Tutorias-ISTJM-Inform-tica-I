""" 
Crear una clase carro que lleve como atributos:
- Marca
- Cilindraje
- Año

Y que tenga algunos métodos:
- Acelerar
- Frenar
- Girar a la Derecha
- Girar a la Izquierda
- Retro 
"""

class Carro:
    
    def __init__(self, marca, cilindraje, año):
        self.marca = marca
        self.cilindraje = cilindraje
        self.año = año

    def __str__(self):
        return f"Este es un objeto de la clase Carro, soy la marca {self.marca}, tengo de cilindraje {self.cilindraje}, y soy del año {self.año}"

    def acelerar(self):
        return f"Soy un {self.marca} y estoy acelerando..."

    def frenar(self):
        return f"Soy un {self.marca} y estoy frenando..."


Toyota = Carro("Toyota", 2000, "2011")
print(Toyota)
print(Toyota.acelerar())
print(Toyota.frenar())

print("--------------------------------------------------")
print("\n")

Suzuki = Carro("Suzuki", 1400, "2001")
print(Suzuki)
print(Suzuki.acelerar())
print(Suzuki.frenar())

print("--------------------------------------------------")
print("\n")

Datzun = Carro("Datzun", 1200, "2000")
print(Datzun)
print(Datzun.acelerar())
print(Datzun.frenar())