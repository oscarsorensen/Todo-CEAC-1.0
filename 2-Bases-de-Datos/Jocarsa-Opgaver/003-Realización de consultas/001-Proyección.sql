-- En esta actividad utilizo la proyección, la selección y la ordenación para controlar la salida de las consultas. Estas tres operaciones me permiten extraer solo la información necesaria de una tabla y presentarla de forma clara. La proyección se usa para elegir columnas específicas en lugar de mostrar todos los datos. La selección define qué campos aparecen en el resultado, y la ordenación organiza las filas según uno o varios valores de las columnas. Estos conceptos se aplican en todas las operaciones básicas con bases de datos, como listas de usuarios, informes y filtrado de datos en aplicaciones reales.

-- La proyección se realiza con la cláusula SELECT, indicando únicamente los nombres de las columnas necesarias. Por ejemplo, escribir SELECT nombre, apellidos limita la salida a dos atributos. El renombrado de columnas se hace con la palabra AS para asignar un nombre más descriptivo al resultado. La ordenación se implementa con la cláusula ORDER BY, seguida de la columna utilizada para ordenar y de la dirección de ordenación. ASC indica orden ascendente y DESC indica orden descendente. La proyección y la ordenación se pueden combinar en la misma consulta, mostrando solo las columnas seleccionadas mientras se ordenan las filas por otro atributo. Estas operaciones forman parte de la sintaxis estándar de SQL y se usan para mejorar la legibilidad del resultado.


-- Acceder a MySQL como usuario root
sudo mysql -u root;
-- Crear una nueva base de datos llamada RandomDatabase
create database RandomDatabase;
-- Seleccionar la base de datos RandomDatabase para usarla
use RandomDatabase;
-- Crear una tabla llamada usuarios con los campos id, nombre, apellidos y edad
create table usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    edad INT NOT NULL

);
-- Insertar 20 registros (de la clase) en la tabla usuarios
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Juan", "Perez", 30);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Ana", "Gomez", 25);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Luis", "Martinez", 28);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Maria", "Lopez", 32);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Carlos", "Sanchez", 41);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Lucia", "Torres", 22);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Pedro", "Ramirez", 35);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Sofia", "Diaz", 29);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Miguel", "Vargas", 27);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Elena", "Castro", 31);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Javier", "Navarro", 33);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Paula", "Rios", 24);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Diego", "Herrera", 26);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Laura", "Cortes", 34);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Andres", "Molina", 30);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Natalia", "Ortega", 23);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Hugo", "Reyes", 36);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Clara", "Morales", 28);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Adrian", "Vega", 39);
INSERT INTO usuarios (nombre, apellidos, edad) VALUES ("Irene", "Campos", 21);

-- Verificar que los registros se han insertado correctamente
select * from usuarios;
-- verificar que los registros se han insertado correctamente (otra vez)
select nombre, apellidos, edad from usuarios;

-- Realizar una consulta para mostrar los nombres, apellidos y edades de todos los usuarios
select nombre as 
    'Nombre del cliente',
    apellidos as 'Apellidos del cliente',
    edad as 'Edad del cliente'
from usuarios;

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Juan               | Perez                 |               30 |
| Ana                | Gomez                 |               25 |
| Luis               | Martinez              |               28 |
| Maria              | Lopez                 |               32 |
| Carlos             | Sanchez               |               41 |
| Lucia              | Torres                |               22 |
| Pedro              | Ramirez               |               35 |
| Sofia              | Diaz                  |               29 |
| Miguel             | Vargas                |               27 |
| Elena              | Castro                |               31 |
| Javier             | Navarro               |               33 |
| Paula              | Rios                  |               24 |
| Diego              | Herrera               |               26 |
| Laura              | Cortes                |               34 |
| Andres             | Molina                |               30 |
| Natalia            | Ortega                |               23 |
| Hugo               | Reyes                 |               36 |
| Clara              | Morales               |               28 |
| Adrian             | Vega                  |               39 |
| Irene              | Campos                |               21 |
+--------------------+-----------------------+------------------+

-- Realizar una consulta para mostrar todos los datos de los usuarios ordenados por edad descendente
SELECT
    *
FROM
    usuarios
ORDER BY
    edad DESC;

+----+---------+-----------+------+
| id | nombre  | apellidos | edad |
+----+---------+-----------+------+
|  5 | Carlos  | Sanchez   |   41 |
| 19 | Adrian  | Vega      |   39 |
| 17 | Hugo    | Reyes     |   36 |
|  7 | Pedro   | Ramirez   |   35 |
| 14 | Laura   | Cortes    |   34 |
| 11 | Javier  | Navarro   |   33 |
|  4 | Maria   | Lopez     |   32 |
| 10 | Elena   | Castro    |   31 |
|  1 | Juan    | Perez     |   30 |
| 15 | Andres  | Molina    |   30 |
|  8 | Sofia   | Diaz      |   29 |
|  3 | Luis    | Martinez  |   28 |
| 18 | Clara   | Morales   |   28 |
|  9 | Miguel  | Vargas    |   27 |
| 13 | Diego   | Herrera   |   26 |
|  2 | Ana     | Gomez     |   25 |
| 12 | Paula   | Rios      |   24 |
| 16 | Natalia | Ortega    |   23 |
|  6 | Lucia   | Torres    |   22 |
| 20 | Irene   | Campos    |   21 |
+----+---------+-----------+------+

-- Realizar una consulta para mostrar solo los nombres y apellidos de los usuarios
SELECT
    nombre,
    apellidos
FROM
    usuarios;
+---------+-----------+
| nombre  | apellidos |
+---------+-----------+
| Juan    | Perez     |
| Ana     | Gomez     |
| Luis    | Martinez  |
| Maria   | Lopez     |
| Carlos  | Sanchez   |
| Lucia   | Torres    |
| Pedro   | Ramirez   |
| Sofia   | Diaz      |
| Miguel  | Vargas    |
| Elena   | Castro    |
| Javier  | Navarro   |
| Paula   | Rios      |
| Diego   | Herrera   |
| Laura   | Cortes    |
| Andres  | Molina    |
| Natalia | Ortega    |
| Hugo    | Reyes     |
| Clara   | Morales   |
| Adrian  | Vega      |
| Irene   | Campos    |
+---------+-----------+

-- Realizar una consulta para mostrar solo los nombres y apellidos de los usuarios ordenados por apellidos ascendente
SELECT
    nombre,
    apellidos
FROM
    usuarios
ORDER BY
    apellidos ASC;

+---------+-----------+
| nombre  | apellidos |
+---------+-----------+
| Irene   | Campos    |
| Elena   | Castro    |
| Laura   | Cortes    |
| Sofia   | Diaz      |
| Ana     | Gomez     |
| Diego   | Herrera   |
| Maria   | Lopez     |
| Luis    | Martinez  |
| Andres  | Molina    |
| Clara   | Morales   |
| Javier  | Navarro   |
| Natalia | Ortega    |
| Juan    | Perez     |
| Pedro   | Ramirez   |
| Hugo    | Reyes     |
| Paula   | Rios      |
| Carlos  | Sanchez   |
| Lucia   | Torres    |
| Miguel  | Vargas    |
| Adrian  | Vega      |
+---------+-----------+

SELECT
    nombre,
    apellidos 
    --, edad. La edad la he quitado para ver solo los nombres y apellidos. la tarea no especifica que se muestre la edad.
FROM
    usuarios
ORDER BY
    edad DESC;

+---------+-----------+
| nombre  | apellidos |
+---------+-----------+
| Carlos  | Sanchez   |
| Adrian  | Vega      |
| Hugo    | Reyes     |
| Pedro   | Ramirez   |
| Laura   | Cortes    |
| Javier  | Navarro   |
| Maria   | Lopez     |
| Elena   | Castro    |
| Juan    | Perez     |
| Andres  | Molina    |
| Sofia   | Diaz      |
| Luis    | Martinez  |
| Clara   | Morales   |
| Miguel  | Vargas    |
| Diego   | Herrera   |
| Ana     | Gomez     |
| Paula   | Rios      |
| Natalia | Ortega    |
| Lucia   | Torres    |
| Irene   | Campos    |
+---------+-----------+

-- La proyección, la selección y la ordenación son operaciones fundamentales de SQL para controlar cómo se obtiene y se presenta la información. Estas funciones ayudan a organizar la salida en columnas relevantes y a ordenar las filas según un criterio específico. Estos conceptos se relacionan directamente con todo lo que he aprendido antes, como el uso de WHERE para filtrar los datos y la combinación de tablas con JOIN para obtener resultados más completos.