"""
Pedir por teclado al usuario su edad, 
si esta es menor a 18 años, imprimir por pantalla "Es menor de Edad"
si esta es igual a 18 años, imprimir por pantalla "Es mayor de Edad"
si esta es mayor a 50 años, imprimir por pantalla "Es de la 3era Edad"    
"""
edad = int(input('¿Qué edad tienes? '))
#print(type(edad))

if edad < 18:
    print("Es menor de Edad")
elif edad > 18 and edad <= 50:
    print("Es mayor de Edad")
else:
    print("Es de la tercera Edad")