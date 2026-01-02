#En este ejercicio, creo una clase llamada Gym. Utilizo esta clase porque me gusta ir al gimnasio y, por lo tanto, es un escenario más cercano a la realidad. La idea es gestionar a las personas que entrenan allí y mantener un control sencillo de los miembros.
#Primero creé la clase Gym con una lista para almacenar a los miembros. Luego creé tres métodos: uno para añadir miembros, otro para contarlos y otro para mostrarlos. En la parte 5, creé un objeto Gym, añadí varios miembros y comprobé que todo funcionaba correctamente.

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

#Miembros actuales: 3
#Oscar
#Sofia
#Carlos

#Este ejercicio muestra cómo una clase de Python puede organizar la información de una manera clara y útil. En un escenario real, podría utilizarse para la gestión de un gimnasio real, y se conecta directamente con lo que hemos aprendido porque practica clases, atributos privados, métodos y la ejecución práctica de programas.