<?php

$host = "localhost";
$user = "blogphp";
$pass = "Blogphp123$";
$db   = "blogphp";

$conexion = new mysqli($host, $user, $pass, $db);

$sql = "SELECT id, titulo, contenido, fecha, autor FROM blog";

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
  echo "ID: " . $fila['id'] . "<br>";
  echo "Nombre: " . $fila['titulo'] . "<br>";
  echo "Email: " . $fila['contenido'] . "<br><br>"; // kept your variable names
}

$conexion->close();
?>
