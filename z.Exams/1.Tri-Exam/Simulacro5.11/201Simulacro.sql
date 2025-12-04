"En este ejercicio se diseña la base de datos de un portafolio digital, que servirá para almacenar información sobre las piezas o trabajos realizados por un autor.
La finalidad es organizar los proyectos por categorías, de manera que cada pieza tenga su título, descripción, imagen y un enlace de referencia.
El trabajo permite comprender cómo se relacionan las tablas mediante claves primarias y foráneas, y cómo usar vistas para simplificar consultas entre tablas relacionadas."

"Se inicia el servicio de MySQL y se crea una base de datos llamada PortafolioDB. Dentro de ella se definen las entidades Categoria y Pieza. La tabla Categoria contiene los campos id, titulo y descripcion, con id como clave primaria. La tabla Pieza incluye id, titulo, descripcion, imagen, url y categoria_id, este último configurado como clave foránea que referencia a Categoria(id) con las acciones ON UPDATE CASCADE y ON DELETE RESTRICT.

Después se realiza una consulta mediante LEFT JOIN entre Pieza y Categoria para combinar los datos de ambas tablas y mostrar las piezas junto a su categoría correspondiente. A continuación, se crea una vista denominada pieza_con_categoria basada en esa unión, lo que permite acceder fácilmente a la información combinada desde una sola estructura lógica."
-- empezar mysql en terminal
sudo mysql -u root -p;
mysql -u useroscar -p


show databases;
-- Crear base de datos PortafolioDB
CREATE DATABASE PortafolioDB;

USE PortafolioDB;

-- Crear tablas Categoria y Pieza con claves primarias
CREATE TABLE IF NOT EXISTS Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Pieza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id) 
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    url VARCHAR(255) NOT NULL
);

-- Hacer un LEFT JOIN entre Pieza y Categoria
SELECT 
    Pieza.id AS pieza_id,
    Pieza.titulo AS pieza_titulo,
    Categoria.titulo AS categoria_titulo
FROM Pieza
LEFT JOIN Categoria
ON Pieza.categoria_id = Categoria.id;

-- Crear una vista llamada pieza_con_categoria

CREATE OR REPLACE VIEW pieza_con_categoria AS
SELECT 
    Pieza.titulo,
    Pieza.descripcion,
    Categoria.titulo AS categoria_titulo
FROM Pieza
LEFT JOIN Categoria
ON Pieza.categoria_id = Categoria.id;

-- testear la vista

use PortafolioDB;

INSERT INTO Categoria (titulo, descripcion)
VALUES ('Diseño Web', 'Proyectos web'), ('Programación', 'Aplicaciones backend');

INSERT INTO Pieza (titulo, descripcion, imagen, categoria_id, url)
VALUES 
('Blog personal', 'Proyecto Flask con base de datos MySQL.', 'example.jpg', 1, 'https://example.com'),
('Gestor de clientes', 'Aplicación CRUD creada en Python.', 'example.jpg', 2, 'https://example.com');

SELECT database();

-- Ver las vistas creadas

SHOW FULL TABLES WHERE TABLE_TYPE = 'VIEW';

"Este ejercicio me ha servido para reforzar mis conocimientos sobre cómo crear y relacionar tablas dentro de una base de datos relacional. Se ha demostrado la utilidad de las claves primarias y externas para mantener la integridad de los datos, así como el uso del comando JOIN para vincular información de diferentes tablas.La creación de la vista final que hago facilita el acceso a todos los datos combinados y muestra cómo aplicar estos conceptos en un proyecto real, como un portafolio web donde las piezas están organizadas por categorías."