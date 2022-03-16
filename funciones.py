def suma():
    a = int(input("Por favor ingrese un valor numerico: "))
    b = int(input("Por favor ingrese un segundo valor numerico: "))
    return a+b

#print(suma())

def resta():
    a = int(input("Por favor ingrese un valor numerico: "))
    b = int(input("Por favor ingrese un segundo valor numerico: "))
    return a-b

#print(resta())

def multiplicacion():
    a = int(input("Por favor ingrese un valor numerico: "))
    b = int(input("Por favor ingrese un segundo valor numerico: "))
    return a*b

#print(multiplicacion())

"""def div():
    try:
        a = int(input("Por favor ingrese un valor numerico: "))
        b = int(input("Por favor ingrese un segundo valor numerico: "))
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir para 0")
    except ValueError:
        print("Usted no ingreso un valor numerico")
    finally:
        print("Gracias por utilizar esta aplicación")

print(div())"""

def potenciacion(num1, num2):
    return (num1**num2)

print(potenciacion(2,3))
print(potenciacion(5,3))
print(potenciacion(10,3))
print(potenciacion(1000,3))
print(potenciacion(4,3))
print(potenciacion(7,3))