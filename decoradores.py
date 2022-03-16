def funcion_decoradores(funcion_parametro):
    def funcion_interna():
        print("Se van a presentar unos calculos mantemáticos")
        
        funcion_parametro()

        print("Aquí va más código")
    return funcion_interna

@funcion_decoradores
def suma():
    print(4+6)
    
print(".....................")
@funcion_decoradores
def resta():
    print(8-2)
    
suma()
resta()