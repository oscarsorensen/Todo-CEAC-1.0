

ALTER TABLE clientes
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
    PRIMARY KEY FIRST;

ALTER = Altera
TABLE = Tabla
clientes = la tabla que quiero realizar
ADD = la operacion que quiero hacer
COLUMN = quiero anadir una columna
identificador = nombre de la columna que quiero anadir
INT = el tipo de dato que va a tener la columna (entero)
AUTO_INCREMENT = el numero va a crecer automaticamente
PRIMARY KEY = clave primaria
FIRST = si hay varias, esta tiene prioridad

DESCRIBE clientes;

INSERT INTO clientes
VALUES()
    NULL,
    `1234567A`,
    `Oscar Sorensen`,
    `Sjorman`,
    `oscar@gmail.com`);

SELECT * FROM clientes;

