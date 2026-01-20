sudo mysql -u root -p

CREATE DATABASE empresa2026;
USE empresa2026;

CREATE TABLE clientes(
	nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

INSERT INTO clientes VALUES(
	"Jose Vicente",
  "Carratala",
  "info@jocarsa.com"
);

SELECT * FROM clientes;


-- Crear usuario y asignar permisos

CREATE USER 
'empresa2026'@'localhost' 
IDENTIFIED  BY 'Empresa2026$';


GRANT USAGE ON *.* TO 'empresa2026'@'localhost';

ALTER USER 'empresa2026'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empresa2026.* 
TO 'empresa2026'@'localhost';

FLUSH PRIVILEGES;