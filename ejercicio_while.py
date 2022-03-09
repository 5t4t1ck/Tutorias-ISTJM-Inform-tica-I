"""Ejercicio 1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

contador = 0
palabra = input("Por favor ingrese una palabra: ")
#print(palabra)
while contador < 10:
    print(contador, palabra)
    contador += 1
    #print(contador)