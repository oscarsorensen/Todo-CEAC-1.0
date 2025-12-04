

"""
En este ejercicio aplico el concepto de herencia en Python para representar diferentes tipos
de animales dentro de un sistema estructurado. La herencia permite crear clases que comparten
características comunes, reduciendo la repetición de código y facilitando la organización.
Defino una clase base "Animal" con los atributos edad, nombre y raza. Las subclases "Gato"
y "Perro" heredan estos atributos y añaden métodos específicos para mostrar el nombre de cada
animal. Cada constructor utiliza "super().__init__()" para invocar el constructor de la clase
superior y asegurar que los atributos se inicialicen correctamente.
Este enfoque puede aplicarse en cualquier programa que necesite modelar entidades relacionadas
de forma jerárquica y reutilizable.
"""

class Animal:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato(Animal):
    def __init__(self):
        super().__init__()
    def mostrarNombre(self):
        print("El gato se llama", self.nombre)

class Perro(Animal):
    def __init__(self):
        super().__init__()
    def mostrarNombre(self):
        print("El perro se llama", self.nombre)

# Ejemplo de uso
gato1 = Gato()
gato1.nombre = "Garfield"
gato1.mostrarNombre()

perro1 = Perro()
perro1.nombre = "Havana"
perro1.mostrarNombre()


"""
Con este ejercicio he aprendido a utilizar la herencia para crear clases más organizadas y reutilizables. Este concepto puede aplicarse en proyectos más grandes, como aplicaciones que gestionen rutinas de entrenamiento o recetas de cocina.
"""