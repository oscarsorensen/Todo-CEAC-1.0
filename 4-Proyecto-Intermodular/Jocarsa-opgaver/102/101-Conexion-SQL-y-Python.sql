--En este ejercicio, trabajo con Python y MySQL para seleccionar y ordenar datos de una base de datos. El objetivo es comprender cómo se pueden utilizar las consultas SQL en Python para mostrar información.
--Me conecto a la base de datos clientes utilizando la plantilla de conexión  y el usuario con los permisos. Utilizo un cursor de diccionario y una consulta SQL para seleccionar las columnas nombre, apellidos y edad, y ordeno los resultados por edad, de mayor a menor.

-- Conexión a la base de datos:
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  

filas = cursor.fetchall()

print(filas)

-- Verificación del usuario y permisos en MySQL:
mysql> SELECT user, host
    -> FROM mysql.user
    -> WHERE user = 'clientes';
+----------+-----------+
| user     | host      |
+----------+-----------+
| clientes | localhost |
+----------+-----------+
1 row in set (0,002 sec)
-- Verificación de permisos del usuario 'clientes'@'localhost':

mysql> SHOW GRANTS FOR 'clientes'@'localhost';
+----------------------------------------------------------------+
| Grants for clientes@localhost                                  |
+----------------------------------------------------------------+
| GRANT USAGE ON *.* TO `clientes`@`localhost`                   |
| GRANT ALL PRIVILEGES ON `clientes`.* TO `clientes`@`localhost` |
+----------------------------------------------------------------+
2 rows in set (0,000 sec)

--Proyección y ordenación:

import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
-- Uso de un cursor de diccionario para obtener resultados como diccionarios
cursor = conexion.cursor(dictionary=True)

cursor.execute("""
  SELECT
    nombre AS "Nombre del cliente",
    apellidos AS "Apellidos del cliente",
    edad AS "Edad del cliente"
  FROM clientes
  ORDER BY edad DESC;
""")

filas = cursor.fetchall()

print(filas)


--Impresión del resultado:

/opt/homebrew/var/www/4-Proyecto-Intermodular/Jocarsa-opgaver/102    main ───────────────────────────────────────── ✔  18:29:30  ─╮
╰─ /opt/homebrew/bin/python3 /opt/homebrew/var/www/4-Proyecto-Intermodular/Jocarsa-opgaver/102/test.py                                           ─╯
[{'Nombre del cliente': 'María', 'Apellidos del cliente': 'Ruiz', 'Edad del cliente': 55}, {'Nombre del cliente': 'Diego', 'Apellidos del cliente': 'Torres', 'Edad del cliente': 47}, {'Nombre del cliente': 'Carla', 'Apellidos del cliente': 'Santos', 'Edad del cliente': 41}, {'Nombre del cliente': 'Luis', 'Apellidos del cliente': 'Martínez', 'Edad del cliente': 35}, {'Nombre del cliente': 'Lucía', 'Apellidos del cliente': 'Navarro', 'Edad del cliente': 33}, {'Nombre del cliente': 'Javier', 'Apellidos del cliente': 'López', 'Edad del cliente': 29}, {'Nombre del cliente': 'Oscar', 'Apellidos del cliente': 'Sorensen', 'Edad del cliente': 28}, {'Nombre del cliente': 'Sofía', 'Apellidos del cliente': 'Morales', 'Edad del cliente': 26}, {'Nombre del cliente': 'Ana', 'Apellidos del cliente': 'García', 'Edad del cliente': 22}, {'Nombre del cliente': 'Pedro', 'Apellidos del cliente': 'Hernández', 'Edad del cliente': 18}]

--Esta práctica me ayudó a comprender cómo proyectar y clasificar datos de una base de datos utilizando Python y MySQL. Estos conceptos son útiles para trabajar con bases de datos en proyectos futuros.