
--En SQL, se pueden utilizar operadores aritméticos con valores numéricos para modificar y calcular directamente en una consulta sin cambiar los datos almacenados. Esto se utiliza principalmente para la generación de informes y el análisis de datos. En este ejercicio, trabajo con una base de datos sencilla de clientes para practicar la suma, la resta, la multiplicación y la división aplicadas al campo de edad.

--MySQL aplica operadores aritméticos dentro de la cláusula SELECT. El operador + suma un valor, – lo resta, * lo multiplica y / lo divide. Estas operaciones se calculan solo en el resultado de la consulta; la tabla en sí no se altera, lo que se puede comprobar si se revisa la tabla entre cálculos. Se utiliza un alias como «Edad ajustada» para mostrar claramente la transformación numérica realizada en cada consulta.


--mysql -u root -p
-- Primero creando la base de datos
CREATE DATABASE clientes;
USE clientes;

-- Y una tabla
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    edad INT
);



-- Ahora insertando datos
INSERT INTO clientes (nombre, apellidos, edad) VALUES
('Ana', 'García', 22),
('Luis', 'Martínez', 35),
('Carla', 'Santos', 41),
('Javier', 'López', 29),
('María', 'Ruiz', 55),
('Pedro', 'Hernández', 18),
('Lucía', 'Navarro', 33),
('Diego', 'Torres', 47),
('Sofía', 'Morales', 26),
('Oscar', 'Sorensen', 28);

-- Datos iniciales
+--------+------------+------+
| nombre | apellidos  | edad |
+--------+------------+------+
| Ana    | García     |   22 |
| Luis   | Martínez   |   35 |
| Carla  | Santos     |   41 |
| Javier | López      |   29 |
| María  | Ruiz       |   55 |
| Pedro  | Hernández  |   18 |
| Lucía  | Navarro    |   33 |
| Diego  | Torres     |   47 |
| Sofía  | Morales    |   26 |
| Oscar  | Sorensen   |   28 |
+--------+------------+------+

-- Consulta para ajustar la edad sumando 500
+--------+------------+---------------+
| nombre | apellidos  | Edad ajustada |
+--------+------------+---------------+
| Ana    | García     |           522 |
| Luis   | Martínez   |           535 |
| Carla  | Santos     |           541 |
| Javier | López      |           529 |
| María  | Ruiz       |           555 |
| Pedro  | Hernández  |           518 |
| Lucía  | Navarro    |           533 |
| Diego  | Torres     |           547 |
| Sofía  | Morales    |           526 |
| Oscar  | Sorensen   |           528 |
+--------+------------+---------------+

-- Consulta para ajustar la edad restando 500
+--------+------------+---------------+
| nombre | apellidos  | Edad ajustada |
+--------+------------+---------------+
| Ana    | García     |          -478 |
| Luis   | Martínez   |          -465 |
| Carla  | Santos     |          -459 |
| Javier | López      |          -471 |
| María  | Ruiz       |          -445 |
| Pedro  | Hernández  |          -482 |
| Lucía  | Navarro    |          -467 |
| Diego  | Torres     |          -453 |
| Sofía  | Morales    |          -474 |
| Oscar  | Sorensen   |          -472 |
+--------+------------+---------------+
-- Consulta para ajustar la edad multiplicando por 500
+--------+------------+---------------+
| nombre | apellidos  | Edad ajustada |
+--------+------------+---------------+
| Ana    | García     |         11000 |
| Luis   | Martínez   |         17500 |
| Carla  | Santos     |         20500 |
| Javier | López      |         14500 |
| María  | Ruiz       |         27500 |
| Pedro  | Hernández  |          9000 |
| Lucía  | Navarro    |         16500 |
| Diego  | Torres     |         23500 |
| Sofía  | Morales    |         13000 |
| Oscar  | Sorensen   |         14000 |
+--------+------------+---------------+

-- Consulta para ajustar la edad dividiendo por 500
+--------+------------+---------------+
| nombre | apellidos  | Edad ajustada |
+--------+------------+---------------+
| Ana    | García     |        0.0440 |
| Luis   | Martínez   |        0.0700 |
| Carla  | Santos     |        0.0820 |
| Javier | López      |        0.0580 |
| María  | Ruiz       |        0.1100 |
| Pedro  | Hernández  |        0.0360 |
| Lucía  | Navarro    |        0.0660 |
| Diego  | Torres     |        0.0940 |
| Sofía  | Morales    |        0.0520 |
| Oscar  | Sorensen   |        0.0560 |
+--------+------------+---------------+


--Los operadores aritméticos son importantes para generar resultados calculados y preparar datos para su posterior análisis. Permiten cambiar valores fácilmente sin modificar la tabla original y se conectan de forma natural con otras operaciones SQL, como la proyección, el filtrado y la clasificación.