"""
En este ejercicio, desarrollaré una mini aplicación de consola en Python que me permita gestionar datos de clientes mediante operaciones CRUD conectadas a mi base de datos MySQL; utilizaré la base de datos que creé en el examen de Bases de datos.El objetivo es practicar la interacción entre un programa Python y una base de datos real, aplicando instrucciones SQL básicas para crear, leer, actualizar y eliminar registros.Este ejercicio muestra cómo se combina la lógica de control (bucles y if-elif) con el uso de bibliotecas externas.La biblioteca mysql.connector se utiliza para establecer la conexión con MySQL, autenticándose con el usuario useroscar y la base de datos portafolioexamen.A continuación, se crea la tabla clients con su clave principal Identifier y los campos nombre, apellidos y correo electrónico.La aplicación muestra un mensaje de bienvenida y un menú de opciones numeradas del 1 al 5.Mediante un bucle while True, el usuario puede seleccionar la operación deseada y, dependiendo de la opción elegida, se ejecutan las sentencias SQL correspondientes:INSERT INTO para añadir un nuevo cliente.SELECT FROM para listar todos los registros.UPDATE SET WHERE para modificar los datos de un cliente específico.DELETE FROM para eliminar un registro por ID.Las decisiones se controlan con estructuras if-elif, y cada operación se confirma con connection.commit() para guardar los cambios en la base de datos.
"""

#import mysql.connector

#usando useroscar porque es el usuario que tiene todo los permisos.
# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="portafolioexamen"
)


cursor = connection.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS piezasportafolio_clientes (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
""")
connection.commit()

#########################################

print("=== CLIENT MANAGEMENT PROGRAM (MySQL) ===")
print("Welcome to the client management program connected to MySQL database.")

while True:
    print("""
1. Create new client
2. List all clients
3. Update client
4. Delete client
5. Exit
""")

    option = int(input("Choose an option: "))

    if option == 1:
        nombre = input("Name: ")
        apellidos = input("Surname: ")
        email = input("Email: ")
        cursor.execute("""
        INSERT INTO clientes (nombre, apellidos, email)
        VALUES (%s, %s, %s);
        """, (nombre, apellidos, email))
        connection.commit()
        print("Client added.")

    elif option == 2:
        cursor.execute("SELECT * FROM clientes;")
        for row in cursor.fetchall():
            print(row)

    elif option == 3:
        identificador = input("Client ID to update: ")
        nombre = input("New name: ")
        apellidos = input("New surname: ")
        email = input("New email: ")
        cursor.execute("""
        UPDATE clientes
        SET nombre = %s, apellidos = %s, email = %s
        WHERE Identificador = %s;
        """, (nombre, apellidos, email, identificador))
        connection.commit()
        print("Client updated.")

    elif option == 4:
        identificador = input("Client ID to delete: ")
        cursor.execute("DELETE FROM clientes WHERE Identificador = %s;", (identificador,))
        connection.commit()
        print("Client deleted.")

    elif option == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

connection.close()

"""
El ejercicio me ha ayudado a practicar el uso de Python como lenguaje para interactuar con una base de datos MySQL. Ya tenía algunos datos en ella, pero practiqué cómo crear una nueva tabla y utilizarla.
Se ha verificado cómo se pueden ejecutar operaciones CRUD desde una aplicación de consola, combinando sentencias SQL con estructuras de control y funciones de conexión.
El resultado final es un programa funcional y reutilizable que demuestra los fundamentos del desarrollo de software conectado a bases de datos reales.
Es fácil ver cómo se puede implementar esto en un escenario real, en el que necesitaría crear y utilizar una base de datos. Ha sido una tarea muy práctica y especialmente útil para comprender mejor cómo utilizar los diferentes lenguajes juntos.
"""