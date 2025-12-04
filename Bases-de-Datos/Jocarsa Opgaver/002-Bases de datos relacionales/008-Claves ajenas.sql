-- En este ejercicio trabajo con claves primarias y claves ajenas dentro de una base de datos relacional.
-- El objetivo es comprender cómo se relacionan dos tablas mediante un identificador común.
-- Para ello, creo una base de datos llamada "ejemploclaves" con las tablas "personas" y "emails".
-- La tabla "personas" contiene un campo autoincremental como clave primaria (id),
-- mientras que la tabla "emails" incluye un campo "persona" que actúa como clave ajena,
-- estableciendo una relación directa con el identificador de la tabla "personas".
-- Finalmente, inserto registros en ambas tablas para comprobar que los valores se enlazan correctamente.
-- Posteriormente realizo una petición cruzada (LEFT JOIN) para visualizar todos los correos junto
-- con los datos de las personas asociadas.

sudo mysql -u root -p

CREATE DATABASE ejemploclaves;
USE ejemploclaves;

CREATE TABLE personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL
);

CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    direccion VARCHAR(255),
    persona INT,
    FOREIGN KEY (persona) REFERENCES personas(id)
);

INSERT INTO personas (nombre, apellidos)
VALUES ('Juan', 'Perez'),
       ('Maria', 'Lopez'),
       ('Carlos', 'Sanchez');

INSERT INTO emails (direccion, persona)
VALUES ('Calle Maximino 123', 1),
       ('Avenida Siempre Viva 742', 2),
       ('Boulevard de los Sueños Rotos 456', 3);

SELECT * FROM personas;
SELECT * FROM emails;


SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.id;

-- A través de este ejercicio comprobé el funcionamiento de las claves ajenas en MySQL.
-- Entendí que una clave primaria identifica de forma única cada registro,
-- mientras que una clave ajena permite conectar información entre tablas diferentes.
-- Gracias a la petición cruzada (LEFT JOIN), pude ver cómo los datos de "emails"
-- se relacionan correctamente con los registros de "personas".
-- Este tipo de relación es fundamental en bases de datos relacionales,
-- ya que garantiza la integridad referencial y evita duplicar información.
