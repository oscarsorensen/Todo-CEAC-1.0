<?php
    if (isset($_GET['operacion'])) {
        $host = "localhost";
        $user = "usuariomusicstore";
        $pass = "pwmusicstore$";
        $db   = "MyMusicStore";

        $conexion = new mysqli($host, $user, $pass, $db);

        $sql = "
            DELETE FROM productos_musica
            WHERE id = " . $_GET['id'] . "
        ";

        $conexion->query($sql);
        $conexion->close();
    }
?>

<!doctype html>
<html lang="es">
<head>

  	<style>
    	body,html{width:100%;height:100%;font-family:sans-serif;}
      body{display:flex;flex-direction:column;background:lightgrey;
      justify-content:center;align-items:center;}
      header,main,footer{background:white;width:1200px;padding:20px;}
      table{border:2px solid lightgray;padding:10px;width:100%;}
      table td{padding:3px;}
      form{columns:2;}
      form input{padding:10px;margin:10px;width:100%;box-sizing:border-box;}
    </style>
  </head>
  <body>
  	<header>
      <h1>Gestor de productos de música</h1>

    </header>
    <main>
      <!-- INSERT -->
      <?php
if(isset($_POST['nombre'])){   // ikke længere $_POST['id']
    $host = "localhost";
    $user = "usuariomusicstore";
    $pass = "pwmusicstore$";
    $db   = "MyMusicStore";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "
        INSERT INTO productos_musica
        (id, nombre, categoria, marca, anio, precio, web)
        VALUES(
            NULL,
            '".$_POST['nombre']."',
            '".$_POST['categoria']."',
            '".$_POST['marca']."',
            ".$_POST['anio'].",
            ".$_POST['precio'].",
            '".$_POST['web']."'
        );
    ";

    $conexion->query($sql);
    $conexion->close();
}
?>

      <!-- TABLA -->
      <table>
<?php
    $host = "localhost";
    $user = "usuariomusicstore";
    $pass = "pwmusicstore$";
    $db   = "MyMusicStore";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM productos_musica";
    $resultado = $conexion->query($sql);

    while ($fila = $resultado->fetch_assoc()) {
        echo "<tr>";

        foreach ($fila as $clave => $valor) {
            echo "<td>" . $valor . "</td>";
        }

        echo "
            <td>
                <a href='?operacion=eliminar&id=" . $fila['id'] . "'>
                    ❌
                </a>
            </td>
        ";

        echo "</tr>";
    }

    $conexion->close();
?>
</table>

      <!-- FORMULARIO -->
      <form action="?" method="POST">
<?php
    $host = "localhost";
    $user = "usuariomusicstore";
    $pass = "pwmusicstore$";
    $db   = "MyMusicStore";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM productos_musica LIMIT 1";
    $resultado = $conexion->query($sql);

    while ($fila = $resultado->fetch_assoc()) {

        foreach ($fila as $clave => $valor) {

            if ($clave == "id") {
                echo "<input type='hidden' name='id' value=''>";
                continue;
            }

            echo "
                <input 
                    type='text' 
                    name='".$clave."' 
                    placeholder='".$clave."'
                >
            ";
        }
    }

    $conexion->close();
?>
    <input type="submit">
</form>

    </main>
    <footer>
    </footer>
  </body>
</html>
