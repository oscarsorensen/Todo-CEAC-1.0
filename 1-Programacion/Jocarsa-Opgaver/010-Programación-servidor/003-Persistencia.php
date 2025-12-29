<!--
En este ejercicio trabajo con preguntas y respuestas. Puedo aplicar lo que aprendo en este ejercicio a mi rutina diaria, ya que me gusta cocinar y organizar mis actividades. Utilizo PHP para crear un formulario y almacenar los datos utilizando una matriz con nombre.
He creado una matriz con el nombre pregunta_respuesta. Dentro de la matriz, añado la pregunta "¿Qué día es hoy?" y la respuesta "Miercules". A continuación, convierto esta matriz a JSON utilizando la función json_encode. Por último, imprimo el resultado JSON en la pantalla para comprobar que todo funciona correctamente.
-->

<?php
// Hago el array nombrado
$pregunta_respuesta = array(
    "pregunta" => "Que dia es hoy?",
    "respuesta" => "Miercoles"
);

// Conviero a JSON
$json = json_encode($pregunta_respuesta);

// En pantalla
echo $json;
?>


    <!--
        output:
        {"pregunta":"QUe dia es hoy","respuesta":"Miercoles"}
    -->

    <!--
Con este ejercicio aprendí a utilizar matrices con nombre en PHP y a convertir información al formato JSON. Esto es útil porque puedo aplicar la misma idea en la vida real, por ejemplo, para almacenar información sobre formación o recetas. Me ayuda a comprender mejor cómo gestionar datos en PHP y cómo puedo utilizarlos en mi rutina diaria.
    -->