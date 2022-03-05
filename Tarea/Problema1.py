"""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
"""

def max():
    num1 = int(input('Por favor ingrese el primer valor '))
    num2 = int(input('Por favor ingrese el segundo valor '))

    if num1 > num2:
        print("El mayor es:", num1)
    else:
        print("El mayor es", num2)
        
max()