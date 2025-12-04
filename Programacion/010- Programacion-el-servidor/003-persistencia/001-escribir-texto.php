<?php
$manejador = fopen("archivo.txt", "a"); // "a" = append
fwrite($manejador, "Nuevo texto escrito desde PHP\n");
fclose($manejador);
?>
