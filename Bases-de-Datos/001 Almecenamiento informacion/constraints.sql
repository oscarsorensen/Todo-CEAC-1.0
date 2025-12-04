/* ===============================================================
   🧾  CLIENTES TABLE — CONSTRAINTS NOTES AND COMMANDS
   =============================================================== */

/* ---------------------------------------------------------------
   1️⃣  SELECT DATABASE AND CHECK TABLES
   --------------------------------------------------------------- */

-- Make sure you're using the correct database
USE empresadam;

-- Show all tables in this database
SHOW TABLES;

-- View structure of the clientes table
DESCRIBE clientes;


/* ---------------------------------------------------------------
   2️⃣  VIEW EXISTING CHECK CONSTRAINTS
   --------------------------------------------------------------- */

-- List all CHECK constraints for the clientes table
SELECT 
    tc.TABLE_NAME,
    cc.CONSTRAINT_NAME,
    cc.CHECK_CLAUSE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
JOIN INFORMATION_SCHEMA.CHECK_CONSTRAINTS AS cc
    ON tc.CONSTRAINT_NAME = cc.CONSTRAINT_NAME
WHERE tc.TABLE_SCHEMA = DATABASE()
  AND tc.TABLE_NAME = 'clientes';


/* ---------------------------------------------------------------
   3️⃣  DROP AN EXISTING CONSTRAINT
   --------------------------------------------------------------- */

-- Example: Drop the DNI/NIE constraint if it already exists
ALTER TABLE clientes DROP CONSTRAINT comprobar_dni;

-- Example: Drop a renamed constraint if needed
ALTER TABLE clientes DROP CONSTRAINT comprobar_dni_nie_letra;


/* ---------------------------------------------------------------
   4️⃣  ADD CONSTRAINTS
   --------------------------------------------------------------- */

-- ✅ Add email format constraint
ALTER TABLE clientes
ADD CONSTRAINT comprobar_email
CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

-- ✅ Add DNI/NIE format constraint
ALTER TABLE clientes
ADD CONSTRAINT comprobar_dni_nie_letra
CHECK (dni REGEXP '^([0-9]{8}[A-Z]|[XYZ][0-9]{7}[A-Z])$');


/* ---------------------------------------------------------------
   5️⃣  TEST VALID INSERTS
   --------------------------------------------------------------- */

-- DNI example (valid)
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES ('12345678A', 'Carlos López', 'Martínez', 'carlos.lopez@gmail.com');

-- NIE example (valid)
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES ('X2345678B', 'Ana Torres', 'Serrano', 'ana.torres@empresa.com');

-- ❌ Invalid DNI (fails)
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES ('1234567A', 'Oscar Sorensen', 'Sjorman', 'oscar@example.com');

-- ❌ Invalid email (fails)
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES ('Y7654321C', 'Lucía Fernández', 'Morales', 'lucia.fernandezmail.es');


/* ---------------------------------------------------------------
   6️⃣  VERIFY CONSTRAINTS AGAIN
   --------------------------------------------------------------- */

-- Confirm both constraints exist
SELECT 
    tc.TABLE_NAME,
    cc.CONSTRAINT_NAME,
    cc.CHECK_CLAUSE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
JOIN INFORMATION_SCHEMA.CHECK_CONSTRAINTS AS cc
    ON tc.CONSTRAINT_NAME = cc.CONSTRAINT_NAME
WHERE tc.TABLE_SCHEMA = DATABASE()
  AND tc.TABLE_NAME = 'clientes';


/* ---------------------------------------------------------------
   7️⃣  VIEW COMPLETE TABLE DEFINITION
   --------------------------------------------------------------- */

-- Show the full CREATE TABLE SQL (includes constraints)
SHOW CREATE TABLE clientes;


/* ---------------------------------------------------------------
   8️⃣  OPTIONAL CLEANUP OR RENAME
   --------------------------------------------------------------- */

-- Rename column if you want to fix typo (idenficador → identificador)
ALTER TABLE clientes CHANGE idenficador identificador INT NOT NULL AUTO_INCREMENT;

/* ===============================================================
   END OF NOTES — CLIENTES CONSTRAINT MANAGEMENT
   =============================================================== */
