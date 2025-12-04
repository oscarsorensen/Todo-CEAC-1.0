

-- ============================================================
--  EXAM DATABASE SETUP SCRIPT — PORTAFOLIO EXAMEN
--  Author: Oscar Sørensen
--  Use: Copy and run this script in MySQL to create everything
-- ============================================================

sudo service mysql start
mysql -u root -p
SHOW DATABASES;
DROP DATABASE IF EXISTS portafolioexamen;


-- 1) Create database and use it
CREATE DATABASE IF NOT EXISTS portafolioexamen;
USE portafolioexamen;

-- 2) Create table for categories
CREATE TABLE categoriasportafolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

-- 3) Create table for portfolio pieces
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

-- 4) Insert example data
INSERT INTO categoriasportafolio (name) VALUES
('Fotografía'),
('Diseño Gráfico'),
('Desarrollo Web');

INSERT INTO piezasportafolio (title, descripcion, fecha, categoria_id) VALUES
('Proyecto 1', 'Descripción del proyecto 1', '2023-01-15', 1),
('Proyecto 2', 'Descripción del proyecto 2', '2023-02-20', 2),
('Proyecto 3', 'Descripción del proyecto 3', '2023-03-10', 3);

-- 5) Create a LEFT JOIN view (for verification or integration)
CREATE OR REPLACE VIEW piezasportafolio_con_categoriasportafolio AS
SELECT 
    p.title,
    p.descripcion,
    p.fecha,
    c.name AS categoria_nombre
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c
ON p.categoria_id = c.id;


-- 6) Create exam user with permissions (optional if already exists)
CREATE USER IF NOT EXISTS 'useroscar'@'localhost' IDENTIFIED BY 'Oscar081100!';
GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'useroscar'@'localhost';
FLUSH PRIVILEGES;

-- 7) Verify everything works
SHOW TABLES;
DESCRIBE categoriasportafolio;
DESCRIBE piezasportafolio;
SELECT * FROM piezasportafolio_con_categoriasportafolio;

