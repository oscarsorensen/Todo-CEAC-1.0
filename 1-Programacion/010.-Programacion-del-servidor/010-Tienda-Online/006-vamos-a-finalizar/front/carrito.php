<?php include "inc/cabecera.php"; ?>

<p>Carrito</p>

<?php
	echo "El producto es: ".$_POST['id']."<br>";
  echo "Las unidades son: ".$_POST['unidades']."<br>";
?>

<form method="POST" action="finalizacion.php">

	<!-- Datos de los productos -->
  <input type="hidden" name="idproducto" value="<?= $_POST['id'] ?>">
  <input type="hidden" name="unidades" value="<?= $_POST['unidades'] ?>">
  
  <!-- Datos del cliente -->
  <input type="text" name="nombre_cliente" placeholder="Nombre del cliente">
  <input type="text" name="apellidos" placeholder="Apellido del cliente">
  <input type="text" name="email" placeholder="Email del cliente">
  <input type="text" name="direccion" placeholder="Direccion del cliente">
  <input type="text" name="telefono" placeholder="Telefono del cliente">
  
  <!-- Y enviamos -->
  <input type="submit">
</form>

<?php include "inc/piedepagina.php"; ?>

