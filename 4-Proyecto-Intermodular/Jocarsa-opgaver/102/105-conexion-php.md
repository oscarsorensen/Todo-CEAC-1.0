En este ejercicio trabajé con PHP, MySQL, SQL y HTML para crear un blog que carga artículos desde una base de datos. Esto simula una situación real en la que un sitio web necesita mostrar contenido dinámico almacenado en un servidor, algo muy común en blogs, sitios web de noticias o cualquier página profesional. Como hicimos este ejercicio en clase, fue uno de los más fáciles.

 Primero, creé la base de datos blogphp y la tabla blog, e inserté algunos artículos de ejemplo. Luego creé un usuario MySQL con permisos para esa base de datos. Después de eso, programé el archivo «le_damos_forma.php», que se conecta a MySQL usando mysqli, realiza una consulta e imprime los artículos usando HTML. Finalmente, integré esto en la página principal «blog_completo_y_bonito.php», que tiene la estructura visual del blog. Probé todo en el navegador y confirmé que todo funciona correctamente.

 ```

# ---------- Paso 1: Primero creo la base de datos ----------
CREATE DATABASE IF NOT EXISTS blogphp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE blogphp;

CREATE TABLE blog (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  fecha DATETIME NOT NULL,
  autor VARCHAR(100) NOT NULL,
  contenido TEXT NOT NULL
);

INSERT INTO blog (titulo, fecha, autor, contenido)
VALUES 
('Artículo 1', NOW(), 'Author 1', 'Contenido del artículo 1'),
('Artículo 2', NOW(), 'Author 2', 'Contenido del artículo 2');

# ---------- Paso 2: Crear usuario para la base de datos ----------
CREATE USER 
'blogphp'@'localhost' 
IDENTIFIED BY 'Blogphp123$';

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


# ---------- Paso 3: Crear el archivo le_damos_forma.php (cambiado desde le damos forma.php) ----------

<?php

$host = "localhost";
$user = "blogphp";
$pass = "Blogphp123$";
$db   = "blogphp";

$conexion = new mysqli($host, $user, $pass, $db);

if ($conexion->connect_error) {
    die("Conexión fallida: " . $conexion->connect_error);
}

$sql = "SELECT * FROM blog";

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
    echo '
        <article>
            <h3>' . htmlspecialchars($fila['titulo']) . '</h3>
            <time>' . htmlspecialchars($fila['fecha']) . '</time>
            <p>' . htmlspecialchars($fila['autor']) . '</p>
            <p>' . htmlspecialchars($fila['contenido']) . '</p>
        </article>
    ';
}

$conexion->close();
?>


# ---------- Paso 4: Crear el archivo blog completo y bonito.php ----------
<!doctype html>
<meta charset="utf-8"> <!-- Añadiendo esto para que el sitio muestre caracteres españoles -->
<html>
<head>
    <style>
        body, html {
            font-family: sans-serif;
        }
        header, main, footer {
            width: 800px;
            margin: auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Oscar Sorensen</h1>
        <h2>Blog super super super interesante</h2>
    </header>
    <main>
        <?php
            include 'le_damos_forma.php';
        ?>
    </main>
    <footer>
    </footer>
</body>
</html>


# ---------- Paso 5: Detectar y resolver errores ----------

Todo funciona según lo previsto. 
```

Este ejercicio me ayudó a practicar cómo PHP se conecta a MySQL y cómo un sitio web puede mostrar información dinámica. También practiqué cómo separar la lógica del servidor de la estructura visual, algo que se utiliza en proyectos web reales.