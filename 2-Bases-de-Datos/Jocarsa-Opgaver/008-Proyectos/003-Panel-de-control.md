En este ejercicio creo una sencilla aplicación web que muestra noticias. Utilizo una base de datos real que yo mismo he creado. El objetivo es comprender cómo se estructura una base de datos, cómo se relacionan las tablas mediante claves externas y cómo se puede mostrar esta información en una página web. Este proyecto está directamente relacionado con lo que hemos aprendido en clase sobre bases de datos MySQL y desarrollo web con PHP. Es un escenario muy práctico de la vida real, y utilizo básicamente la misma configuración cuando realizo el proyecto en grupo para nuestros exámenes de este trimestre.

Empiezo creando la base de datos llamada «periodico» con dos tablas: autores y noticias. La tabla de autores contiene el id, el nombre, el correo electrónico único y la biografía, mientras que la tabla de noticias contiene el id, el título, el contenido, la fecha de publicación automática y una clave externa que vincula cada artículo de noticias con su autor. A continuación, inserto datos de prueba para que la aplicación tenga información que mostrar. Luego creo la página principal utilizando index.php y el archivo inc/listar_articulos.php, que se conecta a la base de datos, recupera las noticias (ordenadas por fecha, de más reciente a más antigua) y muestra el título, el contenido y el autor en la pantalla. A continuación, utilizo el diseño visual del archivo CSS proporcionado en la tarea.

# ---------- Estructura de la Base de Datos ----------

- Crear la base de datos
CREATE DATABASE periodico
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE periodico;

- Tabla de autores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,  <!-- #cambio a not null para que no haya autores sin email -->
    bio TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

- Tabla de noticias
CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor_id INT NULL,   -- ← Debe permitir NULL

    CONSTRAINT fk_noticias_autores
        FOREIGN KEY (autor_id)
        REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

- Insertar datos de ejemplo, generado
INSERT INTO autores (nombre, email, bio) VALUES
('Laura Sánchez', 'laura.sanchez@example.com', 'Periodista especializada en medio ambiente y sostenibilidad.'),
('Miguel Torres', 'miguel.torres@example.com', 'Analista de tecnología e innovación digital.'),
('Elena García', 'elena.garcia@example.com', 'Reportera de actualidad internacional con experiencia en conflictos globales.'),
('Rubén Castillo', 'ruben.castillo@example.com', 'Economista y columnista sobre mercados y empresas.');


INSERT INTO noticias (titulo, contenido, autor_id) VALUES
('España alcanza un nuevo récord en energías renovables',
 'El último informe del Ministerio de Transición Ecológica señala un crecimiento histórico en producción solar y eólica.',
 1),

('Una empresa española lanza un nuevo sistema de inteligencia artificial',
 'La compañía presenta una plataforma capaz de optimizar procesos industriales utilizando aprendizaje automático.',
 2),

('Nuevas tensiones diplomáticas entre varios países europeos',
 'Líderes europeos se reúnen para abordar las recientes discrepancias en materia de defensa y cooperación.',
 3),

('Las pequeñas empresas registran una mejora en sus cifras de ventas',
 'Un estudio económico revela que el comercio local ha experimentado una recuperación progresiva en los últimos meses.',
 4),

('Se aprueba un nuevo plan nacional de reciclaje',
 'El gobierno introduce nuevas medidas para reducir residuos y fomentar el uso responsable de materiales.',
 1);

- En una mejora futura, podría usar un JOIN entre noticias y autores para obtener nombre y email desde la tabla autores.

$sql = "
SELECT noticias.titulo,
       noticias.contenido,
       autores.nombre,
       autores.email
FROM noticias
INNER JOIN autores
ON noticias.autor_id = autores.id
ORDER BY noticias.fecha_publicacion DESC;
";



# ---------- Aplicación Web ----------
Tengo acceso a todo.

# ---------- Paso a paso ----------

- inc/listar_articulos.php
<!doctype html>
<html lang="es">
	<head>
  	<title>El jocarsa - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
  	<header>
    	<h1>El jocarsa</h1>
      <h2>Noticias tecnológicas</h2>
    </header>
    <main>
    	<?php
        // Conecta a la base de datos
        $host = "localhost";
        $user = "periodico";
        $pass = "Periodico123$";
        $db   = "periodico";
        $conexion = new mysqli($host, $user, $pass, $db);
        
        if ($conexion->connect_error) {
            die("Conexión fallida: " . $conexion->connect_error);
        }
        
        // Selecciona la base de datos
        $sql = "SELECT * FROM noticias ORDER BY fecha_publicacion DESC";
        $result = $conexion->query($sql);
        
        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<h3>" . $row["titulo"] . "</h3><br>";
                echo $row['contenido'] . "<br><br>";
                echo "Autor: <strong>" . $row["nombre"]."</strong> (<a href='mailto:$row[email]'>$row[email]</a>)<br><br>";
            }
        } else {
            echo "0 resultados";
        }
        
        // Cerrar la conexión
        $conexion->close();
    	?>
    </main>
    <footer>
    </footer>
  </body>
</html>

- css/estilo.css

/* ESTILOS GENERALES /////////////  */
body, html {
	width:100%;
	height:100%;
	margin:0px;
	padding:0px;
}
body{
	display:flex;
}
nav{
	flex:1;
	background:teal;
}
main{
	flex:4;
}
footer{
	flex:1;
	background:teal;
	color:white;
}
h1{
	font-size:24px;
	text-align:center;
	margin-bottom:20px;
}
h2{
	font-size:18px;
	text-align:center;
	margin-bottom:10px;
}

/* ESTILOS PARA LISTA DE NOTICIAS */
main{
	display:grid;
	gap: 5px;
}
.noticia {
	background-color: white;
	border-radius:50%;
	padding:20px;
	box-shadow: 0 3px 4px rgba(0, 0, 0, 0.2);
	width:300px; height:200px;
}
.noticia:hover {
-box-shadow: 0 8px 14px rgba(0, 0, 0, 0.2), 0 16px 24px rgba(0, 0, 0, 0.2)
}

/* ESTILOS PARA FOTTER */
footer{
	padding-top:20px;
}

- index.php
<!doctype html>
<html lang="es">
	<head>
  	<title>El jocarsa - Noticias tecnológicas</title>
    <!-- Mi propio proyecto se llama The Oscar, pero como las tareas requieren que se llame El Jocarsa, lo hago así. -->
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
  	<header>
    	<h1>El jocarsa</h1>
      <h2>Noticias tecnológicas</h2>
    </header>
    <main>
    	<?php include "inc/listar_articulos.php"; ?>
    </main>
    <footer>
    </footer>
  </body>
</html>

- El localhost donde lo tengo:
http://localhost:8080/2-Bases-de-Datos/008-Proyectos/003-Panel-de-control/aplicacion/

Puedo acceder a la aplicación web y ver las noticias con sus autores correctamente enlazados. Uso 8080 porque uso Apache y mac. Tengo menos conflictos así. En el localhost puedo ver la aplicación web funcionando correctamente, mostrando las noticias y los autores asociados.


Este ejercicio me ayudó a practicar cómo las aplicaciones web reales utilizan bases de datos para gestionar y mostrar información. Ahora puedo ver más claramente cómo se utilizan las relaciones entre tablas para organizar autores y noticias. Fue una tarea muy práctica, que disfruté resolviendo. Especialmente porque puedo ver cómo voy a utilizar esta configuración muchas veces en el futuro.