"""5- Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista."""

"""
Paso 1: Definir una función sum
Paso 2: Definir una función multip
Paso3: La función sum debe sumar los números de una lista
Paso 4: La función multip debe sumar los numeros de una lista
"""
lista = [2,5,6,8,2]
suma = 0
multiplica = 1
def sum():
    print("Ahora la suma")
    for x in lista:
        global suma
        suma = suma + x
        print(suma)

sum()

def multip():
    print("Ahora la multiplicación")
    for x in lista:
        global multiplica
        multiplica = multiplica * x
        print(multiplica)
    
multip()