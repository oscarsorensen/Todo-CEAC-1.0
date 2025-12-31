

class Gimnasio:
    def __init__(self):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__miembros = []   # lista privada

    def anadirMiembro(self, nombre, apellidos):
        self.__miembros.append(nombre)



# ------------ 2 Herencia y polimorfismo ------------

class MiembroGimnasio(Persona):
  def __init__(self,nombre,apellidos,edad):
    super().__init__(nombre, apellidos)
    self.edad = edad

  def dameDatos(self):
    return "Miembro de gimnasio:"+self.nombre+" "+self.apellidos+"; Edad:"+str(self.edad) # Sobrescribo el otro dameDatos
