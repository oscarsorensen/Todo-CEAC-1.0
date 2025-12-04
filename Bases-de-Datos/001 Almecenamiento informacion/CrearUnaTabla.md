SHOW TABLES;
Empty set(0,00 sec)


CREATE TABLE clientes (

    dni VARCHAR(9),
    nombre VARCHAR(50),
    appelidos VARCHAR(255),
    email VARCHAR(100)

);

INSERT INTO clientes VALUES(
    '1234567A',
    'Oscar Sorensen',
    'Sjorman',
    'info@oscar.es'


);