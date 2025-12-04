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
CREATE TABLE categoriasportafolio(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE piezasportafolio(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) not NULL,
    descripcion TEXT,
    fecha varchar (50),
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES categoriasportafolio(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    categoria_id INT
);

-- data insercion ejemplo categoriasportafolio
INSERT INTO categoriasportafolio (name) VALUES
('Fotografia'),
('Diseno Grafico'),
('Desarrollo Web');

-- data insercion ejemplo piezasportafolio
INSERT INTO piezasportafolio (title, descripcion, fecha, autor_id, categoria_id) VALUES
('Proyecto 1', 'Descripcion del proyecto 1', '2023-01-15', 1, 1),
('Proyecto 2', 'Descripcion del proyecto 2', '2023-02-20', 2, 2),
('Proyecto 3', 'Descripcion del proyecto 3', '2023-03-10', 3, 3);

-- reading data
mysql> show tables;
+----------------------------+
| Tables_in_portafolioexamen |
+----------------------------+
| categoriasportafolio       |
| piezasportafolio           |
+----------------------------+

mysql> DESCRIBE categoriasportafolio;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
mysql> DESCRIBE piezasportafolio;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | NULL    | auto_increment |
| title        | varchar(150) | NO   |     | NULL    |                |
| descripcion  | text         | YES  |     | NULL    |                |
| fecha        | varchar(50)  | YES  |     | NULL    |                |
| autor_id     | int          | NO   | MUL | NULL    |                |
| categoria_id | int          | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+


-- 3) LEFT JOIN EXAMPLE
SELECT 
    piezasportafolio.id AS piezasportafolio_id,
    piezasportafolio.title,
    categoriasportafolio.name AS categoriasportafolio_name
FROM piezasportafolio
LEFT JOIN categoriasportafolio
on piezasportafolio.categoria_id = categoriasportafolio.id;

-- mostrando resultado

+---------------------+------------+---------------------------+
| piezasportafolio_id | title      | categoriasportafolio_name |
+---------------------+------------+---------------------------+
|                   1 | Proyecto 1 | Fotografia                |
|                   2 | Proyecto 2 | Diseno Grafico            |
|                   3 | Proyecto 1 | Fotografia                |
|                   4 | Proyecto 2 | Diseno Grafico            |
|                   5 | Proyecto 3 | Desarrollo Web            |
+---------------------+------------+---------------------------+

-- 4) CREATE VIEW EXAMPLE

CREATE OR REPLACE VIEW piezasportafolio_con_categoriasportafolio AS
SELECT 
    piezasportafolio.title,
    piezasportafolio.fecha,
    categoriasportafolio.name AS categoriasportafolio_name
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.categoria_id = categoriasportafolio.id;

-- verificando la vista
SELECT * FROM piezasportafolio_con_categoriasportafolio;

+------------+------------+---------------------------+
| title      | fecha      | categoriasportafolio_name |
+------------+------------+---------------------------+
| Proyecto 1 | 2023-01-15 | Fotografia                |
| Proyecto 2 | 2023-02-20 | Diseno Grafico            |
| Proyecto 1 | 2023-01-15 | Fotografia                |
| Proyecto 2 | 2023-02-20 | Diseno Grafico            |
| Proyecto 3 | 2023-03-10 | Desarrollo Web            |
+------------+------------+---------------------------+
5 rows in set (0,01 sec)



-- 5) CREATE USER WITH PERMISSIONS
CREATE USER IF NOT EXISTS 'exam_user'@'localhost' IDENTIFIED BY 'Oscar12345!';
GRANT SELECT, INSERT, UPDATE, DELETE ON portafolioexamen.* TO 'exam_user'@'localhost';

-- mostrando resultado

mysql> CREATE USER IF NOT EXISTS 'exam_user'@'localhost' IDENTIFIED BY 'Oscar12345!'
    -> ;
Query OK, 0 rows affected (0,02 sec)

mysql> GRANT SELECT, INSERT, UPDATE, DELETE ON portafolioexamen.* TO 'exam_user'@'localhost';

FLUSH PRIVILEGES; 


-- Read only certain columns:
select title, fecha from piezasportafolio;
+------------+------------+
| title      | fecha      |
+------------+------------+
| Proyecto 1 | 2023-01-15 |
| Proyecto 2 | 2023-02-20 |
| Proyecto 1 | 2023-01-15 |
| Proyecto 2 | 2023-02-20 |
| Proyecto 3 | 2023-03-10 |
+------------+------------+


-- Read with conditions:
select * from piezasportafolio where autor_id = 2;
+----+------------+----------------------------+------------+----------+--------------+
| id | title      | descripcion                | fecha      | autor_id | categoria_id |
+----+------------+----------------------------+------------+----------+--------------+
|  2 | Proyecto 2 | Descripcion del proyecto 2 | 2023-02-20 |        2 |            2 |
|  4 | Proyecto 2 | Descripcion del proyecto 2 | 2023-02-20 |        2 |            2 |
+----+------------+----------------------------+------------+----------+--------------+

-- Update data:
UPDATE piezasportafolio SET title = 'Proyecto 1 Actualizado' WHERE id = 1;

-- Delete data:

delete from piezasportafolio where id = 1;

-- ultima verificacion de tablas y estructura

mysql> show tables;
+-------------------------------------------+
| Tables_in_portafolioexamen                |
+-------------------------------------------+
| categoriasportafolio                      |
| piezasportafolio                          |
| piezasportafolio_con_categoriasportafolio |
+-------------------------------------------+
3 rows in set (0,00 sec)

mysql> describe categoriasportafolio;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
2 rows in set (0,01 sec)

mysql> select * from categoriasportafolio;
+----+----------------+
| id | name           |
+----+----------------+
|  1 | Fotografia     |
|  2 | Diseno Grafico |
|  3 | Desarrollo Web |
+----+----------------+
3 rows in set (0,00 sec)

mysql> describe piezasportafolio;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | NULL    | auto_increment |
| title        | varchar(150) | NO   |     | NULL    |                |
| descripcion  | text         | YES  |     | NULL    |                |
| fecha        | varchar(50)  | YES  |     | NULL    |                |
| autor_id     | int          | NO   | MUL | NULL    |                |
| categoria_id | int          | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
6 rows in set (0,00 sec)

mysql> select * from piezasportafolio;
+----+------------+----------------------------+------------+----------+--------------+
| id | title      | descripcion                | fecha      | autor_id | categoria_id |
+----+------------+----------------------------+------------+----------+--------------+
|  2 | Proyecto 2 | Descripcion del proyecto 2 | 2023-02-20 |        2 |            2 |
|  3 | Proyecto 1 | Descripcion del proyecto 1 | 2023-01-15 |        1 |            1 |
|  4 | Proyecto 2 | Descripcion del proyecto 2 | 2023-02-20 |        2 |            2 |
|  5 | Proyecto 3 | Descripcion del proyecto 3 | 2023-03-10 |        3 |            3 |
+----+------------+----------------------------+------------+----------+--------------+
4 rows in set (0,00 sec)


mysql> describe piezasportafolio_con_categoriasportafolio;
+---------------------------+--------------+------+-----+---------+-------+
| Field                     | Type         | Null | Key | Default | Extra |
+---------------------------+--------------+------+-----+---------+-------+
| title                     | varchar(150) | NO   |     | NULL    |       |
| fecha                     | varchar(50)  | YES  |     | NULL    |       |
| categoriasportafolio_name | varchar(100) | YES  |     | NULL    |       |
+---------------------------+--------------+------+-----+---------+-------+
3 rows in set (0,00 sec)

mysql> select * from piezasportafolio_con_categoriasportafolio;
+------------+------------+---------------------------+
| title      | fecha      | categoriasportafolio_name |
+------------+------------+---------------------------+
| Proyecto 2 | 2023-02-20 | Diseno Grafico            |
| Proyecto 1 | 2023-01-15 | Fotografia                |
| Proyecto 2 | 2023-02-20 | Diseno Grafico            |
| Proyecto 3 | 2023-03-10 | Desarrollo Web            |
+------------+------------+---------------------------+
4 rows in set (0,01 sec)


"""
La base de datos cumple su propósito: conecta todas las tablas correctamente y evita errores en los datos almacenados.
Gracias a su estructura, los registros se mantienen coherentes y el acceso a la información es más rápido y seguro.
Además, el diseño demuestra cómo una base de datos relacional puede organizar la información real de forma clara y estructurada, aplicando reglas que garantizan la integridad de los datos.
En resumen, portafolioexamen es un ejemplo sencillo pero completo de cómo se puede aplicar SQL para crear un sistema fiable, ordenado y fácil de mantener.
"""