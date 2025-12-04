
----- NY UBUNTU KODE ER 1234 ---------

-- ✅ ACCESS AND SETUP
sudo mysql -u root -p;
sudo service mysql start
mysql -u useroscar -p

-- show database
show databases;

-- Select database
USE empresadam;

-- Check tables and structure
SHOW TABLES;
DESCRIBE clientes;

-- ✅ INSERT TEST DATA
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES ('12345678A', 'Nombre del cliente', 'Apellidos del cliente', 'algo@correo.com');

-- ✅ REMOVE OLD CONSTRAINT (if it exists)
-- Note: MySQL doesn’t support IF EXISTS for constraints. If it doesn’t exist, this will show an error — that’s fine.
ALTER TABLE clientes DROP CONSTRAINT comprobar_email;

-- ✅ ADD EMAIL FORMAT CHECK
ALTER TABLE clientes
ADD CONSTRAINT comprobar_email
CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

-- ✅ VERIFY CONSTRAINT
SELECT 
    tc.TABLE_NAME,
    cc.CONSTRAINT_NAME,
    cc.CHECK_CLAUSE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
JOIN INFORMATION_SCHEMA.CHECK_CONSTRAINTS AS cc
    ON tc.CONSTRAINT_NAME = cc.CONSTRAINT_NAME
WHERE tc.TABLE_SCHEMA = DATABASE()
  AND tc.TABLE_NAME = 'clientes';

-- ✅ TEST VALID EMAIL (should work)
INSERT INTO clientes VALUES (NULL, '87654321B', 'Juan', 'García', 'juan@gmail.com');

-- ❌ TEST INVALID EMAIL (should fail)
INSERT INTO clientes VALUES (NULL, '87654321B', 'Juan', 'García', 'juangmail.com');
