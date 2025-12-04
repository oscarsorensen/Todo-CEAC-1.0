
# En este ejercicio, practico las operaciones CRUD 
# (Crear, Leer, Actualizar y Eliminar) utilizando SQLite en Python.
# El objetivo es comprender cómo un programa Python puede gestionar
# un archivo de base de datos local (.db) para almacenar y modificar datos de clientes.
#
# En primer lugar, el script se conecta a una base de datos llamada «company.db»
# y crea una tabla llamada «clients» si no existe.
# A continuación, se definen funciones individuales para:
#   - Añadir un nuevo cliente (crear_cliente)
#   - Listar todos los clientes (listar_clientes)
#   - Actualizar la información de un cliente (actualizar_cliente)
#   - Eliminar un cliente (eliminar_cliente)
#   - Buscar clientes por nombre, apellido o correo electrónico
#
# La sección práctica prueba cada operación para verificar 
# que todos los cambios se aplican correctamente a la base de datos.

import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# CREATE TABLE. Since it may already exist, we use IF NOT EXISTS.
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT
);
""")
connection.commit() 

# CREATE
def crear_cliente(name, surname, email):
    cursor.execute("INSERT INTO clients (name, surname, email) VALUES (?, ?, ?)", (name, surname, email))
    connection.commit()
    print("Client added successfully.")

# READ
def listar_clientes():
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# UPDATE
def actualizar_cliente(id, new_name, new_surname, new_email):
    cursor.execute("UPDATE clients SET name=?, surname=?, email=? WHERE id=?", (new_name, new_surname, new_email, id))
    connection.commit()
    print("Client updated successfully.")

# DELETE
def eliminar_cliente(id):
    cursor.execute("DELETE FROM clients WHERE id=?", (id,))
    connection.commit()
    print("Client deleted successfully.")


# SEARCH
def buscar_cliente_por_email(email):
    cursor.execute("SELECT * FROM clients WHERE email=?", (email,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def buscar_cliente_por_nombre(name):
    cursor.execute("SELECT * FROM clients WHERE name=?", (name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def buscar_cliente_por_apellido(surname):
    cursor.execute("SELECT * FROM clients WHERE surname=?", (surname,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Test section
crear_cliente("Oscar", "Sorensen", "oscar@email.com")
listar_clientes()

crear_cliente("Oscarååå", "Sørensenæ", "oscar@email.com")
listar_clientes()

crear_cliente("Oscaråå###å", "Søren%55//senæ", "oscar@e()mail.com")
listar_clientes()

eliminar_cliente(2) # Delete client with ID 2. This works. Using SQL viewer to check db.

# Search example
buscar_cliente_por_nombre("Oscar")

connection.close()
print("Connection closed successfully.")


# A través de este ejercicio, aprendí a utilizar Python y SQLite
# conjuntamente para realizar una gestión completa de bases de datos a nivel local.
# Cada función CRUD interactúa con el archivo de la base de datos utilizando
# comandos SQL ejecutados a través de la biblioteca sqlite3.
#
# Los resultados confirman que es posible:
#   - Crear y estructurar una tabla de forma dinámica.
#   - Insertar, actualizar, leer y eliminar información.
#   - Realizar búsquedas con diferentes criterios.
#
# Esta actividad demuestra cómo se pueden integrar las bases de datos
# en aplicaciones Python y sienta las bases para 
# sistemas más avanzados que gestionan información real de clientes.