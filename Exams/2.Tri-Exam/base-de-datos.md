# Base de Datos - Examen Trimestral, 2

- Este trabajo está escrito originalmente en inglés y posteriormente traducido al español con ChatGPT.
- Oscar Sorensen, DAW, 14/1/2026

---

## 1.-Introducción breve y contextualización

Este examen de base de datos forma parte de un examen más amplio, que incluye las asignaturas: Base de Datos, Lenguajes de Marcas, Programación y Proyecto Intermodular. El proyecto consiste en una base de datos como base principal y, posteriormente, PHP, HTML y CSS en las otras asignaturas. Es el primer proyecto que hemos realizado desarrollado como un proyecto de grupo real. La base de datos debe almacenar toda la información de nuestro sitio web “Chamitos Movie Club”. Aquí hablamos de usuarios, películas, reseñas y toda la información relacionada. La base de datos es utilizada tanto por el frontend como por el backend del proyecto.

---

## 2.-Desarrollo detallado y preciso

Cuando empezamos a pensar qué tipo de datos debía almacenar la base de datos, hicimos una lista larga en papel e intentamos conectar las diferentes partes para que todo pareciera lógico y tuviera un flujo profesional. Sin embargo, durante el desarrollo de la aplicación nos dimos cuenta de que necesitábamos cosas en las que no habíamos pensado y que también era necesario ampliar otras que ya teníamos. Al final, terminamos con la siguiente estructura para todo el proyecto:

```
├── back
│   ├── css
│   │   └── estilo.css
│   ├── escritorio.php
│   ├── inc
│   │   ├── create
│   │   │   ├── formulario.php
│   │   │   └── procesaformulario.php
│   │   ├── db.php
│   │   ├── delete
│   │   │   └── eliminar.php
│   │   ├── read
│   │   │   └── leer.php
│   │   └── update
│   │       ├── formularioactualizar.php
│   │       └── procesaformulario.php
│   ├── index.php
│   └── sql
│       └── bdd.md
├── front
│   ├── css
│   │   ├── Register.css
│   │   ├── estilo.css
│   │   ├── login.css
│   │   ├── movie.css
│   │   └── profile.css
│   ├── img
│   │   ├── login
│   │   │   └── fondo.png
│   │   ├── peliculas
│   │   │   └── (aprox. 20 imágenes jpg, omitidas por simplicidad)
│   │   ├── registro
│   │   │   └── background.png
│   │   └── usuarios
│   │       └── file.gitkeep
│   ├── inc
│   │   ├── detalle_pelicula.php
│   │   └── listar_articulos.php
│   ├── index.php
│   ├── info.md
│   ├── login.php
│   ├── logout.php
│   ├── movie.php
│   ├── procesar_puntuacion.php
│   ├── profile.php
│   └── register.php
└── screenshots
        └── (capturas de las distintas fases del desarrollo)
```

Sin embargo, empezamos con algo más simple y luego avanzamos paso a paso. A continuación se muestra la parte del backend.

Primero creamos la base de datos y accedimos a ella:

```
CREATE DATABASE IF NOT EXISTS proyecto_peliculas;
USE proyecto_peliculas;
```

Después creamos un usuario para la base de datos. La razón de esto es que es una buena práctica de cara al futuro. Técnicamente podríamos haber usado el usuario root, ya que se trata de un proyecto escolar y la base de datos está alojada en local, pero decidimos no hacerlo por principio. Si hubiéramos usado el usuario root y algo hubiera salido mal, podría haber afectado a nuestras otras bases de datos, lo cual habría sido desafortunado.

```
CREATE USER 'peliculas_app'@'localhost'
IDENTIFIED BY 'Peliculas123$';
```

Decidimos otorgarle todos los privilegios con GRANT ALL PRIVILEGES, ya que era más sencillo que especificar exactamente qué permisos necesitaba, puesto que todavía no lo sabíamos con certeza.

```
GRANT ALL PRIVILEGES
ON proyecto_peliculas.*
TO 'peliculas_app'@'localhost';
FLUSH PRIVILEGES;
```

A continuación creamos nuestras primeras tablas. Creamos todas las tablas que pensamos que podrían ser útiles desde el principio, aunque finalmente no usamos todas. Nos aseguramos de que estuvieran conectadas mediante claves foráneas para poder agrupar los datos correctamente. También utilizamos INT para los identificadores, TEXT para descripciones de texto y DATE o DATETIME cuando trabajábamos con fechas. El objetivo de estos requisitos es evitar datos incorrectos en la base de datos.

```
-- Tabla: usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: categorias
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(100)
);

-- Tabla: peliculas
CREATE TABLE peliculas (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200),
    director VARCHAR(150),
    duracion_min INT,
    restriccion_edad INT,
    fecha_estreno DATE,
    descripcion TEXT,
    imagen VARCHAR(255),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Tabla: resenas
CREATE TABLE resenas (
    id_resena INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_pelicula INT,
    comentario TEXT,
    fecha_resena DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (id_usuario, id_pelicula),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);

-- Tabla: puntajes
CREATE TABLE puntajes (
    id_puntaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_pelicula INT,
    puntaje_1_5 INT CHECK (puntaje_1_5 BETWEEN 1 AND 5),
    UNIQUE (id_usuario, id_pelicula),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);

-- Tabla: listas (watchlists)
CREATE TABLE listas (
    id_lista INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    nombre VARCHAR(100),
    fecha_agregado DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Tabla: listas_peliculas (relación N:M)
CREATE TABLE listas_peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_lista INT,
    id_pelicula INT,
    FOREIGN KEY (id_lista) REFERENCES listas(id_lista),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);
```

También creamos tres vistas desde el inicio. Estaban pensadas para distintos usos, como calcular la puntuación media de una película, relacionar películas con categorías y puntuaciones, y mostrar las listas de seguimiento de cada usuario. Funcionaban correctamente, pero finalmente no las utilizamos en el proyecto final.

```
-- 1) Vista: promedio de puntuación por película
CREATE VIEW vista_promedio_puntaje AS
SELECT 
    p.id_pelicula,
    p.nombre AS pelicula,
    ROUND(AVG(pt.puntaje_1_5), 2) AS promedio_puntaje,
    COUNT(pt.id_puntaje) AS total_votos
FROM peliculas p
LEFT JOIN puntajes pt ON p.id_pelicula = pt.id_pelicula
GROUP BY p.id_pelicula, p.nombre;

-- 2) Vista: películas con categoría y puntuación media
CREATE VIEW vista_peliculas_con_categoria_y_puntaje AS
SELECT
    p.id_pelicula,
    p.nombre AS pelicula,
    c.nombre_categoria,
    ROUND(AVG(pt.puntaje_1_5), 2) AS promedio_puntaje
FROM peliculas p
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
LEFT JOIN puntajes pt ON p.id_pelicula = pt.id_pelicula
GROUP BY p.id_pelicula, p.nombre, c.nombre_categoria;

-- 3) Vista: watchlist lista para mostrar
CREATE VIEW vista_watchlist AS
SELECT
    u.id_usuario,
    u.username,
    l.id_lista,
    l.nombre AS nombre_lista,
    p.id_pelicula,
    p.nombre AS pelicula,
    p.imagen
FROM listas l
JOIN usuarios u ON l.id_usuario = u.id_usuario
JOIN listas_peliculas lp ON l.id_lista = lp.id_lista
JOIN peliculas p ON lp.id_pelicula = p.id_pelicula;
```

A continuación insertamos datos de prueba.

```
-- CATEGORÍAS (15)
INSERT INTO categorias (nombre_categoria) VALUES
('Acción'),
('Drama'),
('Ciencia ficción'),
('Comedia'),
('Thriller'),
('Aventura'),
('Fantasía'),
('Romance'),
('Terror'),
('Animación'),
('Documental'),
('Crimen'),
('Misterio'),
('Guerra'),
('Historia');
```

Estos fueron los primeros usuarios de backend creados para pruebas.

```
-- USUARIOS (5) Usuarios de backend, administradores
INSERT INTO usuarios (nombre, apellidos, username, password) VALUES
('Oscar', 'Sorensen', 'oscaradmin', 'admin'),
('Carlos', 'Gallardo', 'CGallardo', 'Gallardo123'),
('Bryan', 'Avila', 'BAvila', 'Avila123'),
('Jose Vicente', 'Carratala', 'jocarsa', 'jocarsa123'),
('Laura', 'Martinez', 'lmartinez', 'password123');
```

También añadimos puntuaciones iniciales.

```
-- PUNTAJES
INSERT INTO puntajes (id_usuario, id_pelicula, puntaje_1_5) VALUES
(1, 1, 5),(2, 2, 4),(3, 3, 3),(4, 4, 4),(5, 5, 5),
(1, 6, 4),(2, 7, 3),(3, 8, 4),(4, 9, 2),(5,10, 3),
(1,11, 4),(2,12, 5),(3,13, 3),(4,14, 4),(5,15, 5),
(1,16, 3),(2,17, 4),(3,18, 2),(4,19, 4),(5,20, 5),
(1,21, 4),(2,22, 3),(3,23, 4),(4,24, 3),(5,25, 5);
```

Y reseñas iniciales.

```
-- RESEÑAS
INSERT INTO resenas (id_usuario, id_pelicula, comentario) VALUES
(1, 1, 'Muy buena película, entretenida.'),
(2, 2, 'Historia interesante y bien contada.'),
(3, 3, 'Correcta, aunque algo lenta.'),
(4, 4, 'Me gustó bastante.'),
(5, 5, 'Excelente, muy recomendable.'),
(1, 6, 'Buena producción.'),
(2, 7, 'Entretenida para pasar el rato.'),
(3, 8, 'No está mal.'),
(4, 9, 'Un poco floja.'),
(5,10, 'Divertida.'),
(1,11, 'Buen ritmo.'),
(2,12, 'Muy buena dirección.'),
(3,13, 'Aceptable.'),
(4,14, 'Interesante propuesta.'),
(5,15, 'Me encantó.'),
(1,16, 'Correcta.'),
(2,17, 'Buena historia.'),
(3,18, 'Podría ser mejor.'),
(4,19, 'Sólida.'),
(5,20, 'Muy recomendable.'),
(1,21, 'Entretenida.'),
(2,22, 'Normal.'),
(3,23, 'Bien hecha.'),
(4,24, 'No destaca mucho.'),
(5,25, 'Muy buena.');
```

Posteriormente modificamos la base de datos para permitir la eliminación en cascada.

```
ALTER TABLE puntajes
DROP FOREIGN KEY puntajes_ibfk_2;

ALTER TABLE puntajes
ADD CONSTRAINT puntajes_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;

ALTER TABLE resenas
DROP FOREIGN KEY resenas_ibfk_2;

ALTER TABLE resenas
ADD CONSTRAINT resenas_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;

ALTER TABLE listas_peliculas
DROP FOREIGN KEY listas_peliculas_ibfk_2;

ALTER TABLE listas_peliculas
ADD CONSTRAINT listas_peliculas_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;
```

---

## 3.-Aplicación práctica

En el frontend utilizamos la base de datos para añadir, comprobar y mostrar datos.

Usamos consultas SELECT, INSERT y JOIN para gestionar usuarios, películas y reseñas, así como claves foráneas para mantener la integridad de los datos.

También utilizamos LEFT JOIN para mostrar películas incluso cuando no tenían reseñas.

En el panel de administración utilizamos comandos SQL básicos como:

```
USE proyecto_peliculas;
SHOW DATABASES;
SHOW TABLES;
DESCRIBE peliculas;
SELECT * FROM peliculas;
```

---

## 4.-Conclusión breve

Este ha sido el proyecto más completo y complejo en el que he participado hasta ahora. Diseñar una base de datos desde cero requiere práctica y lógica antes de empezar a crearla. He aprendido qué partes se pueden definir desde el principio y cuáles es mejor dejar para más adelante.

También he aprendido que, aunque las vistas son importantes y pueden simplificar el trabajo, es posible prescindir de ellas utilizando consultas específicas tanto en el frontend como en el backend. Considero que este proyecto me será muy útil en trabajos futuros.


Exam Title: Base de Datos - Examen Trimestral, 2
- This assignment is originally written in english, and then translated into spanish with ChatGPT. See below for the original english version.
- Oscar Sorensen, DAW, 14/1/2026

## 1.-Introducción breve y contextualización
This database exam is a part of a broader exam, consisting of the subjects: Base de Datos, Lenguajes de Marcas, Programacion and Proyecto intermodular. The project consists of a database as the groundwork, and then php, html and css in the other subjects. It is the first project that we have made that is developed as a proper group project. The database is supposed to hold all data for our website "Chamitos Movie Club". Here we are talkig users, movies, reviews and all other information related. The database is used by both /Front and /Back for the project. 

## 2.-Desarrollo detallado y preciso 
When we started thinking about what kind of data the database should hold, we made a long list on paper and tried to connect the different parts, as to it appear logically and have a professional flow. But during the development of the app we realised we needed things we hadnt thought about, and needed to expand other that we had. In the end we ended up with this structure for the whole project:


├── back
│   ├── css
│   │   └── estilo.css
│   ├── escritorio.php
│   ├── inc
│   │   ├── create
│   │   │   ├── formulario.php
│   │   │   └── procesaformulario.php
│   │   ├── db.php
│   │   ├── delete
│   │   │   └── eliminar.php
│   │   ├── read
│   │   │   └── leer.php
│   │   └── update
│   │       ├── formularioactualizar.php
│   │       └── procesaformulario.php
│   ├── index.php
│   └── sql
│       └── bdd.md
├── front
│   ├── css
│   │   ├── Register.css
│   │   ├── estilo.css
│   │   ├── login.css
│   │   ├── movie.css
│   │   └── profile.css
│   ├── img
│   │   ├── login
│   │   │   └── fondo.png
│   │   ├── peliculas
│   │   │   
│   │   │   ├── Here and below you actuaoyo have roughly 20 pictures, all jpg. I have cut them out for simplictys sake. 
│   │   ├── registro
│   │   │   └── background.png
│   │   └── usuarios
│   │       └── file.gitkeep
│   ├── inc
│   │   ├── detalle_pelicula.php
│   │   └── listar_articulos.php
│   ├── index.php
│   ├── info.md
│   ├── login.php
│   ├── logout.php
│   ├── movie.php
│   ├── procesar_puntuacion.php
│   ├── profile.php
│   └── register.php
└── screenshots
        --Here you have a lot of screenshots about the different stages in development.


 However we started with the following, and then took it one step at a time. Tollowing is the back-end part.

- We started by creating the database, and entering it.
CREATE DATABASE IF NOT EXISTS proyecto_peliculas;
USE proyecto_peliculas;

- Then straight away, we created a user for the database. The reason for this, is that is is good practice for the future. We could technically have used the root user, since this is both a school project and that the database is located locally, but we decided against it out of principle. If we had used the root user and something went wrong, it could have affected our other databases- which would have been unfortunate. 

CREATE USER 'peliculas_app'@'localhost'
IDENTIFIED BY 'Peliculas123$';

- We did however decide to give the user all privileges with GRANT ALL PRIVILEGES, because it was easier than specifying what exact priviledges he should have, since we didnt know that exactly yet.
GRANT ALL PRIVILEGES
ON proyecto_peliculas.*
TO 'peliculas_app'@'localhost';
FLUSH PRIVILEGES;

- Then we came to making our first tables- we made all the tables we thought could be usefull from the start, even though we didnt end up using all of them. We make sure that they were connected by Foreign Keys, so that we could group data correctly. We also used INT for ID´s (becuase of course you cant have more than one id of the same number). And we used TEXT for text descriptions and DATE/DATETIME when we used dates. The reason for these requirements is so that we dont get wrong data in the database. And example would be having a date in a "description". It wouldnt fit and create the overall experiance confusing.

-- Tabla: usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: categorias
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(100)
);

-- Tabla: peliculas
CREATE TABLE peliculas (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200),
    director VARCHAR(150),
    duracion_min INT,
    restriccion_edad INT,
    fecha_estreno DATE,
    descripcion TEXT,
    imagen VARCHAR(255),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Tabla: resenas
CREATE TABLE resenas (
    id_resena INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_pelicula INT,
    comentario TEXT,
    fecha_resena DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (id_usuario, id_pelicula),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);

-- Tabla: puntajes
CREATE TABLE puntajes (
    id_puntaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_pelicula INT,
    puntaje_1_5 INT CHECK (puntaje_1_5 BETWEEN 1 AND 5),
    UNIQUE (id_usuario, id_pelicula),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);


-- Tabla: listas (watchlists)
CREATE TABLE listas (
    id_lista INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    nombre VARCHAR(100),
    fecha_agregado DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);


-- Tabla: listas_peliculas (relación N:M)
CREATE TABLE listas_peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_lista INT,
    id_pelicula INT,
    FOREIGN KEY (id_lista) REFERENCES listas(id_lista),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula)
);

- We also made 3 VISTAS from the get-go. They were supposed to be used for different things, like the grade of the movie, the gategory and points, and a watchlist that each user could have privately. They worked as intended, but in the final project we did not end up using these. We found out that each of them included data that we werent ready for yet, or decided not to use. In the end we took information directly from the tables, and used that. Next time i think the way is to wait with creating the vistas, untill i know exactly where and when i need it. That would be a way to avoid this problem in the future.

-- 1) Vista: promedio de puntuación por película
CREATE VIEW vista_promedio_puntaje AS
SELECT 
    p.id_pelicula,
    p.nombre AS pelicula,
    ROUND(AVG(pt.puntaje_1_5), 2) AS promedio_puntaje,
    COUNT(pt.id_puntaje) AS total_votos
FROM peliculas p
LEFT JOIN puntajes pt ON p.id_pelicula = pt.id_pelicula
GROUP BY p.id_pelicula, p.nombre;


-- 2) Vista: películas con categoría y puntuación media
CREATE VIEW vista_peliculas_con_categoria_y_puntaje AS
SELECT
    p.id_pelicula,
    p.nombre AS pelicula,
    c.nombre_categoria,
    ROUND(AVG(pt.puntaje_1_5), 2) AS promedio_puntaje
FROM peliculas p
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
LEFT JOIN puntajes pt ON p.id_pelicula = pt.id_pelicula
GROUP BY p.id_pelicula, p.nombre, c.nombre_categoria;


-- 3) Vista: watchlist lista para mostrar
CREATE VIEW vista_watchlist AS
SELECT
    u.id_usuario,
    u.username,
    l.id_lista,
    l.nombre AS nombre_lista,
    p.id_pelicula,
    p.nombre AS pelicula,
    p.imagen
FROM listas l
JOIN usuarios u ON l.id_usuario = u.id_usuario
JOIN listas_peliculas lp ON l.id_lista = lp.id_lista
JOIN peliculas p ON lp.id_pelicula = p.id_pelicula;

- Then we came to the inserting of some test data
-- CATEGORÍAS (15)
INSERT INTO categorias (nombre_categoria) VALUES
('Acción'),
('Drama'),
('Ciencia ficción'),
('Comedia'),
('Thriller'),
('Aventura'),
('Fantasía'),
('Romance'),
('Terror'),
('Animación'),
('Documental'),
('Crimen'),
('Misterio'),
('Guerra'),
('Historia');

- These were the first backend users we made. They funcioned for testing and making sure things worked as supposed, but they are not specially safe. Later in the project we tried to hash the passwords, but ran into some conversation trouble. Next time it will be easier (and safer) so hash the passwords from the start.
-- USUARIOS (5) Backengnd users, admins. Not frontend users.
INSERT INTO usuarios (nombre, apellidos, username, password) VALUES
('Oscar', 'Sorensen', 'oscaradmin', 'admin'),
('Carlos', 'Gallardo', 'CGallardo', 'Gallardo123'),
('Bryan', 'Avila', 'BAvila', 'Avila123'),
('Jose Vicente', 'Carratala', 'jocarsa', 'jocarsa123'),
('Laura', 'Martinez', 'lmartinez', 'password123');

- We also have each movie a starting score. We didnt end up using it, but the plan was that the user could give his own score, and it would be devided with the other scores, creating an avarage score for each movie.
-- PUNTAJES (1 por película)
INSERT INTO puntajes (id_usuario, id_pelicula, puntaje_1_5) VALUES
(1, 1, 5),(2, 2, 4),(3, 3, 3),(4, 4, 4),(5, 5, 5),
(1, 6, 4),(2, 7, 3),(3, 8, 4),(4, 9, 2),(5,10, 3),
(1,11, 4),(2,12, 5),(3,13, 3),(4,14, 4),(5,15, 5),
(1,16, 3),(2,17, 4),(3,18, 2),(4,19, 4),(5,20, 5),
(1,21, 4),(2,22, 3),(3,23, 4),(4,24, 3),(5,25, 5);

- We of course also made sure that each movie had some resena to start. Later in the project the frontend connected to these resenas, so that users could add one (and only one) resena pr movie. 
-- RESEÑAS (1 por película)
INSERT INTO resenas (id_usuario, id_pelicula, comentario) VALUES
(1, 1, 'Muy buena película, entretenida.'),
(2, 2, 'Historia interesante y bien contada.'),
(3, 3, 'Correcta, aunque algo lenta.'),
(4, 4, 'Me gustó bastante.'),
(5, 5, 'Excelente, muy recomendable.'),
(1, 6, 'Buena producción.'),
(2, 7, 'Entretenida para pasar el rato.'),
(3, 8, 'No está mal.'),
(4, 9, 'Un poco floja.'),
(5,10, 'Divertida.'),
(1,11, 'Buen ritmo.'),
(2,12, 'Muy buena dirección.'),
(3,13, 'Aceptable.'),
(4,14, 'Interesante propuesta.'),
(5,15, 'Me encantó.'),
(1,16, 'Correcta.'),
(2,17, 'Buena historia.'),
(3,18, 'Podría ser mejor.'),
(4,19, 'Sólida.'),
(5,20, 'Muy recomendable.'),
(1,21, 'Entretenida.'),
(2,22, 'Normal.'),
(3,23, 'Bien hecha.'),
(4,24, 'No destaca mucho.'),
(5,25, 'Muy buena.');

- Later in the project we changed the database slightly. One of the reasons were that it wasnt possible to delete a movie with a resena- which wasnt super practical, since all movies had resenas. We also changed the puntajes, but as i said earlier we didnt end up using them at all.
ALTER TABLE puntajes
DROP FOREIGN KEY puntajes_ibfk_2;

ALTER TABLE puntajes
ADD CONSTRAINT puntajes_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;

ALTER TABLE resenas
DROP FOREIGN KEY resenas_ibfk_2;

ALTER TABLE resenas
ADD CONSTRAINT resenas_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;

ALTER TABLE listas_peliculas
DROP FOREIGN KEY listas_peliculas_ibfk_2;

ALTER TABLE listas_peliculas
ADD CONSTRAINT listas_peliculas_ibfk_2
FOREIGN KEY (id_pelicula)
REFERENCES peliculas(id_pelicula)
ON DELETE CASCADE;

## 3.-Aplicación práctica
The frontend part:
- For the frontend part we used the database by either adding, checking or showing the data. 
- We used the database to verify what kind of a user that was logging in, like this;
$sql = "
SELECT id_usuario, username, password
FROM usuarios
WHERE username = '$usuario'
    AND tipo_usuario = 'frontend'
";

- We also used the database when we were making and editing movie, like this:
 "/../db.php";- we had a file with the connection to the database, for ease.

$nombre         = $_POST['nombre'];
$director       = $_POST['director'];
$fecha_estreno  = $_POST['fecha_estreno'];
$descripcion    = $_POST['descripcion'];
$id_categoria   = $_POST['id_categoria'];

$sql = "
  INSERT INTO peliculas (
    nombre,
    director,
    fecha_estreno,
    descripcion,
    id_categoria,
    imagen
  ) VALUES (
    '$nombre',
    '$director',
    '$fecha_estreno',
    '$descripcion',
    $id_categoria,
    'placeholder.jpg'
  )
";

-- Foreign Key
```
Foreign Key
$id_usuario = $_SESSION["frontend_user"]["id_usuario"];
$sql = "
INSERT INTO resenas (id_usuario, id_pelicula, comentario)
VALUES (?, ?, ?)
";
```

-- Left joins
```
Left Join
SELECT r.comentario, r.fecha_resena, u.username
FROM resenas r
JOIN usuarios u ON r.id_usuario = u.id_usuario
WHERE r.id_pelicula = ?;
```

-- Resenas
```
My resenas
SELECT r.comentario, p.nombre
FROM resenas r
JOIN peliculas p ON r.id_pelicula = p.id_pelicula
WHERE r.id_usuario = ?;
```

- Another thing we did was making sure that some of the tables, had restrictions of different types of data. Like peliculas could only have one category and one resensa or user. The users could also only give one resena per movie. We made sure of these things with foreign keys.

- We also used JOINS when it was convinient, like here where we use a left join to make sure that movies are shown even when they dont have reviews.
```
$sql = "
  SELECT 
    p.id_pelicula,
    p.nombre,
    p.director,
    p.fecha_estreno,
    c.nombre_categoria
  FROM peliculas p
  LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
  ORDER BY p.id_pelicula ASC
";
```

- We used the same kind of left join on resenas and usuarios in the movie details. This way we linked all of the resenas to the specific movie.

- When we worked in the admin panel we used the following commands, to make sure we were the right place and working with the right data:

USE chamitos_movie_club;
SHOW DATABASES;
SHOW TABLES;
DESCRIBE peliculas;
DESC resenas;
SELECT * FROM peliculas;
SELECT nombre, estreno FROM peliculas;
SELECT * FROM peliculas WHERE id_pelicula = 1;
SELECT p.nombre, c.nombre
FROM peliculas p
LEFT JOIN categorias c
ON p.id_categoria = c.id_categoria;
SELECT * FROM peliculas LIMIT 5;



## 4.-Conclusión breve

- All in all this was the most comprehensive and complicated assignment i have taken part of yet. Designing a database from scratch takes practice and a bunch of logic- before you even start making it. I learned what parts of a database can be made at once, and what parts of a database that is better to wait with- untill get you have a better view of the project. I also learned that while views are important, and can simplify your work, you can also get around using them, by useing specific quieries both in front and back end. 

- I relized how different front and back end of a program is, but also how you can mix the two. However in the future i will likely be making two seperate databases, to make sure the things are devided properly. The fix with adding a row on usuario that told wether it was a bag or front end usuario worked because it was a school project, but i wouldnt do it again. All in all it was a very good project and i walk away feeling like this is something i can use in the future work i will do.