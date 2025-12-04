
    class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

clientes = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))
    
    
    
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        email = input("Introduce el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        for cliente in clientes:
            print(cliente.nombre, cliente.apellidos, cliente.email)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass