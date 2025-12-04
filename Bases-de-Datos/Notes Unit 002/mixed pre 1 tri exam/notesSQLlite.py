# ===========================================================
# UNIT – SQLITE + PYTHON (CEAC)
# Complete study file | Oscar Sørensen
# ===========================================================
# SQLite is a small database engine that comes with Python.
# It stores all data inside a single .db file and uses SQL syntax.
# No server, no password, no installation required.
# ===========================================================

# ===========================================================
# 0. CONNECTING TO A DATABASE
# ===========================================================
# Import the sqlite3 library (built into Python)
import sqlite3

# Connect to a database (creates the file if it doesn’t exist)
connection = sqlite3.connect("company.db")

# Create a cursor (used to execute SQL commands)
cursor = connection.cursor()

# ===========================================================
# 1. CREATE A TABLE
# ===========================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT
);
""")
connection.commit()  # Save changes to the file

# ===========================================================
# 2. INSERT DATA (CREATE)
# ===========================================================
# We use SQL syntax but executed through Python.
cursor.execute("""
INSERT INTO clients VALUES (NULL, 'Jorge', 'Garcia Lopez', 'jorge@jocarsa.com');
""")
connection.commit()

# You can also insert dynamic data using variables:
name = input("Enter client name: ")
surname = input("Enter client surname: ")
email = input("Enter client email: ")

cursor.execute("""
INSERT INTO clients VALUES (NULL, ?, ?, ?)
""", (name, surname, email))  # safer than string concatenation
connection.commit()

# ===========================================================
# 3. READ DATA (READ)
# ===========================================================
cursor.execute("SELECT * FROM clients;")
rows = cursor.fetchall()  # Returns all records
for row in rows:
    print(row)

# Each "row" is a tuple, for example: (1, 'Oscar', 'Sorensen', 'oscar@example.com')

# ===========================================================
# 4. UPDATE DATA (UPDATE)
# ===========================================================
client_id = input("Enter client ID to update: ")
new_name = input("New name: ")
new_surname = input("New surname: ")
new_email = input("New email: ")

cursor.execute("""
UPDATE clients
SET name = ?, surname = ?, email = ?
WHERE id = ?;
""", (new_name, new_surname, new_email, client_id))
connection.commit()
print("Client updated successfully.")

# ===========================================================
# 5. DELETE DATA (DELETE)
# ===========================================================
client_id = input("Enter client ID to delete: ")
cursor.execute("DELETE FROM clients WHERE id = ?;", (client_id,))
connection.commit()
print("Client deleted successfully.")






# ===========================================================
# 6. FULL MENU EXAMPLE (CRUD PROGRAM) SQLITE
# ===========================================================
# The following menu puts all operations together.

import sqlite3
connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellidos TEXT,
    email TEXT
);
""")
connection.commit()

#########################################

print("=== CLIENT MANAGEMENT PROGRAM (SQLite) ===")

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
        INSERT INTO clientes VALUES (NULL, ?, ?, ?);
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
        SET nombre = ?, apellidos = ?, email = ?
        WHERE Identificador = ?;
        """, (nombre, apellidos, email, identificador))
        connection.commit()
        print("Client updated.")

    elif option == 4:
        identificador = input("Client ID to delete: ")
        cursor.execute("DELETE FROM clientes WHERE Identificador = ?;", (identificador,))
        connection.commit()
        print("Client deleted.")

    elif option == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

connection.close()
# ===========================================================
# 6. FULL MENU EXAMPLE (CRUD PROGRAM) MYSQL – CEAC STYLE
# ===========================================================

import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",   # ← replace with your real password
    database="PortafolioDB"
)
cursor = connection.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
""")
connection.commit()

#########################################

print("=== CLIENT MANAGEMENT PROGRAM (MySQL) ===")

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
        VALUES (?, ?, ?);
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
        SET nombre = ?, apellidos = ?, email = ?
        WHERE Identificador = ?;
        """, (nombre, apellidos, email, identificador))
        connection.commit()
        print("Client updated.")

    elif option == 4:
        identificador = input("Client ID to delete: ")
        cursor.execute("DELETE FROM clientes WHERE Identificador = ?;", (identificador,))
        connection.commit()
        print("Client deleted.")

    elif option == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

connection.close()



# ===========================================================
# 7. EXTRA NOTES
# ===========================================================
# - The .db file (example: empresa.db) is automatically created.
# - You can open it with any SQLite viewer (e.g., DB Browser for SQLite).
# - The 'cursor.execute' command runs normal SQL.
# - Use '?' placeholders to safely insert values from variables.
# - After making changes (INSERT, UPDATE, DELETE), always call connection.commit().
# - To read data, use cursor.fetchall() or cursor.fetchone().

# ===========================================================
# 8. COMMON SQLITE COMMANDS (CHEAT SHEET)
# ===========================================================
# CREATE TABLE clients (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, email TEXT);
# INSERT INTO clients VALUES (NULL, 'Oscar', 'Sorensen', 'oscar@example.com');
# SELECT * FROM clients;
# UPDATE clients SET email='new@example.com' WHERE id=1;
# DELETE FROM clients WHERE id=1;
# ===========================================================
