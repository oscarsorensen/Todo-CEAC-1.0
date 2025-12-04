"""En este ejercicio, utilizo constructores en Python para crear una clase que muestra una situación real: el registro de clientes de un gimnasio.
Este contexto conecta directamente con uno de mis propios pasatiempos, ir al gimnasio, y me permite comprender cómo la programación orientada a objetos puede ayudar a gestionar información del mundo real.
Al crear una clase Cliente, los datos de cada cliente (nombre, apellidos, correo electrónico y dirección) se pueden organizar y reutilizar de manera eficiente dentro de un programa.
"""

"""La clase Cliente incluye un método constructor __init__, que se ejecuta automáticamente cuando se crea un nuevo objeto.
Este constructor inicializa los cuatro atributos: nombre, apellido, correo electrónico y dirección.
El método show_info imprime la información completa del cliente en la pantalla.

Para probar la clase, el programa solicita al usuario que introduzca los cuatro datos.
A continuación, se crea un nuevo objeto Cliente con estos valores y se almacena en una lista llamada clientes.
Por último, la función list_clientes() recorre la lista e imprime los datos de cada cliente, confirmando que el constructor ha inicializado correctamente el objeto.
"""

"""
Programa: ClienteGimnasio
Versión: 0.1
Autor: Oscar Sorensen
Descripción: Creación de una clase Cliente con un constructor para inicializar los atributos del cliente.
"""

class Cliente:
    def __init__(self, nombre, apellido, email, direccion):   # (constructor)
        self.nombre = nombre               # property (propiedad)
        self.apellido = apellido            # property (propiedad)
        self.email = email                  # property (propiedad)
        self.direccion = direccion          # property (propiedad)

    def show_info(self):                    # method (método)
        print(f"Cliente: {self.nombre}, Apellido: {self.apellido}, "
              f"Email: {self.email}, Dirección: {self.direccion}")


clients = []  # lista global para guardar objetos

def insert_client():
    nombre = input("Name: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    direccion = input("Direccion: ")
    clients.append(Cliente(nombre, apellido, email, direccion))
    print("Inserted.")

def list_clients():
    if len(clients) == 0:
        print("No clients yet.")
        return
    i = 1
    for c in clients:
        print(f"Cliente(nombre='{c.nombre}', apellidos='{c.apellido}', email='{c.email}', direccion='{c.direccion}')")  
        i = i + 1

insert_client()
list_clients()


"""Esta tarea muestra cómo los constructores facilitan la creación e inicialización automática de objetos, garantizando que cada instancia cuente con los atributos necesarios desde el principio.
Mediante el uso de esta estructura, es posible gestionar los datos de los clientes de forma clara y eficiente, un principio que se aplica no solo a este ejemplo, sino a cualquier sistema futuro que almacene y organice información utilizando clases.
"""