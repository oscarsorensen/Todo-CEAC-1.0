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
