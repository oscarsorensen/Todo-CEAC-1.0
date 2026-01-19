
Esta tarea está escrita originalmente en inglés y luego traducida al español. El texto original se encuentra debajo.

## 1.-Introducción breve y contextualización

Este examen de programación forma parte de un examen más amplio, que incluye las asignaturas: Base de Datos, Lenguajes de Marcas, Programación y Proyecto Intermodular. En este examen explicaré lo que he aprendido en programación durante los dos últimos trimestres en CEAC, así como cómo nuestro grupo hizo el proyecto que llamamos Chamitos Movie Club.

Un poco de contexto: este proyecto consiste en una base de datos como base, y después PHP, JS, HTML y CSS. Es el primer proyecto que hemos hecho que está desarrollado como un proyecto de grupo real. Elegimos hacer una mini aplicación donde puedes reseñar películas, iniciar/cerrar sesión, y donde los administradores tienen la opción de crear y eliminar películas en un panel separado.


## 2 & 3.-Desarrollo detallado y preciso + Aplicación práctica

- Al empezar este proyecto hablamos sobre qué podíamos usar como controlador. Estuvimos debatiendo bastante sobre si usar Python o PHP, y finalmente terminamos usando PHP, ya que parecía un poco más profesional para este proyecto. PHP también es lo último que hemos aprendido, lo que hizo que el proyecto fuera un poco más desafiante, y eso nos gustó.

- Elegimos estructurar el proyecto de la siguiente manera. Usamos la última configuración que nos enseñó Jose Vicente, con un front/back separado, y luego los controladores en su sitio.

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


- Se podría decir que el corazón del proyecto realmente empieza en la base de datos, a la que nos conectamos en db.php, así:

```
<?php
$conexion = new mysqli(
  "localhost",
  "peliculas_app",
  "Peliculas123$",
  "proyecto_peliculas"
);

if ($conexion->connect_error) {
  die("Database connection failed");
}
```

- Aquí tenemos una conexión PHP/SQL a la base de datos. Esto es solo una conexión, y nada más. La razón por la que hicimos esto es porque ahora en todos los demás archivos, cuando necesitamos una conexión a la base de datos, simplemente podemos enlazar a db.php. Nos pareció bastante inteligente. Recuerdo que hace solo 3 meses cuando empezamos a hacer proyectos CRUD, teníamos una conexión a la base de datos en cada archivo. Esto es mucho más inteligente.

- Usamos la conexión a la base de datos en muchos sitios, como por ejemplo aquí:

```
include __DIR__ . "/../../back/inc/db.php";

$sql = "
SELECT 
    p.id_pelicula,
    p.nombre,
    p.director,
    p.fecha_estreno,
    p.imagen,
    c.nombre_categoria,
    p.descripcion
FROM peliculas p
JOIN categorias c ON p.id_categoria = c.id_categoria
ORDER BY p.id_pelicula ASC
";
```

- Aquí se puede ver cómo, después de la conexión, seleccionamos cosas específicas de la base de datos que nos interesan. En este caso es la información que mostramos en la página principal del proyecto. Esto técnicamente podría haberse preparado como una vista, y creo que así lo haremos en el próximo proyecto. Pero para este proyecto funcionó, aunque no sea demasiado elegante.

- Ahora esta siguiente parte usa esa información y la “imprime” de una forma que podemos usar en nuestro diseño. Aquí se puede ver una mezcla de HTML y PHP. Como el HTML está integrado dentro de PHP, esto funciona muy bien junto. Esto evita código duplicado y hace que el mantenimiento sea más fácil, con un solo lugar donde actualizar las credenciales.

```
$resultado = $conexion->query($sql);

echo "<h2>Catálogo de películas</h2>";

echo "<div class='movie-grid'>";   // GRID wrapper

while ($fila = $resultado->fetch_assoc()) {
  echo "
      <article class='movie-card'>
          <a href='movie.php?id={$fila['id_pelicula']}'>
              <img src='img/peliculas/{$fila['imagen']}' alt='Poster {$fila['nombre']}'>
          </a>

          <h3>
            <a href='movie.php?id={$fila['id_pelicula']}'>
              {$fila['nombre']}
            </a>
          </h3>
          <p><strong>Director:</strong> {$fila['director']}</p>
          <p><strong>Category:</strong> {$fila['nombre_categoria']}</p>
          <p><strong>Release:</strong> {$fila['fecha_estreno']}</p>
          <p>{$fila['descripcion']}</p>
      </article>
  ";
}

echo "</div>";  
$conexion->close();
```

- Otra página que muestra PHP interesante es la página detalle_pelicula. Es la página a la que llegas si haces clic en una de las películas en la página principal. Primero, como siempre, empezamos con una conexión a la base de datos.

```
include __DIR__ . "/../../back/inc/db.php";

/* A check that the movie id exists */
if (!isset($_GET['id']) || !is_numeric($_GET['id'])) {
    echo "<p>Película no válida.</p>";
    exit;
}
```

- Pero después de eso hay una comprobación que asegura que la película realmente existe. Esto es para evitar que la gente pueda cambiar la URL a algo como ID18 y entrar en una película con ID18, aunque esa película ya no exista. En esa página también tenemos esta comprobación, que funciona con sesiones. Esta es una de las comprobaciones de la web que revisa si ya estás en una sesión o no. La razón por la que lo hicimos es porque dependiendo de la respuesta (si estás logueado o no) puedes ver botones diferentes y tener derechos diferentes, como el derecho a escribir una reseña. Solo puedes hacer esto si estás logueado.

```php
<?php if (!isset($_SESSION['frontend_user'])): ?>

  <p class="login-aviso">
    Debes iniciar sesión para escribir una reseña.
  </p>
  <a href="login.php">Ir al login</a>

<?php else: ?>
```

- En detalle_pelicula también usamos joins:

```sql
$sql = "
SELECT
    p.nombre,
    p.director,
    p.duracion_min,
    p.restriccion_edad,
    p.fecha_estreno,
    p.descripcion,
    p.imagen,
    c.nombre_categoria
FROM peliculas p
JOIN categorias c ON p.id_categoria = c.id_categoria
WHERE p.id_pelicula = $id_pelicula
";
```

```sql
$sql2 = "
SELECT r.comentario, u.nombre
FROM resenas r
JOIN usuarios u ON r.id_usuario = u.id_usuario
WHERE r.id_pelicula = $id_pelicula
";
```

- Se puede ver que el JOIN se usa para combinar datos de dos tablas usando una clave relacionada (PK -> FK), así puedo mostrar información más relacionada. Uso JOIN peliculas + categorias para obtener el nombre de la categoría (nombre_categoria) para cada película, porque la tabla de películas solo guarda id_categoria. Después uso JOIN resenas + usuarios para obtener el nombre de usuario (u.nombre) para cada reseña, porque la tabla de reseñas solo guarda id_usuario. Estaba bastante orgulloso de esta solución. Es bastante más avanzado que cualquier cosa que aprendimos en el primer trimestre, y realmente muestra cómo he progresado durante los últimos meses.

- También usamos sesiones en la parte de login de la web. Este es el PHP de login.php:

```
<?php

session_start();

include __DIR__ . "/../back/inc/db.php";

$error = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username == "" || $password == "") {
        $error = "Rellena todos los campos.";
    } else {

        $sql = "
        SELECT id_usuario, username, password, tipo_usuario
        FROM usuarios
        WHERE username = '$username'
    ";


        $resultado = $conexion->query($sql);

        if ($resultado->num_rows == 1) {

            $fila = $resultado->fetch_assoc();

            if (
                ($fila['tipo_usuario'] === 'frontend' && password_verify($password, $fila['password']))
                ||
                ($fila['tipo_usuario'] === 'backend' && $password === $fila['password'])
            ) {


                $_SESSION['frontend_user'] = $fila['username'];
                $_SESSION['frontend_user_id'] = $fila['id_usuario'];
                $_SESSION['tipo_usuario'] = $fila['tipo_usuario'];



                header("Location: profile.php");
                exit;
            } else {
                $error = "Contraseña incorrecta.";
            }
        } else {
            $error = "Usuario no existe.";
        }
    }
}
?>
```

- Esta es probablemente la parte más “complicada” de PHP en todo el proyecto. No es en sí muy complicada, pero la lógica para pensarla me llevó bastante tiempo la primera vez. Primero se puede ver que inicio la sesión con session_start() porque necesito recordar si el usuario está logueado o no. Por supuesto incluyo db.php para conectarme a la base de datos. Cuando el formulario se envía (con POST), tomo el username y la contraseña de los campos. Si uno de ellos está vacío, muestro un mensaje de error.

- Si ambos campos están rellenados, ejecuto una consulta SQL para buscar un usuario en la tabla usuarios con el mismo username. Si la consulta devuelve exactamente 1 fila, significa que el usuario existe y obtengo los datos. Después compruebo si la contraseña es correcta. Para los usuarios frontend uso password_verify() porque su contraseña está hasheada en la base de datos. Para los usuarios backend comparo la contraseña directamente (texto plano) porque la contraseña de admin está almacenada de forma diferente. En el próximo proyecto, por supuesto, también hashearé las contraseñas de los usuarios backend, ya que en realidad son “más importantes”, pero como esas se crearon con la base de datos, por ahora no están hasheadas.

- Después de todo eso, si la contraseña es correcta, guardo la información de login en $_SESSION (username, id de usuario y tipo de usuario). Después redirijo al usuario a profile.php. Si algo va mal, muestro un error como “contraseña incorrecta” o “usuario no existe”.

- Otra cosa interesante de PHP que hice fue procesar_puntuacion.php. Esto es para las reseñas. Primero me conecto a MySQL. Después compruebo si la página fue accedida con un POST, lo que significa que el formulario de reseña fue enviado. Si es POST, tomo los valores del formulario: el texto de la reseña, el id de la película (id_pelicula) y el id del usuario (id_usuario). Después creo una consulta INSERT que añade una nueva fila en la tabla resenas, conectando la reseña con la película correcta y el usuario correcto usando claves foráneas. Luego ejecuto la consulta dentro de un try/catch. Si el insert funciona, imprimo “ok” y paro el script. Si algo falla (por ejemplo un error de base de datos), devuelvo HTTP 400 e imprimo “error”. Esta es la única vez en el proyecto que usé try/catch. Es un poco más avanzado de lo que realmente hemos usado en clase, así que fue más una prueba para ver si podía usarlo bien.

```
<?php

include __DIR__ . "/../back/inc/db.php";

$error = "";
$success = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $comentario = $_POST['comentario'];
    $id_pelicula    = $_POST['id_pelicula'];
    $id_usuario     = $_POST['id_usuario'];

    $sql = "
    INSERT INTO resenas(
        comentario,
        id_pelicula,
        id_usuario

    ) VALUES (
        '$comentario',
        $id_pelicula,
        $id_usuario
    )
";

    try {
        $conexion->query($sql);
        echo "ok";
        exit;

    } catch (mysqli_sql_exception $e) {
        http_response_code(400);
        echo "error";
        exit;
    }



}

?>
```

- Ahora todo lo anterior ha tenido que ver con el frontend de la aplicación. Es hora de pasar al backend. El backend consiste en una estructura CRUD simple pero efectiva (como se puede ver en el resumen de carpetas). En inc en backend, tenemos Create, Read, Update, Delete.

- Primero el Create. Se llama procesaformulario, y lo único que realmente hace es conectarse a la base de datos e insertar algunos datos. El estilo estaba en un archivo separado, en HTML. Esto fue una de las partes más simples de PHP del proyecto.

```
<?php
include __DIR__ . "/../db.php";

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

$conexion->query($sql);
$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>
```

- El Delete fue aún más simple. Simplemente seleccionamos la película y la eliminamos de la base de datos.

```
<?php
include __DIR__ . "/../db.php";


$id = $_GET['id'];

$sql = "DELETE FROM peliculas WHERE id_pelicula = $id";

$conexion->query($sql);

$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>
```

- Read. Esto es lo que muestra nuestra lista de películas en el backend index.php. Aquí ejecuto una consulta SELECT para obtener la información básica de cada película (id, nombre, director, fecha de estreno) y también el nombre de la categoría. Uso un LEFT JOIN con categorias para que las películas se sigan mostrando incluso si una película no tiene una categoría conectada. Si no, sería poco práctico.

Después de eso, recorro el resultado con fetch_assoc(). Para cada película, imprimo una fila <tr> con columnas <td> mostrando los datos. Al final de la fila añado dos enlaces de acción: uno para editar y otro para eliminar. Estos enlaces envían accion=editar o accion=eliminar y el id de la película en la URL, para que la misma página sepa qué acción realizar.

```
<table>
<?php
include __DIR__ . "/../db.php"; 


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

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
  echo "<tr>";
    echo "<td>".$fila['nombre']."</td>";
    echo "<td>".$fila['director']."</td>";
    echo "<td>".$fila['fecha_estreno']."</td>";
    echo "<td>".$fila['nombre_categoria']."</td>";
    echo "<td><a href='?accion=editar&id=".$fila['id_pelicula']."' class='editar' title='Editar película'>✎</a></td>";
    echo "<td><a href='?accion=eliminar&id=".$fila['id_pelicula']."' class='eliminar' title='Eliminar película'>✖</a></td>";
  echo "</tr>";
}

$conexion->close();
?>
</table>
```

- Update fue lo más complicado de los 4, así que lo incluiré todo. Primero, en la página de edición, me conecto a la base de datos y selecciono la película específica que me interesa, usando el id de la URL ($_GET['id']). Luego imprimo un formulario HTML donde los inputs ya están rellenados con los datos actuales de la película de la base de datos (nombre, director, fecha de estreno, descripción y categoría). También incluyo el id de la película como un input oculto para que se envíe cuando se envía el formulario.

Cuando pulso submit, el formulario envía los datos con POST a procesaformulario.php. En ese archivo me conecto a la base de datos otra vez, recojo todos los valores del formulario desde $_POST, y ejecuto una consulta UPDATE en la tabla peliculas. Esto actualiza los campos de la película en la base de datos para el id_pelicula correcto.

Después de que el update se complete, cierro la conexión y redirijo de vuelta al panel de administración (escritorio.php) para poder ver inmediatamente la película actualizada en la lista.

```
<?php
include __DIR__ . "/../db.php";

$id_pelicula   = $_POST['id_pelicula'];
$nombre        = $_POST['nombre'];
$director      = $_POST['director'];
$fecha_estreno = $_POST['fecha_estreno'];
$descripcion   = $_POST['descripcion'];
$id_categoria  = $_POST['id_categoria'];

$sql = "
  UPDATE peliculas SET
    nombre = '$nombre',
    director = '$director',
    fecha_estreno = '$fecha_estreno',
    descripcion = '$descripcion',
    id_categoria = $id_categoria
  WHERE id_pelicula = $id_pelicula
";

$conexion->query($sql);
$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>

<?php
include __DIR__ . "/../db.php";

/* Traemos la peli espicifico a editar */
$sql = "SELECT * FROM peliculas WHERE id_pelicula = ".$_GET['id'].";";

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
?>

<form action="inc/update/procesaformulario.php" method="POST">

  <!-- ID (oculto) -->
  <input type="hidden" name="id_pelicula" value="<?= $fila['id_pelicula'] ?>">

  <div class="controlformulario">
    <label for="nombre">Nombre de la película</label>
    <input type="text" name="nombre" id="nombre" value="<?= $fila['nombre'] ?>">
  </div>

  <div class="controlformulario">
    <label for="director">Director</label>
    <input type="text" name="director" id="director" value="<?= $fila['director'] ?>">
  </div>

  <div class="controlformulario">
    <label for="fecha_estreno">Fecha de estreno</label>
    <input type="date" name="fecha_estreno" id="fecha_estreno" value="<?= $fila['fecha_estreno'] ?>">
  </div>

  <div class="controlformulario">
    <label for="descripcion">Descripción</label>
    <textarea name="descripcion" id="descripcion"><?= $fila['descripcion'] ?></textarea>
  </div>

  <div class="controlformulario">
    <label for="id_categoria">Categoría (ID 1-15)</label>
    <input type="number" name="id_categoria" id="id_categoria" value="<?= $fila['id_categoria'] ?>">
    <select name="id_categoria"><Option id="1">Option 1</option><Option id="2">Option 2</option></select>
  </div>

  <input type="submit">

</form>

<?php
}
?>
```


## 4.-Conclusión breve

Trabajar en la parte de programación de este proyecto ha sido el proceso de programación más completo y desafiante en el que he participado hasta ahora. Tener que conectar todo (base de datos, lógica PHP, sesiones, CRUD y las páginas) fue mucho más difícil de lo que esperaba al principio. A lo largo del proyecto aprendí a respetar cuánta lógica hay detrás de una web “simple” (que al final no resultó ser tan simple), y aprendí mucho mejorando el código poco a poco hasta que funcionó como queríamos.

También me di cuenta de lo diferentes que son realmente el frontend y el backend, porque resuelven dos problemas muy distintos. El frontend trata sobre lo que el usuario ve y cómo se comporta la web, mientras que el backend trata sobre control y seguridad (que me aseguraré de mejorar mucho la próxima vez), y sobre gestionar los datos correctamente. Aprendí que pequeñas decisiones de programación, como usar db.php para una única conexión compartida, usar sesiones para controlar el acceso y usar JOINs para mostrar información completa, hacen que todo el proyecto se sienta mucho más profesional. En general fue un proyecto muy bueno, y siento que puedo usar estas habilidades en proyectos futuros y en trabajo real.

 ## ################################################################################################################################


## 1.-Introducción breve y contextualización

This programming exam is a part of a broader exam, consisting of the subjects: Base de Datos, Lenguajes de Marcas, Programacion and Proyecto intermodular. In this exam i will explain what i have learned in programming in the last two trimesters at CEAC as well as how our group made the project that we called Chamitos Movie Club.

 A bit of contect: This project consists of a database as the groundwork, and then php, js, html and css. It is the first project that we have made that is developed as a proper group project. We choose to make a mini application where you can review movies, log in / out, and where the admins have the options to create and delete movies in a seperate panel


## 2 & 3.-Desarrollo detallado y preciso + Aplicación práctica

- Starting this project we talked about what we could use as a controller- we were debating a lot about wether to use Python or PHP, and finally ended up with PHP, since it seemed a but more professional for this project. PHP is also the latest thing we have learned about, which made the project a bit more of a challange- which we welcomed. 

- We choose to structure the project in the following way. We used the latest setup Josevicente showed us, with a separate front / back, and then the controllers in each their place.

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


- One could say that the heart of the project actually starts in the database-which we connect to in db.php, like this. 

```
<?php
$conexion = new mysqli(
  "localhost",
  "peliculas_app",
  "Peliculas123$",
  "proyecto_peliculas"
);

if ($conexion->connect_error) {
  die("Database connection failed");
}
```

- Here we have a php/sql connection to the database. This is just a conecction, and nothing more. The reason we made this is because now in all of the other files when we needed a database connection, we can just link to db.php. We thought this was pretty smart. I rememeber just 3 months ago when we started doing CRUD projects, and we had a database connection in each file. This is much more intelligent.

- We use the database connection in lots of places, like the following here.

```
include __DIR__ . "/../../back/inc/db.php";

$sql = "
SELECT 
    p.id_pelicula,
    p.nombre,
    p.director,
    p.fecha_estreno,
    p.imagen,
    c.nombre_categoria,
    p.descripcion
FROM peliculas p
JOIN categorias c ON p.id_categoria = c.id_categoria
ORDER BY p.id_pelicula ASC
";
```

- Here you can see how after the connection we select specific things from the database that we are interested in. Here it is the information that we show on the frontpage of the project. Now this could technically have been pre-prepared as a view, and i think that that is how we will do it next project. But for this project, it worked even though it isnt too elegant.

- Now this next part here used that information and "prints" it in a way that we can use it in our design. You can see this here us a mix of html and php. Since html is build into php, this works very well together. This avoids duplicated code and makes maintenance easier with only one place to update credentials.

```
$resultado = $conexion->query($sql);

echo "<h2>Catálogo de películas</h2>";

echo "<div class='movie-grid'>";   // GRID wrapper

while ($fila = $resultado->fetch_assoc()) {
  echo "
      <article class='movie-card'>
          <a href='movie.php?id={$fila['id_pelicula']}'>
              <img src='img/peliculas/{$fila['imagen']}' alt='Poster {$fila['nombre']}'>
          </a>

          <h3>
            <a href='movie.php?id={$fila['id_pelicula']}'>
              {$fila['nombre']}
            </a>
          </h3>
          <p><strong>Director:</strong> {$fila['director']}</p>
          <p><strong>Category:</strong> {$fila['nombre_categoria']}</p>
          <p><strong>Release:</strong> {$fila['fecha_estreno']}</p>
          <p>{$fila['descripcion']}</p>
      </article>
  ";
}

echo "</div>";  
$conexion->close();
```

- Now another page that showcases some interesting php, is the detalle_pelicula page. Is is the page you ends up at, if you click one one of the movies at the main page. First, like always we start with a database connection

```
include __DIR__ . "/../../back/inc/db.php";

/* A check that the movie id exists */
if (!isset($_GET['id']) || !is_numeric($_GET['id'])) {
    echo "<p>Película no válida.</p>";
    exit;
}
```
- but that is then followed by a check that makes sure the movie actually exists. This is to avoid that people can change the URL to like ID18, and then go to movie with ID18, even if it doesnt exist anymore that movie. On that page we also have this check, which works with sessions. This is one of the checks that the webpage have that checks wether you are already in a session or no. The reason we dodthis is becase depenidng on the answer (depending on wether you are logged in or not) you can see different buttons and have differents rights- like the right to write a review. You can only do this if you are logged in.  

<?php if (!isset($_SESSION['frontend_user'])): ?>

  <p class="login-aviso">
    Debes iniciar sesión para escribir una reseña.
  </p>
  <a href="login.php">Ir al login</a>

<?php else: ?>

- On the detalle_pelicula side we also use joins:
$sql = "
SELECT
    p.nombre,
    p.director,
    p.duracion_min,
    p.restriccion_edad,
    p.fecha_estreno,
    p.descripcion,
    p.imagen,
    c.nombre_categoria
FROM peliculas p
JOIN categorias c ON p.id_categoria = c.id_categoria
WHERE p.id_pelicula = $id_pelicula
";

$sql2 = "
SELECT r.comentario, u.nombre
FROM resenas r
JOIN usuarios u ON r.id_usuario = u.id_usuario
WHERE r.id_pelicula = $id_pelicula
";

- You can see that the JOIN is used to combine data from two tables using a related key (PK -> FK), so i can show more related information. I use JOIN peliculas + categorias to get the category name (nombre_categoria) for each movie, because the movie table only stores id_categoria. Then i use JOIN resenas + usuarios to get the username (u.nombre) for each review, because the review table only stores id_usuario. I was pretty proud of this solution. This is a good deal more advanced than anything we learned in the first trimester, and it really shows how i have progressed through the last few months.

- We also used sessions in the log-in part of the website. This here is the following php for login.php

```
<?php

session_start();

include __DIR__ . "/../back/inc/db.php";

$error = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username == "" || $password == "") {
        $error = "Rellena todos los campos.";
    } else {

        $sql = "
        SELECT id_usuario, username, password, tipo_usuario
        FROM usuarios
        WHERE username = '$username'
    ";


        $resultado = $conexion->query($sql);

        if ($resultado->num_rows == 1) {

            $fila = $resultado->fetch_assoc();

            if (
                ($fila['tipo_usuario'] === 'frontend' && password_verify($password, $fila['password']))
                ||
                ($fila['tipo_usuario'] === 'backend' && $password === $fila['password'])
            ) {


                $_SESSION['frontend_user'] = $fila['username'];
                $_SESSION['frontend_user_id'] = $fila['id_usuario'];
                $_SESSION['tipo_usuario'] = $fila['tipo_usuario'];



                header("Location: profile.php");
                exit;
            } else {
                $error = "Contraseña incorrecta.";
            }
        } else {
            $error = "Usuario no existe.";
        }
    }
}
?>
```
- This is probably the most "complicated" pieve of php in the entre project. It is not in itself very complicated, but the logic to think it out took be a good while, first time around. First you can see that I start the session with session_start() because I need to remember if the user is logged in or not. I of course include db.php to connect to the database. When the form is submitted (with POST), I take the username and password from the input fields. If one of them is empty, I show an error message.

- If both fields are filled, I run a SQL query to find a user in the table usuarios with the same username. If the query returns exactly 1 row, it means the user exists, and I fetch the user data. Afterwards I check if the password is correct. For frontend users I use password_verify() because their password is hashed in the database. For backend users I compare the password directly (plain text) because the admin password is stored differently. In the next project i will of course also hash the backend users passwords, since those acutally are "more important", but because those were made with the database, as of now, they arent hashed. 
- The, after all that, If the password is correct, I save the login information in $_SESSION (username, user id, and user type). After that I redirect the user to profile.php. If something is wrong, I show an error like “wrong password” or “user does not exist”. 


- another interesting php thing i did was the procesar_punctuacion.php. This is all for the reviews. First I connect to MySQL. Then I check if the page was accessed with a POST request, which means the review form was submitted. If it is POST, I take the values from the form- the review text, the movie id (id_pelicula) and the user id (id_usuario). After that I create an INSERT query that adds a new row into the table resenas, connecting the review to the correct movie and the correct user using foreign keys. Then I run the query inside a try/catch. If the insert works, I print "ok" and stop the script. If something fails (for example a database error), I return HTTP 400 and print "error". This is the only time in the project i used try/catch. Its a bit more advanced that what we have really used in class, so it was mostly a test to see if i could use it properly.

```
<?php

include __DIR__ . "/../back/inc/db.php";

$error = "";
$success = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $comentario = $_POST['comentario'];
    $id_pelicula    = $_POST['id_pelicula'];
    $id_usuario     = $_POST['id_usuario'];

    $sql = "
    INSERT INTO resenas(
        comentario,
        id_pelicula,
        id_usuario

    ) VALUES (
        '$comentario',
        $id_pelicula,
        $id_usuario
    )
";

    try {
        $conexion->query($sql);
        echo "ok";
        exit;

    } catch (mysqli_sql_exception $e) {
        http_response_code(400);
        echo "error";
        exit;
    }

    

}

?>
```


- Now all of this above have had something to do with the frontend of the applicataion- its time we move on to the backend. The backend consists of a simple but effictive, CRUD structure (as you can see i the overview of the folders). In inc in backend, we have Create, Read, Update, Delete. 

- first the Create. Its called procesaformulario, and the only thing it readdy does is connect to the database, and insert some data into this. The styling was one in a seperate file, in html. This here was one of the more simple php items of the project. 
```
<?php
include __DIR__ . "/../db.php";

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

$conexion->query($sql);
$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>
```

- Deleting was even more simple. We simply select the movie, and delete it from the database. 

```
<?php
include __DIR__ . "/../db.php";


$id = $_GET['id'];

$sql = "DELETE FROM peliculas WHERE id_pelicula = $id";

$conexion->query($sql);

$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>
```
- Reading. This here is what shows our list of movie on the backend index.php. Here I run a SELECT query to get the basic information for each movie (id, name, director, release date) and also the category name. I use a LEFT JOIN with categorias so that the movies are still shown even if a movie does not have a category connected. Otherwise it would have impractical. 

After that, I loop through the result with fetch_assoc(). For each movie, I print one <tr> row with <td> columns showing the movie data. At the end of the row I add two action links: one for editing and one for deleting. These links send accion=editar or accion=eliminar and the movie id in the URL, so the same page can know what action to perform.
```
<table>
<?php
include __DIR__ . "/../db.php"; 


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

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
  echo "<tr>";
    echo "<td>".$fila['nombre']."</td>";
    echo "<td>".$fila['director']."</td>";
    echo "<td>".$fila['fecha_estreno']."</td>";
    echo "<td>".$fila['nombre_categoria']."</td>";
    echo "<td><a href='?accion=editar&id=".$fila['id_pelicula']."' class='editar' title='Editar película'>✎</a></td>";
    echo "<td><a href='?accion=eliminar&id=".$fila['id_pelicula']."' class='eliminar' title='Eliminar película'>✖</a></td>";
  echo "</tr>";
}

$conexion->close();
?>
</table>
```
- Updateting was the most complicated of the 4, so i will include all of it. First, on the edit page, I connect to the database and select the specific movie that i am interested in, using the id from the URL ($_GET['id']). Then I print an HTML form where the inputs are already filled with the current movie data from the database (name, director, release date, description, and category). I also include the movie id as a hidden input so it gets sent when the form is submitted.

When I press submit, the form sends the data with POST to procesaformulario.php. In that file I connect to the database again, collect all the form values from $_POST, and run an UPDATE query on the table peliculas. This updates the movie fields in the database for the correct id_pelicula.

After the update is done, I close the connection and redirect back to the admin dashboard (escritorio.php) so I can immediately see the updated movie in the list.

```
<?php
include __DIR__ . "/../db.php";

$id_pelicula   = $_POST['id_pelicula'];
$nombre        = $_POST['nombre'];
$director      = $_POST['director'];
$fecha_estreno = $_POST['fecha_estreno'];
$descripcion   = $_POST['descripcion'];
$id_categoria  = $_POST['id_categoria'];

$sql = "
  UPDATE peliculas SET
    nombre = '$nombre',
    director = '$director',
    fecha_estreno = '$fecha_estreno',
    descripcion = '$descripcion',
    id_categoria = $id_categoria
  WHERE id_pelicula = $id_pelicula
";

$conexion->query($sql);
$conexion->close();

header("Location: /oscar-bryan-carlos/Chamitos_Movie_Club/back/escritorio.php");
exit;

?>

<?php
include __DIR__ . "/../db.php";

/* Traemos la peli espicifico a editar */
$sql = "SELECT * FROM peliculas WHERE id_pelicula = ".$_GET['id'].";";

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
?>

<form action="inc/update/procesaformulario.php" method="POST">

  <!-- ID (oculto) -->
  <input type="hidden" name="id_pelicula" value="<?= $fila['id_pelicula'] ?>">

  <div class="controlformulario">
    <label for="nombre">Nombre de la película</label>
    <input type="text" name="nombre" id="nombre" value="<?= $fila['nombre'] ?>">
  </div>

  <div class="controlformulario">
    <label for="director">Director</label>
    <input type="text" name="director" id="director" value="<?= $fila['director'] ?>">
  </div>

  <div class="controlformulario">
    <label for="fecha_estreno">Fecha de estreno</label>
    <input type="date" name="fecha_estreno" id="fecha_estreno" value="<?= $fila['fecha_estreno'] ?>">
  </div>

  <div class="controlformulario">
    <label for="descripcion">Descripción</label>
    <textarea name="descripcion" id="descripcion"><?= $fila['descripcion'] ?></textarea>
  </div>

  <div class="controlformulario">
    <label for="id_categoria">Categoría (ID 1-15)</label>
    <input type="number" name="id_categoria" id="id_categoria" value="<?= $fila['id_categoria'] ?>">
    <select name="id_categoria"><Option id="1">Option 1</option><Option id="2">Option 2</option></select>
  </div>

  <input type="submit">

</form>

<?php
}
?>
```


## 4.-Conclusión breve

Working on the programming part of this project was the most complete and challenging programming process I have been part of so far. Having to connect everything together (database, PHP logic, sessions, CRUD, and the pages) was much more difficult than I expected in the beginning. Throughout the project I learned to respect how much logic is needed behind a “simple” website (that didnt end up being quite so simple), and I learned a lot by slowly improving the code step by step until it worked the way we wanted. 

I also realized how different the frontend and backend really are, because they solve two very different problems. The frontend is about what the user sees and how the site behaves, while the backend is about control and security (which i will make sure to improve a lot on by next time), and managing the data correctly. I learned that small programming decisions, like using db.php for one shared connection, using sessions to control access, and using JOINs to show complete information, makes the whole project feel much more professional. Overall it was a very good project, and I feel like I can use these skills in future projects and real work.


