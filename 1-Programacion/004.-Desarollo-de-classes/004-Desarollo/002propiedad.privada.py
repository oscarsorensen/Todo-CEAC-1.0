


class Gato():
    def __init__(self):
        self.__color = ""      #esto es  una propiedad privada (contrapuesta a publica)
        
gato1 = Gato()
print(gato1.__color)   #esto da error, la propiedad es privada
        
