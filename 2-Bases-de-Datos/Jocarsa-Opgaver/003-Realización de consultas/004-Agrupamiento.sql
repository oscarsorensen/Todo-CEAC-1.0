-- En este ejercicio, practico cómo agrupar datos almacenados en una base de datos utilizando SQL y Python. Agrupar registros me permite resumir información y comprender mejor cómo se distribuyen los datos en diferentes categorías, como categorías de productos o colores. Esta es una tarea común en aplicaciones reales donde se requiere el análisis de datos y la generación de informes.
--Primero, establezco una conexión entre Python y la base de datos MySQL llamada "clientes" utilizando las credenciales proporcionadas. Esta conexión permite a Python ejecutar consultas SQL directamente en la base de datos. Verifico que la tabla «productos» existe en la base de datos y contiene datos, por lo que se puede utilizar directamente sin necesidad de recrearla.
--A continuación, utilizo consultas SQL con GROUP BY para agrupar los productos por atributos específicos. En un caso, los productos se agrupan por categoría y, en otro, por color. La función COUNT(*) se utiliza para calcular cuántos productos pertenecen a cada grupo. Estas consultas devuelven resultados que muestran el número de productos por categoría o color.
--A continuación, los resultados de la base de datos se procesan en Python para que puedan utilizarse para la visualización.

-- SQL PART

--mysql -u root -p
USE clientes;

-- Table structure already created in a previous exercise
CREATE TABLE productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    categoria VARCHAR(100),
    precio DECIMAL(6,2)
);

INSERT INTO productos (nombre, categoria, precio) VALUES
('Teclado', 'Electrónica', 25.99),
('Ratón', 'Electrónica', 15.50),
('Camiseta', 'Ropa', 12.00),
('Pantalón', 'Ropa', 29.90),
('Silla', 'Hogar', 85.00);

SELECT * FROM productos;

+----+-----------+--------------+--------+
| id | nombre    | categoria    | precio |
+----+-----------+--------------+--------+
|  1 | Teclado   | Electrónica  |  25.99 |
|  2 | Ratón     | Electrónica  |  15.50 |
|  3 | Camiseta  | Ropa         |  12.00 |
|  4 | Pantalón  | Ropa         |  29.90 |
|  5 | Silla     | Hogar        |  85.00 |
+----+-----------+--------------+--------+

-- Python Part 

import mysql.connector 

conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT 
        categoria,
        COUNT(*) AS total
    FROM productos
    GROUP BY categoria
    ORDER BY categoria ASC;
""")

filas = cursor.fetchall()
print(filas)

-- Python part 2

import mysql.connector
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT
        categoria,
        COUNT(*) AS total
    FROM productos
    GROUP BY categoria
    ORDER BY categoria ASC;
""")

filas = cursor.fetchall()

cantidades = []
etiquetas = []

for fila in filas:
    etiquetas.append(fila[0])
    cantidades.append(fila[1])

plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%")
plt.title("Distribución de productos por categoría")
plt.show()


-- Cambiado desde Ejercicio 004

SELECT COUNT(*) 
FROM productos; 

+----------+
| COUNT(*) |
+----------+
|        5 |
+----------+

SELECT COUNT(*) AS total, categoria
FROM productos
GROUP BY categoria;
+-------+--------------+
| total | categoria    |
+-------+--------------+
|     2 | Electrónica  |
|     2 | Ropa         |
|     1 | Hogar        |
+-------+--------------+

-- Cambiado desde Ejercicio 017

-- Añadiendo la columna color e insertando datos
ALTER TABLE productos
ADD color VARCHAR(50);

UPDATE productos SET color = 'Negro' WHERE nombre = 'Teclado';
UPDATE productos SET color = 'Negro' WHERE nombre = 'Ratón';
UPDATE productos SET color = 'Rojo' WHERE nombre = 'Camiseta';
UPDATE productos SET color = 'Azul' WHERE nombre = 'Pantalón';
UPDATE productos SET color = 'Blanco' WHERE nombre = 'Silla';


import mysql.connector
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT
        color,
        COUNT(*) AS total
    FROM productos
    GROUP BY color
    ORDER BY total DESC;
""")

filas = cursor.fetchall()

cantidades = []
etiquetas = []

for fila in filas:
    etiquetas.append(fila[0])
    cantidades.append(fila[1])

print(cantidades)
print(etiquetas)

plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%")
plt.title("Conteo de productos por color")
plt.show()


-- Cambiado desde Ejercicio 014

import mysql.connector
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT
        categoria,
        COUNT(*) AS total
    FROM productos
    GROUP BY categoria
    ORDER BY total DESC;
""")

filas = cursor.fetchall()

cantidades = []
etiquetas = []

for fila in filas:
    etiquetas.append(fila[0])
    cantidades.append(fila[1])

print(cantidades)
print(etiquetas)

plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%")
plt.title("Distribución de productos por categoría")
plt.show()

--Después de completar estos ejercicios, comprendo mejor cómo funciona la agrupación de registros en una base de datos. Al utilizar SQL para agrupar y contar datos, y Python para visualizar los resultados, puedo convertir la información sin procesar de la base de datos en resúmenes claros y útiles. Estas técnicas se pueden aplicar a muchas situaciones reales, como el análisis de datos de productos o la generación de informes sencillos, y son una parte importante del trabajo con bases de datos en el desarrollo de aplicaciones.