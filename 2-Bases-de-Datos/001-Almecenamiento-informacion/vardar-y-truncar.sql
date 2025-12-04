-- Delete all rows in the table
DELETE FROM clientes;

-- Insert one valid client
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES (
    '12345678A',
    'Oscar Sorensen',
    'Sjorman',
    'oscar@gmail.com'
);

-- Show all current clients
SELECT * FROM clientes;

TRUNCATE TABLE clientes; -- resetea la tabla pero no se la carga


INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES (
    '12345678A',
    'Oscar Sorensen',
    'Sjorman',
    'oscar@gmail.com'
);

SELECT * FROM clientes;

DROP TABLE clientes; --mucho cuidado conesto porque borra la tabla.