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
