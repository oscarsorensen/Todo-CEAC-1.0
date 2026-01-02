

# ----------- 1-4 -----------
class Gimnasio:
    def __init__(self):
        self.__miembros = [] # Lista privada para almacenar los nombres de los miembros

    def anadirMiembro(self, nombre):
        self.__miembros.append(nombre) # Añadir un nuevo miembro a la lista

    def contarMiembros(self):
        return len(self.__miembros) # Devolver el número de miembros actuales

    def mostrarMiembros(self):
        for m in self.__miembros: # Mostrar todos los nombres de los miembros
            print(m)


# ----------- 5 (methodo main) -----------
if __name__ == "__main__":
    gym = Gimnasio()

    gym.anadirMiembro("Oscar")
    gym.anadirMiembro("Sofia")
    gym.anadirMiembro("Carlos")

    print("Miembros actuales:", gym.contarMiembros())
    gym.mostrarMiembros()

# Output:

Miembros actuales: 3
Oscar
Sofia
Carlos