""""
En este ejercicio he creado una miniaplicación CRUD en Python utilizando la librería pickle para guardar y recuperar datos de forma persistente.
Aplico los conceptos de clases y propiedades, evitando el uso de métodos, y empleo un bucle while True junto con estructuras condicionales if/elif para construir un menú interactivo en la terminal.
Todo esto me permite crear, leer, actualizar y eliminar datos de clientes dentro de una clase, relacionando la programación con una situación real, donde la información personal puede cambiar y debe actualizarse de manera controlada.

Comencé definiendo una clase llamada Cliente, que representa a una persona y contiene tres propiedades vacías: nombre, email y dirección.
A continuación, añadí varias líneas print() para mostrar el menú principal y guiar al usuario sobre cómo funciona el programa.
Después utilicé un bloque try/except para intentar abrir un archivo llamado clientes.bin, donde se almacenarán los datos. Si el archivo no existe, se crea una lista vacía.
Esto garantiza que el programa pueda iniciarse sin errores y recuperar los clientes guardados previamente.
El núcleo del programa es un bucle while True que muestra las opciones del menú y captura la elección del usuario.
Según la opción seleccionada, se ejecutan las operaciones Crear, Listar, Actualizar o Eliminar clientes.
Para crear un nuevo cliente, empleo nuevocliente = Cliente() y luego clientes.append(nuevocliente) para añadirlo a la lista.
Finalmente, después de cada operación, uso pickle.dump() para guardar la lista actualizada en el archivo binario y cierro el archivo correctamente con archivo.close().
"""

import pickle

# Defino la clase Cliente 
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.email = ""
        self.direccion = ""

print("Programa de gestion de clientes c0.1 Oscar Sorensen")
print("1. Insertar un cliente")
print("2. Listar clientes")
print("3. Actualizar clientes")
print("4. Eliminar clientes")
print("5. Salir")

# --------- Añadido: cargar datos existentes si hay archivo ----------
try:
    archivo = open("clientes.bin", "rb")
    clientes = pickle.load(archivo)
    archivo.close()
    print("Clientes cargados correctamente.")
except:
    print("No existe archivo de datos, se creará uno nuevo.")
    clientes = []
    #la archivo aperece cuando se inserta el primer cliente en "La Raiz del proyecto"
# -------------------------------------------------------------------

while True: # Menu de opciones
    opcion = input("Escoge una opcion: ")
    opcion = int(opcion)

    if opcion == 1: #La archivo aperece cuando se inserta el primer cliente
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        print("Cliente insertado correctamente.")
        clientes.append(nuevocliente)

    elif opcion == 2: # Listar clientes
        print("Vamos a ver los clientes")
        for c in clientes:
            print("Nombre:", c.nombre, "Email:", c.email, "Direccion:", c.direccion)

    elif opcion == 3: # Actualizar cliente
        print("Vamos a actualizar un cliente")
        nombre_buscar = input("Introduce el nombre del cliente a actualizar: ")
        for c in clientes:
            if c.nombre == nombre_buscar:
                print("Cliente encontrado.")
                c.email = input("Nuevo email: ")
                c.direccion = input("Nueva dirección: ")
                print("Cliente actualizado correctamente.")
                break
        else:
            print("No se encontró un cliente con ese nombre.")

    elif opcion == 4: # Eliminar cliente
        print("Vamos a eliminar un cliente")
        nombre_eliminar = input("Nombre del cliente a eliminar: ")
        for c in clientes:
            if c.nombre == nombre_eliminar:
                clientes.remove(c)
                print("Cliente eliminado.")
                break

    elif opcion == 5: # Salir
        print("Saliendo del programa...")
        break

    # --------- Añadido: guardar los cambios después de cada acción ----------
    archivo = open("clientes.bin", "wb")
    pickle.dump(clientes, archivo)
    archivo.close()
    # -----------------------------------------------------------------------


""""
Con esta actividad he practicado el uso de la librería pickle, junto con estructuras de control como while True y if/elif, para implementar un programa CRUD completo.
El ejercicio refuerza los principios básicos de la programación orientada a objetos, como la organización, la reutilización del código y la claridad en el diseño.
Además, demuestra cómo Python puede manejar datos de manera persistente, combinando clases y almacenamiento binario de forma sencilla y estructurada.
"""