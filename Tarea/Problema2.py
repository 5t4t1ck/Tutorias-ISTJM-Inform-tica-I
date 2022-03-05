"""
2- Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos.
"""

def max_de_tres():
    num1 = int(input('Por favor ingrese el primer valor '))
    num2 = int(input('Por favor ingrese el segundo valor '))
    num3 = int(input('Por favor ingrese el tercer valor '))

    if num1 > num2 and num1 > num3:
        print("El mayor es:", num1)
    elif num2 > num3:
        print("El mayor es", num2)
    else:
        print("El mayor es", num3)
        
max_de_tres()