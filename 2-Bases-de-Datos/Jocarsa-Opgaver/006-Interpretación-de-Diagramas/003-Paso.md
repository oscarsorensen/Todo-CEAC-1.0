
En este ejercicio trabajo con bases de datos en SQL utilizando la idea de que diferentes entidades pueden compartir información común. Se trata de un ejercicio lógico, ya que lo hemos trabajado en clase. Creo una tabla general para Persona, ya que tanto los alumnos como los profesores son personas, y luego creo tablas específicas para Alumno y Profesor que amplían esta información. El objetivo es comprender cómo funcionan la herencia y las relaciones en el diseño de bases de datos.

 Primero, creo la tabla Persona con los atributos id, nombre y apellidos. Luego creo la tabla Alumno con su propio atributo NIA y una clave externa que apunta a Persona(id). Después de eso, creo la tabla Profesor con el atributo asignaturas y también la conecto a Persona(id) con una clave externa. Por último, inserto algunos datos de ejemplo que se proporcionan en las tareas y realizo consultas JOIN para comprobar que la información de Persona está correctamente relacionada con Alumno y Profesor.

# ---------- Paso 1 ----------
Persona
id
nombre
apellidos
--
Alumno (Persona)
NIA
--
Profesor (Persona)
asignaturas

# ---------- Paso 2 ----------

CREATE TABLE Persona (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(50)
);

CREATE TABLE Alumno (
    id INT PRIMARY KEY,
    NIA VARCHAR(10),
    FOREIGN KEY (id) REFERENCES Persona(id)
);

CREATE TABLE Profesor (
    id INT PRIMARY KEY,
    asignaturas TEXT,
    FOREIGN KEY (id) REFERENCES Persona(id)
);
# ---------- Paso 3 ----------

INSERT INTO Persona (id, nombre, apellidos) VALUES (1, 'Juan', 'Pérez');

INSERT INTO Alumno (id, NIA) VALUES (1, 'A123456789');

INSERT INTO Profesor (id, asignaturas) VALUES (1, 'Matemáticas, Física');

# ---------- Paso 4 ----------

SELECT Persona.*, Alumno.NIA FROM Persona JOIN Alumno ON Persona.id = Alumno.id;

SELECT Persona.*, Profesor.asignaturas FROM Persona JOIN Profesor ON Persona.id = Profesor.id;

Después de este ejercicio, entiendo mejor cómo las bases de datos relacionales pueden reutilizar la información utilizando una entidad base y entidades especializadas. Practiqué la creación de tablas, trabajé con claves externas, inserté datos y realicé consultas JOIN para recuperar la información. Puedo ver fácilmente cómo esto es muy útil para los sistemas reales, ya que muchas aplicaciones necesitan representar datos y funciones específicas con datos específicos de forma organizada.