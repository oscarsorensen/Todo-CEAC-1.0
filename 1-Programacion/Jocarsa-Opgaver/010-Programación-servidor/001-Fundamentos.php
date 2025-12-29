<!--
En este ejercicio practico la toma de decisiones básicas en PHP. Utilizo un ejemplo de la vida real que comprueba la edad. Esto también podría usarse para hacer comprobaciones relacionadas con el estilo de vida o la salud, el gimnasio y la cocina en la vida diaria. Puedes usar la lógica de programación para decidir si alguien todavía es “joven” o no, como hago aquí. O puedes usar PHP para decidir otras cosas relacionadas con el estilo de vida.
Primero, creo una variable llamada $edad y le asigno un valor. Luego utilizo una estructura if–else para comprobar ese valor. Si la edad es menor de 30, el programa imprime “Eres un joven”. En caso contrario, imprime “Ya no eres un joven”. Esto sigue exactamente lo que aprendimos en clase: usar condiciones para controlar lo que el programa debe decir según la situación. Probé con las edades 25 y 35 y puse la salida en comentarios.
-->

<?php

	$edad = 25;
  if($edad < 30){
  	echo "Eres un joven";
  }else{
  	echo "Ya no eres un joven";
  }
  
//output con edad 25: Eres un joven
//output con edad 35: Ya no eres un joven


?>

<!--
Este ejercicio me ayudó a practicar cómo funciona la lógica if–else en PHP y cómo pequeñas condiciones (como la edad) pueden cambiar el comportamiento y la salida de un programa. Puedo ver cómo esto se relaciona con la vida real, donde la edad, la salud y los hábitos importan. Muestra cómo la lógica de programación simple puede aplicarse a situaciones cotidianas.
-->