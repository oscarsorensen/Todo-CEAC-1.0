En este ejercicio, practico cómo enviar y recibir datos utilizando los métodos HTTP GET y POST. Esto se utiliza para una sencilla aplicación web destinada a un entrenador personal que desea registrar la información básica de sus clientes. Se trata de un paso muy importante hacia el desarrollo web real, ya que los formularios son una de las principales formas en que los usuarios interactúan con las aplicaciones web y envían y recuperan datos al servidor.

Utilizo formularios HTML para enviar datos con los métodos GET y POST, y PHP para recibir y procesar esos datos. Con GET, los datos se envían a través de la URL y se accede a ellos utilizando la matriz $_GET. Esto solo es adecuado para pequeños fragmentos de datos. Con POST, los datos se envían de forma segura en el cuerpo de la solicitud y se accede a ellos utilizando la matriz $_POST. Más adelante en la tarea, utilizo isset() para comprobar que los campos existen antes de utilizarlos y valido el campo de correo electrónico utilizando el método integrado de PHP para asegurarme de que es válido y de que el formato es correcto.

# ---------- 1. Formulario de Registro (GET) ----------
- formulario.html

<form action="procesar_get.php" method="GET">
    <p>Introduce tu nombre</p>
    <input type="text" name="nombre">
    <input type="text" name="apellidos">
    <input type="submit">
  </form>


- procesar_get.php
<?php
    echo $_GET['nombre'];
    echo "<br>";
    echo $_GET['apellidos'];
?>

# ---------- 2. Formulario de Registro (POST) ----------

- formulario_post.html

<form action="procesar_post.php" method="POST">
    <p>Introduce tu nombre y edad</p>
    <input type="text" name="nombre">
    <input type="text" name="edad">
    <input type="submit">
  </form>

- procesar_post.php

<?php
    echo $_POST['nombre'];
    echo "<br>";
    echo $_POST['edad'];
?>

# ---------- 3. Formulario de Registro (POST) con Validación ----------

- formulario_validacion.html
<form action="procesar_post_validacion.php" method="POST">
    <p>Introduce tu nombre, edad y email</p>
    <input type="text" name="nombre" id="nombre">
    <input type="number" name="edad" id="edad">
    <input type="text" name="email" id="email">
    <input type="submit">
  </form>

- procesar_post_validacion.php

<?php

if (
    isset($_POST['nombre']) &&
    isset($_POST['edad']) &&
    isset($_POST['email'])
) {
    if (filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
        echo $_POST['nombre'];
        echo "<br>";
        echo $_POST['edad'];
        echo "<br>";
        echo $_POST['email'];
    } else {
        echo "Email no válido";
    }
}

?>

# ---------- 4. Formulario de Registro (POST) con Validación y Redirección ----------

- formulario_redireccion.html

<form action="procesar_post_redirection.php" method="POST">
    <p>Introduce tu nombre, edad y email</p>
    <input type="text" name="nombre" id="nombre">
    <input type="number" name="edad" id="edad">
    <input type="text" name="email" id="email">
    <input type="submit">
  </form>

- procesar_post_redirection.php

<?php

if (
    isset($_POST['nombre']) &&
    isset($_POST['edad']) &&
    isset($_POST['email'])
) {
    if (filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
        header("Location: confirmacion.html");
        exit;
    } else {
        echo "Email no válido";
    }
}

?>

- confirmacion.html
<h1>Registro completado correctamente</h1>
<p>Gracias por enviar el formulario.</p>


Este ejercicio me ayudó a practicar la diferencia entre GET y POST y cómo fluyen los datos desde un formulario al servidor. Ahora también comprendo mejor la importancia de validar la información introducida por el usuario antes de procesarla. Estos conceptos son esenciales en proyectos web reales, como el registro de usuarios, los formularios de contacto y los sistemas de inicio de sesión, donde el manejo y la validación correctos de los datos son muy importantes. Esta es una de las mejores tareas prácticas que he realizado en mucho tiempo. Sentí como si algo «encajara» al hacerlo. Será muy útil para el futuro.