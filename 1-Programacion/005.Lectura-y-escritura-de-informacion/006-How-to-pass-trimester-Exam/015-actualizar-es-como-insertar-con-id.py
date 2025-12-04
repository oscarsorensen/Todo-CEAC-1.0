
class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print("**************** Gestion de clientes v0.1 ******************")
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
        clientes.append(Cliente(nombre, apellidos, email))

    elif opcion == 2:
        for i, cliente in enumerate(clientes):
            print(i, cliente.nombre, cliente.apellidos, cliente.email)

    elif opcion == 3:
        identificador = int(input("Introduce el ID del cliente a actualizar: "))
        nombre = input("Introduce el nuevo nombre del cliente: ")
        apellidos = input("Introduce los nuevos apellidos del cliente: ")
        email = input("Introduce el nuevo email del cliente: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        pass
