--En esta tarea creo una vista en MySQL para combinar la información de dos tablas relacionadas: personas y emails. El objetivo es practicar el uso de claves foráneas y la instrucción CREATE VIEW, que permite simplificar consultas mostrando datos de varias tablas en una sola vista lógica.
--Primero se crea la base de datos ejemploclaves y las tablas personas y emails, definiendo sus claves primarias y la relación foránea entre ellas.
--Después se insertan datos de prueba y finalmente se construye la vista personas_correos, que utiliza un LEFT JOIN para mostrar todas las direcciones de correo junto con los nombres y apellidos de las personas vinculadas.

-- Tarea 9: Vistas 
CREATE DATABASE IF NOT EXISTS ejemploclaves;
USE ejemploclaves;

-- Creando la tabla personas y emails con claves primarias y foráneas
CREATE TABLE personas (
    identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(100)
);

-- Tabla emails con clave foránea a personas
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    direccion VARCHAR(100),
    persona INT,
    FOREIGN KEY (persona) REFERENCES personas(identificador)
);

-- Insertando datos de prueba
INSERT INTO personas (nombre, apellidos) VALUES
('Ana', 'López García'),
('Luis', 'Pérez Torres'),
('María', 'Fernández Ruiz');

INSERT INTO emails (direccion, persona) VALUES
('ana@gmail.com', 1),
('luis@empresa.com', 2),
('sin_persona@gmail.com', NULL);


-- Creando la VIEW
CREATE VIEW personas_correos AS
SELECT 
    personas.identificador,
    emails.direccion,
    personas.nombre,
    personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

-- Probando la VIEW
SELECT * FROM personas_correos;


--El ejercicio demuestra cómo las vistas permiten un acceso más simple y organizado a la información combinada de varias tablas, manteniendo la integridad de los datos y facilitando futuras consultas o informes.