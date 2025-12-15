<!--

http://localhost:8080/2-Bases-de-Datos/008-Proyectos/004-superCRUD-poco-a-poco/004-parametro-get.php?tabla=cliente
http://localhost:8080/2-Bases-de-Datos/008-Proyectos/004-superCRUD-poco-a-poco/004-parametro-get.php?tabla=pedido
http://localhost:8080/2-Bases-de-Datos/008-Proyectos/004-superCRUD-poco-a-poco/004-parametro-get.php?tabla=producto
http://localhost:8080/2-Bases-de-Datos/008-Proyectos/004-superCRUD-poco-a-poco/004-parametro-get.php?tabla=lineaspedido

-->

<table>
<?php
	$host = "localhost";
  $user = "tiendaonlinedamdaw";
  $pass = "Tiendaonlinedamdaw123$";
  $db   = "tiendaonlinedamdaw";

  $conexion = new mysqli($host, $user, $pass, $db);
	$resultado = $conexion->query("
  	SELECT * FROM ".$_GET['tabla'].";
  ");
  while ($fila = $resultado->fetch_assoc()) {
  	echo "<tr>";
    foreach($fila as $clave=>$valor){
    	echo "<td>".$valor."</td>";
    }
    echo "</tr>";
   }
?>
</table>