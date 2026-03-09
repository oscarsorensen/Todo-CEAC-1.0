-- En este ejercicio, trabajo con la base de datos MySQL que creé en clase y Flask para practicar el uso de plantillas. El objetivo es recuperar datos de diferentes tablas utilizando consultas SQL y mostrar los resultados en una página web. Este ejemplo simula un pequeño sistema con estudiantes, asignaturas y matrículas, y ayuda a comprender cómo fluyen los datos desde la base de datos hasta la interfaz de usuario.
-- Primero, creo una base de datos llamada composiciones con las tablas alumnos, profesores, asignaturas y matriculas. A continuación, creo consultas SQL utilizando LEFT JOIN para combinar información de diferentes tablas. También creo una vista llamada matriculas_join para almacenar el resultado de la consulta combinada, lo que facilita la reutilización de los datos desde Flask.

-- 1 -- Crear la base de datos y las tablas necesarias
CREATE DATABASE composiciones;

USE composiciones;

CREATE TABLE alumnos(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE profesores(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE asignaturas(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  id_profesor INT
);

CREATE TABLE matriculas(
	Identificador INT PRIMARY KEY,
  id_asignatura INT,
  id_alumno INT
);

INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1,'Ana','García López'),
(2,'Luis','Martínez Pérez'),
(3,'María','Sánchez Ruiz'),
(4,'Javier','Fernández Gómez'),
(5,'Laura','Díaz Ortega'),
(6,'Carlos','Romero Torres'),
(7,'Elena','Navarro Martínez'),
(8,'Pablo','Hernández Soto'),
(9,'Sofía','Iglesias Navarro'),
(10,'Miguel','Castro León'),
(11,'Clara','Vidal Serrano'),
(12,'Diego','Morales Rivas'),
(13,'Lucía','Cano Torres'),
(14,'Adrián','Herrero Gil'),
(15,'Nuria','Requena Soler');

INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(1,'Juan','López García'),
(2,'Isabel','Martín Torres'),
(3,'Pedro','Hernández Rojas'),
(4,'Raquel','Santos Pérez'),
(5,'Alberto','Gómez Ortiz'),
(6,'Carmen','Fuentes Beltrán'),
(7,'Roberto','Pascual Torres');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1,'Matemáticas',1),
(2,'Lengua Española',2),
(3,'Historia',3),
(4,'Geografía',4),
(5,'Física',5),
(6,'Química',6),
(7,'Biología',7),
(8,'Inglés',2),
(9,'Tecnología',5),
(10,'Educación Física',3),
(11,'Música',4),
(12,'Arte',1);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1,1,1),
(2,1,2),
(3,1,3),
(4,2,1),
(5,2,4),
(6,2,5),
(7,3,6),
(8,3,7),
(9,3,8),
(10,4,9),
(11,4,10),
(12,5,11),
(13,5,12),
(14,6,13),
(15,6,14),
(16,7,15),
(17,7,3),
(18,8,4),
(19,8,5),
(20,9,6),
(21,10,7),
(22,11,8),
(23,12,9),
(24,12,10),
(25,9,11),
(26,5,12),
(27,4,13),
(28,3,14),
(29,2,15),
(30,1,4);

-- 2 -- Realizar consultas para obtener información específica (005)
-- Consulta para obtener todas las matrículas junto con la información del alumno y la asignatura

SELECT 
*
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;

-- Crear una vista para la consulta anterior (009)
 
SELECT * FROM matriculas_join; -- Esto fue en el 009. Yo mismo hice la vista, ya que faltaba.

-- Creando la vista
CREATE VIEW matriculas_join AS
SELECT
  matriculas.Identificador AS id_matricula,
  alumnos.nombre,
  alumnos.apellidos,
  asignaturas.nombre AS asignatura
FROM matriculas
LEFT JOIN alumnos
  ON matriculas.id_alumno = alumnos.Identificador
LEFT JOIN asignaturas
  ON matriculas.id_asignatura = asignaturas.Identificador;

-- 3 -- Parte Python - Este código se encuentra en 014 y 011
-- ambos funciona con la misma base de datos y tablas creadas anteriormente. Muestra correctamente los datos en una página web.
import mysql.connector 
from flask import Flask,render_template

conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones",
  password="composiciones",
  database="composiciones"
)                                      

app = Flask(__name__)
@app.route("/")
def inicio():
  cursor = conexion.cursor(dictionary=True) 
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html",datos=filas)

if __name__ == "__main__":
  app.run(debug=True)
--
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones",
  password="composiciones",
  database="composiciones"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM matriculas_join;")  

filas = cursor.fetchall()

print(filas)

-- En este ejercicio, practico cómo conectar una base de datos a una aplicación Flask y utilizar una plantilla para mostrar los resultados. También practiqué la creación de vistas SQL y el uso de consultas JOIN para combinar datos de varias tablas. Esto ayuda a organizar las consultas y facilita la visualización de datos estructurados en una página web.