
"""
Las clases en programación permiten organizar información y comportamientos dentro de una misma estructura. En este tema aprendo a representar objetos del mundo real —como clientes o cuentas bancarias— y a gestionarlos mediante propiedades y métodos, igual que en una aplicación real de gestión personal o profesional.

Defino varias clases (Client, BankAccount) con el método __init__() y atributos bien estructurados.
Implemento métodos que modifican y muestran la información (show_info, deposit, withdraw, get_balance, set_balance), aplicando el principio de encapsulación y un menú CRUD básico para practicar la manipulación de objetos.
"""

# Defino la clase Cliente (necesario antes de usar Cliente())
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""


print("Programa de gestion de clientes c0.1 Oscar Sorensen")
print("1. Insertar un cliente")
print("2. Listar clientes")
print("3. Actualizar cliente")
print("4. Eliminar cliente")
print("5. Salir")

clientes = []  # creo una lista VACÍA

while True:  # Esto desata un bucle infinito pero controlado

    opcion = input("Escoge una opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
        print("Cliente insertado correctamente")

    elif opcion == 2:
        print("Vamos a ver los clientes")
        for cliente in clientes:
            print(cliente.nombre, cliente.email, cliente.direccion)

    elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a actualizar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                cliente.email = input("Nuevo email: ")
                cliente.direccion = input("Nueva direccion: ")
                print("Cliente actualizado correctamente")

    elif opcion == 4:
        print("Vamos a eliminar un cliente")
        nombreabuscar = input("Introduce el nombre del cliente a eliminar: ")
        for cliente in clientes:
            if cliente.nombre == nombreabuscar:
                clientes.remove(cliente)
                print("Cliente eliminado correctamente")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta otra vez")


"""
Este ejercicio demuestra cómo las clases permiten unir datos y acciones en un solo bloque lógico.
Gracias a ello puedo crear aplicaciones más organizadas y reutilizables, comprendiendo cómo la programación orientada a objetos se aplica a casos reales como la gestión de clientes o cuentas.
Del mismo modo, podría aplicar estos conceptos para desarrollar una aplicación que gestione mis rutinas de gimnasio o mis recetas de cocina, almacenando información y operaciones de forma estructurada y eficiente.
"""