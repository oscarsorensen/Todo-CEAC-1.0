"""En esta actividad pongo en práctica los conceptos básicos del manejo de ficheros en Python. He aprendido a abrir, escribir, añadir y leer información utilizando diferentes modos de acceso. El ejercicio se basa en Antonio, un aficionado al fitness que quiere registrar sus comidas y entrenamientos en una aplicación personal. A través de este contexto, la actividad muestra cómo se puede guardar y consultar información más adelante, una habilidad fundamental en proyectos reales que necesitan almacenar datos de forma permanente."""

"""Python ofrece la función open() para trabajar con ficheros. Esta función recibe el nombre del fichero y el modo de acceso, que define cómo se va a utilizar. Los modos más comunes son "w" para escribir y crear un nuevo archivo o reemplazar uno existente, "a" para añadir información al final del fichero y "r" para leer su contenido. Una vez abierto el fichero, el programa puede escribir o leer datos, y siempre debe cerrarse con close() para liberar recursos y asegurar que la información se guarde correctamente.

El ejercicio también introduce la librería pickle, que permite guardar y cargar objetos completos de Python en formato binario. Esto hace posible almacenar datos estructurados, como los entrenamientos de Antonio, para poder recuperarlos y mostrarlos más adelante."""

import pickle

# Crear fichero, escribir y leer datos
f = open("comidas.txt", "w") # Modo escritura (write) (w)
f.write("Alimento cocinado: Pizza\n") #\n para salto de línea
f.close() # Cerrar fichero después de escribir. Esto es importante

# Anado una línea más, Hamburguesa
f = open("comidas.txt", "a") # Modo añadir (append) (a)
f.write("Alimento cocinado: Hamburguesa\n")
f.close() 

# Leer el fichero y mostrar la última línea
f = open("comidas.txt", "r") # Modo lectura (read) (r)
for linea in f: 
    ultima = linea
f.close()
print("Último alimento cocinado:", ultima) # Mostrar última línea, con loop


#### segunda parte (4): uso de pickle para guardar objetos ####

# Guardar y recuperar objeto con pickle
class Entrenamiento:
    def __init__(self):
        self.ejercicio = "weightlifting"
        self.duracion = 90   # minutos

# Guardar objeto en fichero binario
archivo = open("entrenamiento.bin", "wb")
pickle.dump(Entrenamiento(), archivo)
archivo.close()

# Recuperar y mostrar objeto
archivo = open("entrenamiento.bin", "rb")
obj = pickle.load(archivo) # Recuperar objeto
archivo.close()

print("Entrenamiento recuperado:")
print("Ejercicio:", obj.ejercicio)
print("Duración:", obj.duracion, "minutos")


"""Este ejercicio me ha ayudado a comprender cómo utilizar los modos de escritura, añadido y lectura en Python para gestionar ficheros de texto, y cómo emplear la librería pickle para guardar objetos en ficheros binarios. Estas técnicas son esenciales para mantener la información disponible entre sesiones y constituyen la base del desarrollo de aplicaciones más avanzadas que gestionan datos de usuario, como el registro de comidas y entrenamientos de Antonio."""