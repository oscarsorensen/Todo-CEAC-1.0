
#las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = None
        self.edad = 0
        self.telefonos = []

#Ahora instancio un nueco objeto
cliente1 = Cliente()

#Ahora le escribo una propiedad

cliente1.nombre = "Oscar Sorensen"

print("El nombre del cliente es: ", cliente1.nombre)

cliente1.telefonos.append("587349373")
cliente1.telefonos.append("187349374")

print(cliente1.telefonos)

