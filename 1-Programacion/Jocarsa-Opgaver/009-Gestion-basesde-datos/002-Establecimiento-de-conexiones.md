
IMPORTANTE! JoseVicente dijo que debía hacer esta tarea en Python, así que eso hice. Fue un error que se generara en Java.

En este ejercicio creo una pequeña aplicación en Python que me permite almacenar las comidas que preparo después de ir al gimnasio. Lo hago para practicar cómo trabajar con clases, objetos y atributos. Y practicar cómo guardar datos dentro de una base de datos.


Primero creo la clase Comida con los atributos id, nombre y calorías, junto con los getters y setters. Luego creo la clase ComidaDAO, que se conecta a la base de datos SQLite utilizando el método conectar(). A continuación, utilizo el método insertar(), que recibe un objeto Comida y guarda sus datos en la base de datos utilizando un comando SQL INSERT. Para probar el programa, creo un objeto Comida, establezco sus valores, me conecto a la base de datos e inserto el objeto.

# ------------ 1 Contexto ------------

Me encanta el fitness y la cocina. Después de cada sesión de gimnasio, quiero registrar qué comida he preparado ese día. Para ello, he creado una aplicación que me permite almacenar los detalles de las comidas en una base de datos.


# ------------ 2 & 3 Desarrolla una clase Comida y Implementa métodos en la clase Comida ------------
import sqlite3

class Comida():
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.calorias = 0

    def getId(self):
        return self.id
    
    def setId(self, nuevo_id):
        self.id = nuevo_id

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def getCalorias(self):
        return self.calorias
    
    def setCalorias(self, nuevas_calorias):
        self.calorias = nuevas_calorias



# ------------ 4 & 5 & 6 Crea una clase para manejar la conexión a la base de datos, Implementa el método conectar, Implementa el método  ------------

class ComidaDAO():
    
    def conectar(self):
        self.conexion = sqlite3.connect("comidas.db")
        cursor = self.conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comidas(
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                calorias INTEGER
            )
        """)
        self.conexion.commit()

    def insertar(self, comida):
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO comidas (id, nombre, calorias) VALUES (?, ?, ?)",
            (comida.getId(), comida.getNombre(), comida.getCalorias())
        )
        self.conexion.commit()

- Asegurando que todo funciona bien.
dao = ComidaDAO()
dao.conectar()

mi_comida = Comida()
mi_comida.setId(1)
mi_comida.setNombre("Pollo con arroz")
mi_comida.setCalorias(650)

dao.insertar(mi_comida)

print("Comida insertada correctamente")


Esta actividad me ayudó a practicar conceptos de programación orientada a objetos, como clases, objetos, atributos y métodos, así como la gestión de bases de datos. También practiqué cómo almacenar información real en una base de datos SQLite desde Python. No fue demasiado complicado, ya que lo he hecho muchas veces. En general, disfruté con la tarea y veo cómo me será útil en el futuro tener un mejor conocimiento de la programación orientada a objetos.