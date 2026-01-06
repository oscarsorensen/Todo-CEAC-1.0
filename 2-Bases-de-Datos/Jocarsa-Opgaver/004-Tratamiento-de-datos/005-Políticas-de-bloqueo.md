En esta actividad estudio la codificación, descodificación y hash en PHP. Después de esto, mi objetivo es comprender cómo funciona base64, cómo descodificar texto codificado y en qué se diferencia el hash, ya que no se puede revertir. También utilizo funciones, bucles y manejo de cadenas mientras pruebo estas cosas con ejemplos reales, como contraseñas y texto normal.

En la tarea, observé cómo funcionan la codificación y la descodificación base64 en PHP, comprobando que el valor original se puede devolver correctamente después de la descodificación. A continuación, trabajo con funciones especiales que codifican y descodifican varias veces utilizando bucles, y las pruebo con diferentes contraseñas. También trabajo con el funcionamiento del hash con MD5 y SHA-1, y aprendo a comprender que los hash no se pueden descodificar y se utilizan para verificar la integridad y la seguridad en lugar de recuperar el texto original. Por último, veo otro método de codificación (codificación romana) que utiliza valores ASCII y manipulación de caracteres en PHP.

# ---------- Desarrollo ----------
- Codificación
Observado

- Descodificación
contraseñasegura1234
Y29udHJhc2XDsWFzZWd1cmExMjM0
contraseñasegura1234

- Funciones de Codificación y Descodificación
    La contraseña de ejemplo.

contrasenaejemplo123
Vm0wd2VHUXhTWGhXV0doVlltdHdVRlp0TVc5V01XeHlXa2M1VjAxWGVGWlZNbkJUVmpGYWRHVkljRmhoTWsweFdWZDRZV014VG5OaVIwWlhWakZLU1ZaclpEUlpWMUpIVm01T2FGSnRhRzlVVm1oRFpWWmtWMXBFVWxwV01VcFlWVzAxVDJGV1NuTlhiR2hhWWtkU2RscFdXbXRXTVdSMFVteFNUbEpHV1hkV1Z6RXdWakZhZEZOclpGaGlSMmhXVm10V1MxUkdXbFpYYlVaWFlrZFNlVll5ZUVOV01rVjNZMFpTVjFaV2NGTmFSRVpEVld4Q1ZVMUVNRDA9
contrasenaejemplo123

- Codificación ASCII:
    El valor ASCII a la letra original con chr
a
97
a

# ---------- Ejercicios Propuestos ----------
- Ejercicio 1: Codificar y Descodificar Contraseña, 3 veces
<?php
	function codificar($cadena){
  	for($i = 0;$i<3;$i++){
    	$cadena = base64_encode($cadena);
    }
    return $cadena;
  }
  function descodificar($cadena){
  	for($i = 0;$i<3;$i++){
    	$cadena = base64_decode($cadena);
    }
    return $cadena;
  }
  
  $contrasena = "hola";
  echo $contrasena;
  echo "<br>";
  
  $codificado = codificar($contrasena);
  echo $codificado;
  echo "<br>";
  
  $descodificado = descodificar($codificado);
  echo $descodificado;
  echo "<br>";
?>

El resultado:
hola
WVVjNWMxbFJQVDA9
hola

- Ejercicio 2: Hasheo de Contraseñas, 3 veces

Hola
f688ae26e9cfa3ba6235477831d5122e
4e46dc0969e6621f2d61d2228e3cd91b75cd9edc

Hola123
5d5b53417c8ff7d13aa16623d384763a
de09b82971cc49e8c5ccee41fc7f59cc8dcdee27

TestFraDanmarkÆØÅ
9d69bb9721cd6f2f3fa5bf6a5b14d84c
8f475a6393ccd19d4eda15d8b69cbb7fe8efa231

<?php

	$cadena = "TestFraDanmarkÆØÅ";
  echo $cadena;
  echo "<br>";
  
  // Hash mediante md5
  
  $picadillo1 = md5($cadena);
  echo $picadillo1;
  echo "<br>";
  
  // Hash mediante sha1 
  
  $picadillo2 = sha1($cadena);
  echo $picadillo2;
  echo "<br>";
  
?>

- Ejercicio 3: Codificación Romana:
<?php
	function codificaRomana($cadena){
  	for($i = 0;$i<strlen($cadena);$i++){
    	$cadena[$i] = chr(ord($cadena[$i])+10);
    }
    return $cadena;
  }
  function descodificaRomana($cadena){
  	for($i = 0;$i<strlen($cadena);$i++){
    	$cadena[$i] = chr(ord($cadena[$i])-10);
    }
    return $cadena;
  }
  $original = "Hola esto es un texto que estoy escribiendo para hacer una prueba con algo más largo";
  echo $original;
  echo "<br>";
  
  $codificado =  codificaRomana($original);
  
  echo $codificado;
  echo "<br>";
  
  $descodificado =  descodificaRomana($codificado);
  
  echo $descodificado;
  echo "<br>";
?>
Test 1

Hola esto es un texto que estoy escribiendo para hacer una prueba con algo más largo
Ryvk*o}~y*o}*x*~o�~y*{o*o}~y�*o}m|slsoxny*zk|k*rkmo|*xk*z|olk*myx*kvqy*wͫ}*vk|qy
Hola esto es un texto que estoy escribiendo para hacer una prueba con algo más largo

Test 2
This is another short test
^rs}*s}*kxy~ro|*}ry|~*~o}~
This is another short test

Test 3
Esto es ena prueba con caracteres daneses æøå y simbolos €@
O}~y*o}*oxk*z|olk*myx*mk|km~o|o}*nkxo}o}*Ͱ��ͯ*�*}swlyvy}*쌶J
Esto es ena prueba con caracteres daneses æøå y simbolos €@


Esta tarea me ayudó a comprender la diferencia entre codificación, descodificación y hash. La codificación se puede revertir, pero el hash no, lo cual es importante para la seguridad de las contraseñas en aplicaciones reales. Me pareció muy interesante que base64 y hash funcionaran con caracteres daneses, pero la codificación romana no. Después de esta tarea, investigaré este tema. Como soy danés, me intrigó.