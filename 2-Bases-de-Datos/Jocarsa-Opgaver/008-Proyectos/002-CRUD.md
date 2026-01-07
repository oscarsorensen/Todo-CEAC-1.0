En este ejercicio trabajo con un ejemplo de gestión de empleados utilizando una base de datos. El ejercicio consiste en comprender cómo se crea una base de datos, cómo está estructurada y cómo podemos almacenar y controlar la información. Como ya habíamos hecho este ejercicio en clase, ahora pude hacerlo aún mejor.
 Empecé creando una base de datos para los empleados y luego utilicé operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar los datos, exactamente como lo haríamos en un proyecto de software real.

 Primero, creo la base de datos y la tabla con los campos necesarios para cada empleado, incluyendo el ID, el nombre, el puesto de trabajo, el salario, la fecha de contratación y el departamento. A continuación, creo un usuario con permisos para trabajar con esta base de datos. Técnicamente, también podría haber utilizado mi usuario ROOT, pero así queda más limpio. Además, es más profesional. Después, aplico la lógica CRUD: inserto nuevos empleados con INSERT, leo la información con SELECT, modifico los empleados con UPDATE y elimino registros con DELETE. Cada parte se realiza paso a paso utilizando PHP y MySQL, siguiendo el mismo proceso de siempre.

# ---------- Todo con la base de datos ----------
Empizo con la creación de la base de datos y la tabla para almacenar la información de los empleados.

CREATE DATABASE IF NOT EXISTS empleados
    DEFAULT CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

USE empleados;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento VARCHAR(100)
);

CREATE USER 
'empleados'@'localhost' 
IDENTIFIED  BY 'Empleados123$';

GRANT USAGE ON *.* TO 'empleados'@'localhost';

ALTER USER 'empleados'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empleados.* 
TO 'empleados'@'localhost';

FLUSH PRIVILEGES;

# ---------- CREATE ----------

- 001-crear.php
<!doctype html>
<html lang="es">
  <head>
    <title>Oscar Sorensen CRUD</title>
    <meta charset="utf-8">
  </head>
  <body>

    <form action="002-procesa.php" method="POST">
      <input type="text" name="nombre" placeholder="nombre">
			<input type="text" name="puesto" placeholder="puesto">
      <input type="text" name="salario" placeholder="salario">
      <input type="text" name="fecha_contratacion" placeholder="fecha_contratacion">
      <input type="text" name="departamento" placeholder="departamento">
      <input type="submit">
    </form>
  </body>
</html>

- 002-procesa.php
<?php
	// Primero cogemos la info que viene del formulario
  
  $nombre = $_POST['nombre'];
  $puesto = $_POST['puesto'];
  $salario = $_POST['salario'];
  $fecha_contratacion = $_POST['fecha_contratacion'];
  $departamento = $_POST['departamento'];

	 // Y luego metemos esa información en la base de datos
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);

	// Metemos los datos en la base de datos
  $sql = "
  	INSERT INTO empleados VALUES(
    	NULL,
      '".$nombre."',
      '".$puesto."',
      '".$salario."',
      '".$fecha_contratacion."',
      '".$departamento."'
    );
  ";
  $conexion->query($sql);
	
  $conexion->close();
  
?>

# ---------- READ ----------
- 001-leer.php
<?php
	session_start(); // Arranco una sesion
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);
  
	// Comprobacion exitosa pero mirando los datos que vienen del formulario en POST
  $sql = "
  	SELECT * FROM empleados;
  ";
	
  $resultado = $conexion->query($sql);
  while ($fila = $resultado->fetch_assoc()) {
  	var_dump($fila);			// Vomito en pantalla y ya luego formateare
  }
	
  	
  $conexion->close();
  
?>

# ---------- UPDATE ----------
- 001-miniformulario1.html
<!doctype html>
<html lang="es">
  <head>
    <title>Oscar Sorensen CRUD</title>
    <meta charset="utf-8">
  </head>
  <body>
    <form action="002-procesamodificar.php" method="POST">
      <p>Introduce el ID del elemento que quieres modificar</p>
      <input type="number" name="id" placeholder="id">
      <input type="submit">
    </form>
  </body>
</html>

- 002-procesamodificar.php

<?php
	// Este archivo va a:
  
  // 1.-Coger el ID
  $id = $_POST['id'];
  
  // 2.-Irse a la base de datos a por ese id
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);
  
	// Comprobacion exitosa pero mirando los datos que vienen del formulario en POST
  $sql = "
  	SELECT * FROM empleados WHERE id = ".$id.";
  ";
	
  $resultado = $conexion->query($sql);
  while ($fila = $resultado->fetch_assoc()) {
  	// 3.-Pintar un formulario en pantalla
    echo '
    	<form action="003-procesaractualizacion.php" method="POST">
      	<input type="hidden" name="id" value="'.$id.'">
        <input type="text" name="nombre" placeholder="nombre" value="'.$fila['nombre'].'">
        <input type="text" name="puesto" placeholder="puesto" value="'.$fila['puesto'].'">
        <input type="text" name="salario" placeholder="salario" value="'.$fila['salario'].'">
        <input type="text" name="fecha_contratacion" placeholder="fecha_contratacion" value="'.$fila['fecha_contratacion'].'">
        <input type="text" name="departamento" placeholder="departamento" value="'.$fila['departamento'].'">
        <input type="submit">
      </form>
    ';
    // 4.-Enviar la información modificada a un tercer archivo
  }
	
  $conexion->close();
  
  
?>

- 003-procesaractualizacion.php

<?php
	// Primero cogemos la info que viene del formulario
  
  $nombre = $_POST['nombre'];
  $puesto = $_POST['puesto'];
  $salario = $_POST['salario'];
  $fecha_contratacion = $_POST['fecha_contratacion'];
  $departamento = $_POST['departamento'];
  
  $id = $_POST['id'];

	 // Y luego metemos esa información en la base de datos
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);

	// Metemos los datos en la base de datos
  $sql = "
  	 UPDATE empleados SET
     	nombre = '".$nombre."',
      puesto = '".$puesto."',
      salario = '".$salario."',
      fecha_contratacion = '".$fecha_contratacion."',
      departamento = '".$departamento."' 
      WHERE id = ".$id."
    ;
  ";
  $conexion->query($sql);
	
  $conexion->close();
  
?>

# ---------- DELETE ----------

- 001-miniformulario.html
<!doctype html>
<html lang="es">
  <head>
    <title>Oscar Sorensen CRUD</title>
    <meta charset="utf-8">
  </head>
  <body>
    <form action="002-procesa.php" method="POST">
      <p>Introduce el ID del elemento que quieres eliminar</p>
      <input type="number" name="id" placeholder="id">
      <input type="submit">
    </form>
  </body>
</html>

- 002-procesaeliminar.php
<?php
	// Primero cogemos la info que viene del formulario
  
  $id = $_POST['id'];

	 // Y luego metemos esa información en la base de datos
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);

	// Metemos los datos en la base de datos
  $sql = "
  	DELETE FROM empleados
    WHERE id = ".$id."
  ";
  $conexion->query($sql);
	
  $conexion->close();
  
?>

Este ejercicio me ayudó a practicar cómo funciona un sistema de base de datos real y cómo se utilizan las operaciones CRUD para controlar la información. Puedo ver cómo se utiliza esto en la vida real en empresas reales para gestionar datos de forma segura y organizada. Esta actividad conecta lo que aprendimos en clase con la práctica real y muestra lo importantes que son las bases de datos en el desarrollo web.