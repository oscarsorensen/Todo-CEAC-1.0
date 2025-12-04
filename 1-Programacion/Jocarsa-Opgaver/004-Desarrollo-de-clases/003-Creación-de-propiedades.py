"""
En la vida cotidiana, la programación puede ayudarnos a organizar información sobre nuestras actividades,
como cocinar o entrenar en el gimnasio. En este ejercicio aplico la programación orientada a objetos
para gestionar productos, lo que podría servir para registrar ingredientes, suplementos o materiales deportivos.
"""

# Definición de la clase Producto
class Producto:
    def __init__(self):
        self.nombre = ""
        self.precio = 0.0
        self.categoria = []  # lista (array) de categorías

# Instanciación del objeto
producto1 = Producto()

# Asignación de valores a las propiedades
producto1.nombre = "Proteina Whey"
producto1.precio = 15
producto1.categoria = ["Suplemento", "Gimnasio", "Nutricion"]

# Mostrar información del producto
print("Información del producto:")
print("Nombre:", producto1.nombre)
print("Precio:", producto1.precio, "€")
print("Categorías:", producto1.categoria)

"""
Este ejercicio demuestra cómo una clase puede representar objetos reales,
en este caso productos relacionados con la cocina o el gimnasio.
A través de la instanciación y asignación de propiedades,
aprendo a modelar información que podría utilizar en aplicaciones prácticas,
como un sistema personal de control de ingredientes o suplementos.
"""
