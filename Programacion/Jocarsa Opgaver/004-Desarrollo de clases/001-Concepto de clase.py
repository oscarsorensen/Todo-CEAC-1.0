"""
En la vida diaria, las clases en programación permiten representar objetos del mundo real. En este caso, la clase Gato refleja cómo puedo organizar información, igual que cuando gestiono mis actividades o pasatiempos como cocinar o entrenar.

Defino la clase Gato con el método __init__() y los atributos nombre y color.
Luego creo dos objetos, Garfield y Gustavo, asignándoles sus respectivos colores y mostrando su estado antes y después de la modificación.
"""

class Gato():
    def __init__(self):
        self.color = ""
        self.nombre = ""

# Crear los gatos (instancias)
gato1 = Gato()
gato2 = Gato()

# Imprimir estado inicial
print("Estado inicial:")
print("Gato 1:", gato1.nombre, gato1.color)
print("Gato 2:", gato2.nombre, gato2.color)

# Modificar atributos
gato1.nombre = "Garfield"
gato1.color = "naranja"
gato2.nombre = "Gustavo"
gato2.color = "blanco"

# Imprimir estado modificado
print("Estado modificado:")
print("Gato 1:", gato1.nombre, gato1.color)
print("Gato 2:", gato2.nombre, gato2.color)

"""
Este ejercicio demuestra cómo los objetos pueden almacenar y cambiar información, igual que en una aplicación real que gestiona mis rutinas o preferencias. Aprender a crear clases me ayuda a estructurar datos de forma lógica y reutilizable.
"""