
prompt: 
sql to create a database called 
blogphp with table blog 
and insert several articles in spanish

CREATE DATABASE IF NOT EXISTS blogphp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE blogphp;

CREATE TABLE IF NOT EXISTS blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor VARCHAR(100) DEFAULT 'Administrador'
);

INSERT INTO blog (titulo, contenido, autor) VALUES
('Bienvenidos a mi nuevo blog',
 'Este es el primer artículo del blog. Aquí compartiré tutoriales, noticias y recursos útiles sobre programación y tecnología.',
 'José Vicente Carratalá'),

('Cómo instalar PHP y Apache en Ubuntu',
 'En este artículo aprenderás a instalar un entorno AMP en Ubuntu utilizando los repositorios oficiales y configurando los módulos necesarios.',
 'José Vicente Carratalá'),

('Introducción a SQL para principiantes',
 'SQL es un lenguaje fundamental para trabajar con bases de datos. En esta guía veremos las instrucciones básicas: SELECT, INSERT, UPDATE y DELETE.',
 'Administrador'),

('Consejos para mejorar tu productividad como programador',
 'Organizar el tiempo, dividir el trabajo en tareas pequeñas y mantener un entorno ordenado puede ayudarte a avanzar más rápidamente en tus proyectos.',
 'Administrador');

INSERT INTO blog (titulo, contenido, autor) VALUES
('This is a selvmade test article',
 'This should be the 5th article in the blog. It is written in spanish but the title is in english.',
 'Oscar Sorensen'),

 -- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'blogphp'@'localhost' 
IDENTIFIED  BY 'Blogphp123$';

GRANT USAGE ON *.* TO 'blogphp'@'localhost';

ALTER USER 'blogphp'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON blogphp.* 
TO 'blogphp'@'localhost';

FLUSH PRIVILEGES;
