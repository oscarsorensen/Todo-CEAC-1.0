
"""
Introducción y contextualización
En este ejercicio aplico los conceptos de clases, constructores y métodos getter y setter
para crear un sistema sencillo de gestión de clientes en una tienda virtual de ropa.
Como me gusta ir al gimnasio, he incluido un método adicional que determina si un cliente
es frecuente, igual que un entrenador evalúa la constancia de sus alumnos.


La clase Cliente utiliza atributos privados (__nombrecompleto, __email y __compras)
para mantener la información encapsulada y evitar accesos directos desde fuera.
Los métodos setter permiten asignar valores a esos atributos, mientras que los getter
devuelven su contenido. Además, se define un método adicional llamado esFrecuente()
que devuelve True si el cliente ha realizado más de 5 compras, y False en caso contrario.
"""


class Cliente:
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""
        self.__compras = 0

    # Setters
    def setNombreCompleto(self, nuevo_nombre):
        self.__nombrecompleto = nuevo_nombre

    def setEmail(self, nuevo_email):
        self.__email = nuevo_email

    def setCompras(self, numero_compras):
        self.__compras = numero_compras

    # Getters
    def getNombreCompleto(self):
        return self.__nombrecompleto

    def getEmail(self):
        return self.__email

    # Método adicional
    def esFrecuente(self):
        return self.__compras > 5


# Ejemplo de uso
cliente1 = Cliente()
cliente1.setNombreCompleto("Oscar Sørensen")
cliente1.setEmail("oscar@example.com")
cliente1.setCompras(7)

print("Nombre completo:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())

if cliente1.esFrecuente():
    print("El cliente es frecuente en la tienda.")
else:
    print("El cliente no es frecuente aún.")

"""
En este ejercicio he aprendido a utilizar clases con encapsulación, métodos getter y setter,
y a implementar un método adicional para evaluar el comportamiento de un cliente.
Este tipo de estructura puede aplicarse fácilmente en sistemas reales de gestión de tiendas,
donde se necesita controlar la información privada y analizar la fidelidad de los clientes.
"""