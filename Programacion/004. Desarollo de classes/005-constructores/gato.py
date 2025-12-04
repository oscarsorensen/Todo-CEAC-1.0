
class Gato():
    def __init__(self,edad,nombre,raza): #el constructor se ejecuta si o si
        self.edad = 0
        self.nombre = nombre
    
    def maulla(self):   #el resto de metodos solo se ejecutan si los llamas
        return "el gato esta maullando"
    
    
gato1 = Gato(5,"micifu","siames")
    


