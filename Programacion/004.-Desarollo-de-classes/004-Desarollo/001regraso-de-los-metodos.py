

class Gato():
    def __init__(self):
        self.color = ""      #esto es  una propiedad
        
    def maulla(self):         #esto es un metodo (es una accion)
        return "miau"

    def setColor(self, nuevocolor):     #define un setter - el metodo es el responsable de cambiar la propiedad
        #por ejemplo aqui podria validar si el color es un color valido para un gato
        self.color = nuevocolor         #Y camvio la propiedad color

    def getColor(self):
        #una vez mas, aqui podria poner validaciones si lo quisiera
        return self.color

    
gato1 = Gato()
gato1.color = "naranja"         #aqui seteamos una propiedad directamente (no es buena practica)
print(gato1.maulla())             #aqui llamamos a un metodo

gato1.setColor("naranja")       #Esto es una practica mucho mejor

print(gato1.color)              #acceco directo, se puede pero no es buena practica

print(gato1.getColor())        #esto es mejor, se recomienda