En este ejercicio, utilizo sesiones PHP para mantener la información disponible entre diferentes páginas web. Las variables normales se pierden al pasar de una página a otra, por lo que se necesita un mecanismo para mantener los datos del usuario en toda la aplicación. Este mecanismo son las sesiones. Esta situación es habitual en proyectos web reales en los que es importante la coherencia entre las páginas.

Por supuesto, utilizo sesiones PHP para esta tarea. Inicio la sesión con session_start() y almaceno el valor en la matriz $_SESSION en origen.php. A continuación, en destino.php, inicio la sesión de nuevo y recupero la misma variable. Esto garantiza que los datos persistan entre páginas sin utilizar variables globales ni bibliotecas externas.

# ---------- Enunciado paso a paso 1-4 ----------

Para lograr este tarea, utilizo sesiones.
- origin.php
<?php
	session_start();
	$_SESSION['nombre'] = "Jose Vicente";
?>
<a href="destino.php">Vamos a otra página</a>

- destino.php

<?php
	session_start();
	echo $_SESSION['nombre'];
?>


Al utilizar sesiones, puedo mantener la información del usuario disponible en varias páginas de forma controlada y correcta. Esto me resulta muy útil para mi proyecto final de programación, en el que los usuarios navegarán entre páginas y esperarán que sus datos se mantengan coherentes en toda la aplicación. Como ya he empezado el otro proyecto, puedo decir que esta mini tarea me ha resultado muy útil y me ha ayudado mucho.