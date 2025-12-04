
--Create
INSERT INTO clientes VALUES(
    '1234567A',
    'Oscar Sorensen'
    'Sjorman'
    'info@oscar.es'
):

-- SELECT
SELECT * FROM clientes;


--Selecting databases
USE --database, like "impresadam"

-- Update
UPDATE clientes
SET dni = '1111111A'
WHERE nombre = 'Oscar Sorensen';

SELECT * FROM clientes;

UPDATE clientes
SET apellidos = 'Garcia Lopez';
WHERE nombre = 'Oscar Sorensen'

--Delete

DELETE FROM clientes
WHERE dni = '1111111A';


