clients = "Pablo, Ricardo"

def create_client(client_name):
    global clients
    
    clients += client_name
    _add_comma()
    
    
def lista_clients():
    global clients
    
    print(clients)

def _add_comma():
    global clients

    clients += ", "


def _print_welcome():
    print("Bienvenido a este Crud de Ventas")
    print("*" * 50)
    print("Qué te gustaría hacer")
    print()

if __name__ == "__main__":
    lista_clients()
    clients += "David"
    lista_clients()
    
    

    
    
