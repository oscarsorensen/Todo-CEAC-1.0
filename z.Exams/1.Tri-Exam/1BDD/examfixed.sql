"""
En este proyecto, diseñé una pequeña base de datos relacional llamada portafolioexamen.

Una base de datos relacional organiza la información en tablas que están conectadas por claves y relaciones. Cada tabla representa una entidad específica, por ejemplo, títulos, descripciones, fechas o autores. Los vínculos entre ellas garantizan la coherencia lógica y la consistencia de los datos.
El modelo relacional permite al sistema evitar duplicaciones, mantener la integridad y consultar de manera eficiente diferentes entidades. En este proyecto, la base de datos demuestra estos principios conectando las cuatro tablas (autores, libros, miembros y préstamos) mediante claves externas y restricciones.
Esta estructura refleja cómo los sistemas de información reales gestionan las relaciones entre los datos.
En general, portafolioexamen demuestra la aplicación práctica de la teoría de las bases de datos relacionales en un contexto realista, garantizando la organización, la precisión y la integridad de la información almacenada.

Para crear esta base de datos, utilicé comandos SQL estándar y seguí la lógica del diseño relacional.
Cada tabla tiene un ID autoincremental como clave principal, y los tipos de datos se eligieron en función de la información que se almacena: por ejemplo, VARCHAR para el texto e INT para el ID.

En la tarea, me aseguro de seguir el progreso de mis tablas, con show tables, describe y select* from xxx, para asegurarme de que todo se vea correcto. Todo parece estar bien, excepto que la próxima vez usaré un formulario de identificación diferente para autor_id y categoria_id para evitar confusiones.

"""
mysql -u useroscar -p 
-- ps is Oscar081100!

-- 1) CREATE DATABASE
CREATE DATABASE IF NOT EXISTS portafolioexamen;
USE portafolioexamen;

-- 2) CREATE TABLES
CREATE TABLE categoriasportafolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE piezasportafolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha VARCHAR(50),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categoriasportafolio(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- 3) INSERT DATA
INSERT INTO categoriasportafolio (name) VALUES
('Fotografía'),
('Diseño Gráfico'),
('Desarrollo Web');

INSERT INTO piezasportafolio (title, descripcion, fecha, categoria_id) VALUES
('Proyecto 1', 'Descripción del proyecto 1', '2023-01-15', 1),
('Proyecto 2', 'Descripción del proyecto 2', '2023-02-20', 2),
('Proyecto 3', 'Descripción del proyecto 3', '2023-03-10', 3);

-- 4) LEFT JOIN
SELECT 
    p.id AS pieza_id,
    p.title,
    c.name AS categoria_nombre
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c
ON p.categoria_id = c.id;

-- 5) CREATE VIEW
CREATE OR REPLACE VIEW piezasportafolio_con_categoriasportafolio AS
SELECT 
    p.title,
    p.descripcion,
    p.fecha,
    c.name AS categoria_nombre
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c
ON p.categoria_id = c.id;


-- 6) VERIFY VIEW
SELECT * FROM piezasportafolio_con_categoriasportafolio;

-- 7) CREATE USER WITH PERMISSIONS
CREATE USER IF NOT EXISTS 'exam_user'@'localhost' IDENTIFIED BY 'Oscar12345!';
GRANT SELECT, INSERT, UPDATE, DELETE ON portafolioexamen.* TO 'exam_user'@'localhost';
FLUSH PRIVILEGES;

-- 8) CRUD DEMONSTRATION
-- Read specific columns
SELECT title, fecha FROM piezasportafolio;

-- Conditional read
SELECT * FROM piezasportafolio WHERE categoria_id = 2;

-- Update data
UPDATE piezasportafolio SET title = 'Proyecto 1 Actualizado' WHERE id = 1;

-- Delete data
DELETE FROM piezasportafolio WHERE id = 1;

-- 9) FINAL CHECKS
SHOW TABLES;
DESCRIBE categoriasportafolio;
DESCRIBE piezasportafolio;
SELECT * FROM piezasportafolio_con_categoriasportafolio;

"""
La base de datos cumple su propósito: conecta todas las tablas correctamente y evita errores en los datos almacenados.
Gracias a su estructura, los registros se mantienen coherentes y el acceso a la información es más rápido y seguro.
Además, el diseño demuestra cómo una base de datos relacional puede organizar la información real de forma clara y estructurada, aplicando reglas que garantizan la integridad de los datos.
En resumen, portafolioexamen es un ejemplo sencillo pero completo de cómo se puede aplicar SQL para crear un sistema fiable, ordenado y fácil de mantener.
"""