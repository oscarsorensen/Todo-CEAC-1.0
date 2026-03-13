<?php
	session_start();
  
  $_SESSION['nombre'] = "Oscar";
  $_SESSION['apellidos'] = "Sorensen";
  
  foreach($_SESSION as $clave=>$valor){
  	echo $clave.": ".$valor."<br>";
  }
?>