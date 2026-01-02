
En este ejercicio, creo un pequeño panel de control para una aplicación web. Creo una barra de navegación lateral desde la que se puede acceder a las diferentes secciones del panel. Utilizo mis aficiones porque imagino que los enlaces a rutinas de entrenamiento o recetas de cocina podrían ser prácticos en el futuro.
Primero, he creado una variable llamada enlaces, que almacena una matriz con los nombres de los enlaces de navegación. A continuación, he creado la función generarNavegacion(enlaces), que recorre la matriz y genera una lista HTML sin ordenar con cada enlace dentro de un elemento de la lista. Por último, llamo a la función y muestro la navegación en el panel utilizando solo PHP y HTML, que he aprendido en esta unidad.

<?php
// -------- 1 Variable con enlaces ----------
$enlaces = array(
    "Inicio",
    "Usuarios",
    "Rutinas de gimnasio",
    "Recetas",
    "Contacto"
);

// -------- 2 Funcion para navegación, con enlaces ----------

function generarNavegacion($enlaces){ //hago una función que reciba la array
    $html = "<ul>";  //inicio de la lista unordered
    foreach($enlaces as $enlace){  //recorro la array
        $html .= "<li><a href='#'>$enlace</a></li>";
    }
    $html .= "</ul>"; //cierre de la lista
    return $html; //devuelvo el html generado
}
// -------- 3 muestralo ----------

echo generarNavegacion($enlaces);

?>

Este ejercicio me ha ayudado a comprender mejor cómo crear y generar HTML utilizando PHP y cómo organizar fácilmente una página web. Además, conecta lo que estamos aprendiendo con situaciones reales, ya que podría utilizar esta idea en futuros proyectos o para crear páginas relacionadas con mis intereses personales, como rutinas de gimnasio o una página web con mis recetas de cocina personales.