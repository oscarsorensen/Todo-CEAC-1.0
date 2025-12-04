
-- =====================================================================
-- EXAMEN RESUMEN - BASES DE DATOS (UNIDAD 002)
-- Autor: Oscar Sørensen
-- Contexto: Proyecto Blog / Portafolio
-- Este archivo reúne todos los apuntes y ejemplos en un único script.
-- Cada bloque incluye comentarios explicativos y ejemplos listos para usar.
-- =====================================================================

-- 1. CREACIÓN DE BASE DE DATOS
-- 2. CREACIÓN DE TABLAS CON CLAVES Y RESTRICCIONES
-- 3. INSERCIÓN DE DATOS
-- 4. CONSULTAS Y LEFT JOIN
-- 5. CREACIÓN DE VISTAS
-- 6. GESTIÓN DE USUARIOS Y PERMISOS
-- 7. EJEMPLOS DE CONSULTAS FINALES



-- ====================================================
-- Contenido original de: Notes Unit 002/notes.sql
-- ====================================================

-- ===========================================================
-- UNIT 002 – RELATIONAL DATABASES (CEAC)
-- Full study file | Author: Oscar Sørensen
-- ===========================================================
-- This file combines theory, SQL commands, and practical notes.
-- All explanations are written as SQL comments so it can be executed
-- safely inside MySQL Workbench or any SQL terminal.
-- ===========================================================


-- ===========================================================
-- 1. INSTALLATION AND ACCESS COMMANDS
-- ===========================================================
-- On Linux:
--   sudo apt update
--   sudo apt install mysql-server
--   sudo systemctl start mysql
--   sudo mysql_secure_installation

-- Access MySQL as root user:
--   sudo mysql -u root -p
-- (then enter your password)


-- ===========================================================
-- 2. BASIC MYSQL COMMANDS
-- ===========================================================

-- Show all existing databases in the system:
SHOW DATABASES;

-- Create a new database:
CREATE DATABASE empresadam;

-- Select (use) a database to work inside:
USE empresadam;

-- Show all tables inside the currently selected database:
SHOW TABLES;

-- Describe the structure of a table (columns, types, constraints):
DESCRIBE clients;

-- Delete an entire database (be very careful!):
DROP DATABASE empresadam;

-- ===========================================================
-- 3. CREATE AND MANAGE TABLES
-- ===========================================================
-- Creating a table means defining its structure:
-- name of columns, data types, and constraints.

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    dni VARCHAR(9)
);

-- To check the table structure:
DESCRIBE clients;

-- To rename a table:
RENAME TABLE clients TO customers;

-- To delete a table:
DROP TABLE customers;

-- ===========================================================
-- 4. DATA TYPES (MOST COMMON IN MYSQL)
-- ===========================================================
-- INT: whole numbers
-- DECIMAL(p,s): exact decimals (example: DECIMAL(5,2) = 999.99)
-- FLOAT, DOUBLE: approximate decimals
-- CHAR(n): fixed-length text
-- VARCHAR(n): variable-length text (common for names, emails)
-- DATE: date (YYYY-MM-DD)
-- DATETIME / TIMESTAMP: date + time
-- BOOLEAN: true/false (1 or 0)
-- TEXT: long text content

-- Example:
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(6,2),
    in_stock BOOLEAN,
    created_at DATETIME
);

-- ===========================================================
-- 5. BASIC CRUD COMMANDS
-- ===========================================================
-- CRUD = Create, Read, Update, Delete

-- Create (insert data):
INSERT INTO products (name, price, in_stock)
VALUES ('Protein Bar', 2.99, TRUE);

-- Read (query data):
SELECT * FROM products;

-- Read only certain columns:
SELECT name, price FROM products;

-- Read with conditions:
SELECT * FROM products WHERE price > 5.00;

-- Update data:
UPDATE products SET price = 3.49 WHERE id = 1;

-- Delete data:
DELETE FROM products WHERE id = 1;

-- Remove all data but keep the table:
TRUNCATE TABLE products;

-- ===========================================================
-- 6. PRIMARY KEYS
-- ===========================================================
-- A PRIMARY KEY uniquely identifies each row.
-- It cannot be NULL and cannot repeat.

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL
);

-- If a table already exists, you can add a primary key later:
ALTER TABLE members ADD PRIMARY KEY (member_id);

-- ===========================================================
-- 7. VALIDATION CONSTRAINTS (CHECK, UNIQUE, NOT NULL)
-- ===========================================================
-- NOT NULL: column cannot be empty
-- UNIQUE: all values must be different
-- CHECK: enforces a condition
-- DEFAULT: gives a value if none is provided

CREATE TABLE gym_clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(9) UNIQUE,
    age INT CHECK (age >= 16),
    weight DECIMAL(5,2) DEFAULT 70.0
);

-- Example of invalid insertion (age too low):
-- INSERT INTO gym_clients (dni, age) VALUES ('12345678A', 12);

-- ===========================================================
-- 8. FOREIGN KEYS (RELATION BETWEEN TABLES)
-- ===========================================================
-- A FOREIGN KEY connects two tables using a shared field.

CREATE TABLE persons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    email VARCHAR(100),
    FOREIGN KEY (person_id) REFERENCES persons(id)
);

-- This ensures each email belongs to an existing person.

-- ===========================================================
-- 9. INDEXES
-- ===========================================================
-- Indexes speed up searches in large tables.
-- They can be created automatically (with PRIMARY/UNIQUE)
-- or manually on frequently searched columns.

CREATE INDEX idx_name ON persons(name);

-- To view existing indexes:
SHOW INDEX FROM persons;

-- ===========================================================
-- 10. NULL VALUE
-- ===========================================================
-- NULL represents “no value”. It is not 0 or empty text.
-- Example table with NULL values allowed:

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    amount DECIMAL(6,2),
    notes TEXT NULL
);

-- Selecting rows where notes are NULL:
SELECT * FROM orders WHERE notes IS NULL;

-- Selecting rows where notes have content:
SELECT * FROM orders WHERE notes IS NOT NULL;

-- ===========================================================
-- 11. VIEWS
-- ===========================================================
-- A VIEW is a virtual table created from a query.
-- It helps simplify complex queries or protect data.

CREATE VIEW active_products AS
SELECT name, price FROM products WHERE in_stock = TRUE;

-- View data like a normal table:
SELECT * FROM active_products;

-- Delete a view:
DROP VIEW active_products;

-- ===========================================================
-- 12. USERS AND PRIVILEGES
-- ===========================================================
-- MySQL allows creating different users with specific permissions.

-- Create a new user:
CREATE USER 'empresadam2'@'localhost' IDENTIFIED BY 'password123';

-- Give permissions (example: all privileges on one DB):
GRANT ALL PRIVILEGES ON empresadam.* TO 'empresadam2'@'localhost';

-- Remove privileges:
REVOKE ALL PRIVILEGES ON empresadam.* FROM 'empresadam2'@'localhost';

-- Show current users and privileges:
SELECT user, host FROM mysql.user;

-- ===========================================================
-- 13. SQL LANGUAGES: DDL, DML, DCL
-- ===========================================================
-- DDL – Data Definition Language:
--   Defines structure: CREATE, ALTER, DROP
-- DML – Data Manipulation Language:
--   Manages data: INSERT, UPDATE, DELETE, SELECT
-- DCL – Data Control Language:
--   Controls permissions: GRANT, REVOKE

-- Example summary:
-- CREATE TABLE = DDL
-- INSERT INTO = DML
-- GRANT PRIVILEGES = DCL

-- ===========================================================
-- 14. RELATIONAL MODEL – KEY CONCEPTS
-- ===========================================================
-- Database: structured collection of related data.
-- Table (Relation): structure with rows (tuples) and columns (attributes).
-- Row (Tuple): a single record.
-- Column (Attribute): a field representing one type of data.
-- Primary Key: unique identifier of each record.
-- Foreign Key: references another table’s primary key.
-- Relationship types:
--   1:1 (one-to-one)
--   1:N (one-to-many)
--   N:M (many-to-many, usually via intermediate table)
-- Referential Integrity: ensures linked data stays consistent.
-- Example: you cannot delete a person if emails still reference it.

-- ===========================================================
-- 15. PYTHON + MYSQL CRUD CONNECTION (REFERENCED IN SECTION 5)
-- ===========================================================
-- These examples use the mysql-connector-python library.
-- They show how to perform basic CRUD operations from Python.
-- You can save these as .py files.

-- Install the connector (Linux/Mac/Windows terminal):
--   pip install mysql-connector-python

-- ----------------------------
-- insert_data.py
-- ----------------------------
-- import mysql.connector
--
-- conn = mysql.connector.connect(
--     host="localhost",
--     user="empresadam2",
--     password="password123",
--     database="empresadam"
-- )
-- cursor = conn.cursor()
-- sql = "INSERT INTO clients (name, surname, email) VALUES (%s, %s, %s)"
-- values = ("Oscar", "Sorensen", "oscar@example.com")
-- cursor.execute(sql, values)
-- conn.commit()
-- print(cursor.rowcount, "record inserted.")
-- conn.close()

-- ----------------------------
-- read_data.py
-- ----------------------------
-- import mysql.connector
--
-- conn = mysql.connector.connect(
--     host="localhost",
--     user="empresadam2",
--     password="password123",
--     database="empresadam"
-- )
-- cursor = conn.cursor()
-- cursor.execute("SELECT * FROM clients")
-- for row in cursor.fetchall():
--     print(row)
-- conn.close()

-- ----------------------------
-- update_data.py
-- ----------------------------
-- sql = "UPDATE clients SET email = %s WHERE id = %s"
-- values = ("newmail@example.com", 1)
-- cursor.execute(sql, values)
-- conn.commit()

-- ----------------------------
-- delete_data.py
-- ----------------------------
-- sql = "DELETE FROM clients WHERE id = %s"
-- value = (1,)
-- cursor.execute(sql, value)
-- conn.commit()

-- ===========================================================
-- END OF FILE
-- ===========================================================



-- ====================================================
-- Contenido original de: Notes Unit 002/notesCompact.sql
-- ====================================================

-- ===========================================================
-- UNIT 002 – RELATIONAL DATABASES (CEAC)
-- COMPLETE AND CLEAR CHEAT SHEET
-- ===========================================================

-- ===========================================================
-- 0.1 ACCESSING MYSQL FROM THE TERMINAL
-- ===========================================================
-- Step 1: Open the terminal.

-- Step 2: Log in to MySQL as the root user.
-- You will be asked for the MySQL password you created during installation.
sudo mysql -u root -p

-- Step 3: (Optional) See all existing databases.
SHOW DATABASES;

-- Step 4: Create a new database if you need one.
CREATE DATABASE company_database;

-- Step 5: Select the database you want to use.
USE company_database;

-- Step 6: Verify that you are inside the correct database.
SELECT DATABASE();

-- Step 7: Start creating or managing tables normally.
SHOW TABLES;

-- ===========================================================
-- BASIC NAVIGATION
-- ===========================================================
SHOW DATABASES;                         -- Show all databases in MySQL
CREATE DATABASE company_database;        -- Create a new database
USE company_database;                    -- Select a database to work in
SHOW TABLES;                             -- Show all tables in the selected database
DESCRIBE clients;                        -- Show the structure of a specific table

-- ===========================================================
-- TABLE MANAGEMENT (DDL – Data Definition Language)
-- ===========================================================
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(100),
    email VARCHAR(100)
);                                       -- Create a new table with four columns

ALTER TABLE clients ADD COLUMN age INT;  -- Add a new column called "age"
DROP TABLE clients;                      -- Delete the table completely
TRUNCATE TABLE clients;                  -- Delete all rows but keep the structure

-- ===========================================================
-- DATA TYPES (MOST COMMON)
-- ===========================================================
-- INT – whole numbers
-- DECIMAL(5,2) – exact decimal numbers (up to 999.99)
-- VARCHAR(100) – variable length text (up to 100 characters)
-- DATE – only date (YYYY-MM-DD)
-- DATETIME – date and time
-- BOOLEAN – true or false (1 or 0)
-- TEXT – long text field

-- ===========================================================
-- CRUD COMMANDS (DML – Data Manipulation Language)
-- ===========================================================
-- CREATE – insert new data
INSERT INTO clients (name, surname, email)
VALUES ('Oscar', 'Sorensen', 'oscar@example.com');

-- READ – show stored data
SELECT * FROM clients;                   -- Show every column and row
SELECT name, email FROM clients;         -- Show only specific columns
SELECT * FROM clients WHERE age > 18;    -- Show rows that meet a condition

-- UPDATE – change existing data
UPDATE clients
SET email = 'newmail@example.com'
WHERE id = 1;

-- DELETE – remove data
DELETE FROM clients WHERE id = 1;        -- Delete only one record
TRUNCATE TABLE clients;                  -- Delete all records

-- ===========================================================
-- CONSTRAINTS (RULES THAT PROTECT DATA)
-- ===========================================================
PRIMARY KEY (id);                        -- Unique identifier for each record
FOREIGN KEY (person_id) REFERENCES persons(id);  -- Link between tables
UNIQUE (email);                          -- Prevent duplicate values
NOT NULL;                                -- Column must always have a value
CHECK (age >= 16);                       -- Condition that must be true
DEFAULT 70.0;                            -- Automatic value if none is given

-- ===========================================================
-- INDEXES (SEARCH SPEED)
-- ===========================================================
CREATE INDEX index_name ON clients(name); -- Create an index on a column
SHOW INDEX FROM clients;                  -- Display all indexes of a table

-- ===========================================================
-- VIEWS (VIRTUAL TABLES)
-- ===========================================================
CREATE VIEW adult_clients AS
SELECT name, surname, email FROM clients WHERE age >= 18;
SELECT * FROM adult_clients;              -- Use the view like a table
DROP VIEW adult_clients;                  -- Delete the view

-- ===========================================================
-- USERS AND PRIVILEGES (DCL – Data Control Language)
-- ===========================================================
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON company_database.* TO 'new_user'@'localhost';
REVOKE ALL PRIVILEGES ON company_database.* FROM 'new_user'@'localhost';
FLUSH PRIVILEGES;                         -- Refresh permission changes

-- ===========================================================
-- NULL VALUES
-- ===========================================================
SELECT * FROM clients WHERE email IS NULL;     -- Show rows with no email
SELECT * FROM clients WHERE email IS NOT NULL; -- Show rows that have an email

-- ===========================================================
-- RELATIONSHIPS BETWEEN TABLES
-- ===========================================================
-- ONE TO ONE:   Each record in Table A has exactly one match in Table B
-- ONE TO MANY:  One record in Table A is linked to many in Table B
-- MANY TO MANY: Many records in Table A are linked to many in Table B
--                (requires a third linking table)

-- ===========================================================
-- PYTHON CONNECTOR REMINDER
-- ===========================================================
-- See Section 15 of main study file for full examples.
-- Library needed: mysql-connector-python
-- Installation: pip install mysql-connector-python
-- Use Python to connect to MySQL and run CRUD operations.

-- ===========================================================
-- END OF CLEAR CHEAT SHEET
-- ===========================================================



-- ====================================================
-- Contenido original de: Notes Unit 002/specifikeksamen.sql
-- ====================================================

-- ============================
-- UNIVERSAL SQL EXAM TEMPLATE
-- Adapt by renaming keywords only
-- ============================
-- ==============================================================
-- HOW TO USE THIS TEMPLATE (EXAM INSTRUCTIONS)
-- ============================================================== 
-- 1) This file is a universal exam skeleton. 
--    You only need to rename the database and table names 
--    to fit the assignment (blog, journal, ads, etc.).
--
-- 2) Example replacements:
--      examdb    →  blog
--      category  →  autores / usuarios
--      item      →  entradas / publicaciones
--
-- 3) Steps this template already covers:
--    - Create database
--    - Create two related tables (1:N relationship)
--    - Define primary and foreign keys
--    - Example LEFT JOIN
--    - Create a view
--    - Create a user with permissions
--
-- 4) Optional: Run the INSERT examples to test your tables.
--    They can be deleted before submission.
--
-- 5) To adapt fast in exam:
--    a) Change names (Ctrl+H)
--    b) Execute the script section by section
--    c) Verify each part with:
--         SHOW TABLES;
--         DESCRIBE table_name;
--         SELECT * FROM view_name;
--
-- Ready for use with MySQL 8 (CEAC exam environment)
-- ==============================================================

-- 1) CREATE DATABASE
CREATE DATABASE IF NOT EXISTS examdb;
USE examdb;

-- 2) CREATE TABLES
CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    category_id INT,
    date DATE,
    image VARCHAR(255),
    content TEXT,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- 3) LEFT JOIN EXAMPLE
SELECT 
    item.id AS item_id,
    item.title,
    category.name AS category_name
FROM item
LEFT JOIN category
ON item.category_id = category.id;

-- 4) CREATE VIEW
CREATE OR REPLACE VIEW items_with_category AS
SELECT 
    item.title,
    item.date,
    category.name AS category_name
FROM item
LEFT JOIN category
ON item.category_id = category.id;

-- 5) CREATE USER WITH PERMISSIONS
CREATE USER IF NOT EXISTS 'exam_user'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON examdb.* TO 'exam_user'@'localhost';
FLUSH PRIVILEGES;

-- 6) TEST DATA (optional for checking)
INSERT INTO category (name, email)
VALUES ('Oscar Sørensen', 'oscar@example.com'),
       ('José Vicente', 'jose@example.com');

INSERT INTO item (title, category_id, date, image, content)
VALUES ('First entry', 1, CURDATE(), 'example.jpg', 'Sample text.');



-- ====================================================
-- Contenido original de: Notes Unit 002/viewNotes.sql
-- ====================================================

-- ===========================================================
-- UNIT: VIEWS AND USERS IN RELATIONAL DATABASES
-- ===========================================================

-- ===========================================================
-- 1. CONCEPT OF A VIEW
-- ===========================================================
-- A VIEW is a saved SQL query that behaves like a virtual table.
-- It does not store data physically; it displays results from a SELECT.
-- Views are useful to simplify complex queries and limit access to sensitive data.

-- CREATE a view:
CREATE VIEW people_emails AS
SELECT 
    persons.id,              -- person's unique identifier
    persons.name,
    persons.surname,
    emails.address           -- email address linked to that person
FROM emails
LEFT JOIN persons
ON emails.person = persons.id;

-- VERIFY that the view works:
SELECT * FROM people_emails;  -- The view behaves like a table

-- DELETE a view:
DROP VIEW people_emails;

-- NOTES:
-- - A view can combine multiple tables using JOIN.
-- - It saves only the query definition, not the data itself.
-- - It can protect data by showing only selected fields to users.

-- ===========================================================
-- 2. SHOWING USERS IN A MYSQL SYSTEM
-- ===========================================================
-- MySQL stores users in the internal table mysql.user.
-- To list all users in the system:

SELECT User, Host FROM mysql.user;   -- shows username and host
SELECT * FROM mysql.user;            -- shows full details (advanced)

-- ===========================================================
-- 3. CREATING A NEW USER
-- ===========================================================
-- Creates a new user called 'new_user' that can connect locally.
-- IMPORTANT: replace 'password123' with a secure password.

CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';

-- ===========================================================
-- 4. ASSIGNING PRIVILEGES TO A USER
-- ===========================================================
-- GRANT is used to give a user permission to access databases or tables.

-- Example: give full access to the database empresadam:
GRANT ALL PRIVILEGES ON empresadam.* TO 'new_user'@'localhost';

-- APPLY the changes so they take effect:
FLUSH PRIVILEGES;

-- ===========================================================
-- 5. KEY CONCEPTS TO REMEMBER FOR THE EXAM
-- ===========================================================
-- * VIEW: A stored SELECT query that acts like a virtual table.
-- * CREATE VIEW view_name AS SELECT ... ;
-- * SELECT FROM a view the same way as a table.
-- * DROP VIEW view_name; removes it.
-- * CREATE USER 'name'@'host' IDENTIFIED BY 'password';
-- * GRANT ALL PRIVILEGES ON database.* TO 'name'@'host';
-- * FLUSH PRIVILEGES; applies the permission changes.
-- * Views simplify complex queries.
-- * Users and privileges control security and data access in MySQL.



-- ====================================================
-- Contenido original de: Notes Unit 002/showcase.sql
-- ====================================================

Este ejercicio consistió en el diseño e implementación de un modelo de datos para la entidad Cliente, donde se creó una estructura de base de datos flexible y práctica para gestionar información de clientes. El enfoque principal fue desarrollar un esquema que se adaptara a escenarios reales donde los usuarios pueden no proporcionar toda su información personal durante el registro.

1. Crearemos una tabla llamada Cliente:

`
CREATE TABLE Cliente (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
`

2. Características del Modelo:

Clave primaria: dni
Todos los campos son opcionales excepto dni (por ser PK)
No hay restricciones de unicidad en email
Estructura flexible que permite registros parciales
Tipos VARCHAR para adaptarse a diferentes longitudes de texto

3. Insertar un ejemplo de Cliente:

`
INSERT INTO Cliente (dni, nombre, apellidos, email)
VALUES ('48763219M', 'Ayman', 'Mouzakki', 'ayman.mouzakki@ejemplo.com');
`

4. Consultar el cliente insertado:

`
SELECT * FROM Cliente WHERE dni = '48763219M';
`

Vamos a juntar las ideas que tenemos arriba para crear un programa completo:

`
CREATE TABLE Cliente (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO Cliente (dni, nombre, apellidos, email)
VALUES ('48763219M', 'Ayman', 'Mouzakki', 'ayman.mouzakki@ejemplo.com');

-- Consultar el cliente insertado
SELECT * FROM Cliente WHERE dni = '48763219M';
`

Este ejercicio sienta las bases para un sistema de gestión de clientes robusto pero flexible, preparado para extenderse con relaciones con otras entidades como pedidos, facturas o reservas en futuras iteraciones.


-- ====================================================
-- Contenido original de: Notes Unit 002/notesSQLlite.py
-- ====================================================

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


--########################################################################################################
-- =====================================================
-- EXAMEN DE BASES DE DATOS — BLOG
-- Autor: Oscar Sørensen
-- =====================================================

-- 1. Crear base de datos
CREATE DATABASE blogdb;
USE blogdb;

-- 2. Crear tabla de autores
CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100)
);

-- 3. Crear tabla de entradas (noticias)
CREATE TABLE entradas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200),
  fecha DATE,
  texto TEXT,
  imagen VARCHAR(200),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- 4. Insertar algunos datos de prueba
INSERT INTO autores (nombre, email) VALUES
('Oscar Sørensen', 'oscar@example.com'),
('José Vicente Carratalá', 'jvc@example.com');

INSERT INTO entradas (titulo, fecha, texto, imagen, autor_id) VALUES
('Primer post', '2025-11-09', 'Contenido del primer artículo.', 'example.jpg', 1),
('Segundo post', '2025-11-09', 'Otra entrada con más texto.', 'example2.jpg', 2);

-- 5. Crear LEFT JOIN para ver autores con sus entradas
SELECT e.id, e.titulo, e.fecha, a.nombre AS autor
FROM entradas e
LEFT JOIN autores a ON e.autor_id = a.id;

-- 6. Crear una vista combinando ambas tablas
CREATE VIEW vista_blog AS
SELECT e.titulo, e.fecha, e.texto, e.imagen, a.nombre AS autor
FROM entradas e
LEFT JOIN autores a ON e.autor_id = a.id;

-- 7. Crear un usuario y asignar permisos
CREATE USER 'userblog'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON blogdb.* TO 'userblog'@'localhost';
FLUSH PRIVILEGES;

-- 8. Comprobación rápida
SELECT * FROM vista_blog;
