"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False
"""
"""
Si ingreso una vocal (a, e, i, o, u) el programa me debe arrojar un mensaje que diga True
Si ingreso una consonante el programa me debe arrojar un mensaje que diga False
"""

"""
Paso 1: Ingreso un valor a traves de teclado
Paso 2: Comparo si este valor es una vocal
Paso 3: Si es un vocal presento True
Paso 4: Si no es una vocal presento False
"""

def caracter():
    letra = print(input("Por favor ingrese un caracter por teclado: "))

    if letra == "a":
        print("El valor es True")
    elif letra == "e":
        print("El valor es True")
    elif letra == "i":
        print("El valor es True")
    elif letra == "o":
        print("El valor es True")
    elif letra == "u":
        print("El valor es True")
    else:
        print("El valor es False")

caracter()

    
    

