En este ejercicio, actúo como cliente de una empresa llamada Empresadam, que ha decidido implementar un sistema de gestión de clientes utilizando bases de datos relacionales.
 El objetivo del ejercicio es crear una tabla que permita almacenar los datos personales de los clientes de forma estructurada y organizada.
 
 
Para resolver este ejercicio, empiezo creando una base de datos llamada Empresadam.
Dentro de ella, creo una tabla llamada clientes con los siguientes campos y restricciones:
dni ->tipo VARCHAR(9), clave primaria que identifica de forma única a cada cliente.



nombre -> tipo VARCHAR(50), campo obligatorio para los nombres. 
apellidos -> tipo VARCHAR(255), campo obligatorio para los apellidos. 
email -> tipo VARCHAR(100), campo obligatorio y único para evitar duplicados. 

Cada campo se ha definido con su tipo de dato correspondiente y las restricciones necesarias para mantener la integridad de los datos.
Luego utilizo la siguiente sentencia SQL para insertar los datos proporcionados en la tarea: 
INSERT INTO clientes (dni, nombre, apellidos, email) VALUES ('12345678A', 'Jose Vicente', 'Carratala Sanchis', 'info@jocarsa.com'); 
Finalmente, utilizo una sentencia SELECT para mostrar todos los datos almacenados: -- Consultar todos los registros de la tabla clientes SELECT * FROM clientes; -- Mostrar todos los registros de la tabla clientes



sudo mysql -u root -p -- Acceso a MySQL como usuario root

CREATE DATABASE Empresadam; -- Crear la base de datos Empresadam

USE Empresadam; -- Seleccionar la base de datos Empresadam

CREATE TABLE clientes ( -- Crear la tabla clientes
    dni VARCHAR(9) PRIMARY KEY, -- define dni como clave primaria
    nombre VARCHAR(50) NOT NULL, -- define nombre como un campo obligatorio
    apellidos VARCHAR(255) NOT NULL, -- define apellidos como un campo obligatorio
    email VARCHAR(100) UNIQUE NOT NULL -- define email como un campo único y obligatorio

);

-- Insertar registro en la tabla clientes

INSERT INTO clientes (dni, nombre, apellidos, email) values ('12345678A', 'Jose Vicente', 'Carratala Sanchis', 'info@jocarsa.com');

-- Consultar todos los registros de la tabla clientes
SELECT * FROM clientes; -- Mostrar todos los registros de la tabla clientes


A través de este ejercicio, utilizo SQL para crear y gestionar tablas dentro de una base de datos.
La creación de la base de datos Empresadam y la tabla de clientes muestra el uso de los comandos CREATE, INSERT y SELECT, que forman parte de las operaciones CRUD básicas.
Este ejercicio muestra los conocimientos adquiridos sobre el modelado de datos y la organización estructurada de la información, que son fundamentales en el desarrollo de aplicaciones que utilizan bases de datos.