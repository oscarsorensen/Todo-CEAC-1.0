--En este ejercicio, trabajo con una base de datos MySQL y Flask para practicar cómo crear una base de datos, gestionar usuarios y acceder a datos a través de puntos finales web. El objetivo es comprender cómo una aplicación Python puede conectarse a una base de datos y mostrar información en formato JSON utilizando Flask. Como esto se hizo en clase, aquí lo analizo más en profundidad para comprenderlo mejor.
-- Primero, creo una base de datos MySQL llamada tiendaclase y hago dos tablas: clientes y productos, usando los tipos de datos y claves primarias adecuados. Luego, creo un usuario MySQL con permisos para acceder a esta base de datos. Después de eso, uso el mysql.connector en Python para establecer una conexión con la base de datos. Con Flask, defino puntos finales que ejecutan consultas SQL y devuelven los resultados como JSON, lo que permite acceder a los datos desde un navegador.

-- 1        Creación de la base de datos y tablas:  #########
-- La base de datos para una tienda de clase con tablas de clientes y productos.
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba: clientes
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');

-- Datos de prueba: productos
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);


-- 2        Conexión a la base de datos desde Flask:  #########
-- http://127.0.0.1:5000/clientes
-- Resultado en en web: [[1, "Ana L\u00f3pez", "ana@example.com", "600123456", null], [2, "Carlos Ruiz", "carlos@example.com", "611987654", null], [3, "Mar\u00eda G\u00f3mez", "maria@example.com", "622111222", null]]

-- http://127.0.0.1:5000/tablas
-- : Resultado en en web ["clientes", "productos"]

--3     Listar los usuarios del servidor MySQL:  #########  

-- Usuarios en el servidor MySQL

+--------------------+-----------+
| User               | Host      |
+--------------------+-----------+
| blogphp            | localhost |
| clientes           | localhost |
| composiciones      | localhost |
| empleados          | localhost |
| exam_user          | localhost |
| futbol2526         | localhost |
| mysql.infoschema   | localhost |
| mysql.session      | localhost |
| mysql.sys          | localhost |
| periodico          | localhost |
| root               | localhost |
| tiendaclase        | localhost |
| tiendaonlinedamdaw | localhost |
| useroscar          | localhost |
| usuariomusicstore  | localhost |
+--------------------+-----------+


--4 hago login con el usuario creado tiendaclase  #########

-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER IF NOT EXISTS 'tiendaclase'@'localhost'
IDENTIFIED BY 'Tiendaclase123$';


-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'tiendaclase'@'localhost'; -- Esto permite el acceso básico sin privilegios específicos. No es necesario, pero es una buena práctica.
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'tiendaclase'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON tiendaclase.* 
TO 'tiendaclase'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;


--5 Nos conectamos a la base de datos con Flask:  #########

-- Resultado
[(1, 'Ana López', 'ana@example.com', '600123456', None), (2, 'Carlos Ruiz', 'carlos@example.com', '611987654', None), (3, 'María Gómez', 'maria@example.com', '622111222', None)]

-- 6 Crea el endpoint principal de Flask:  #########
# http://127.0.0.1:5000/clientes
-- Resultao [[1, "Ana L\u00f3pez", "ana@example.com", "600123456", null], [2, "Carlos Ruiz", "carlos@example.com", "611987654", null], [3, "Mar\u00eda G\u00f3mez", "maria@example.com", "622111222", null]]

# http://127.0.0.1:5000/tablas
-- Resultado ["clientes", "productos"]

-- 7 Añade Flask a los proyectos:
import mysql.connector 
from flask import Flask
import json

conexion = mysql.connector.connect(
  host="localhost",
  user="tiendaclase",
  password="Tiendaclase123$",
  database="tiendaclase"
)                                      
app = Flask(__name__)

@app.route("/clientes")
def inicio():
	cursor = conexion.cursor() 
	cursor.execute("SELECT * FROM clientes;")  

	filas = cursor.fetchall()
	return json.dumps(filas)

if __name__ == "__main__":
	app.run(debug=True) 
    
# http://127.0.0.1:5000/clientes
-- Funciona correctamente y muestra los clientes.

--8 Verifica los clientes en la interfaz web:
-- Funciona correctamente y muestra los clientes.

--Con este ejercicio, practiqué cómo crear una base de datos, gestionar los permisos de los usuarios y conectar MySQL con Flask. También practiqué la creación de puntos finales que devuelven datos de la base de datos en formato JSON, lo cual es un concepto básico pero importante para crear aplicaciones web que funcionen con bases de datos.