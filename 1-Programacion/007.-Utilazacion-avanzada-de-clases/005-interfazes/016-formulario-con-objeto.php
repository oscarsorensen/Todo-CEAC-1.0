

<?php
	
  $cliente = [
  	"nombre" => "Oscar Sorensen",
    "apellidos" => "Sjorman ",
    "email" => "info@oscar.com"
  ];
  
  foreach($cliente as $clave=>$valor){
  	echo "<label>".$clave."</label>";
    echo "<input type='text' value='".$valor."'>";
  }
 
?>