<!doctype html>
<html>
	<head>
  	<style>
    	html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        background:#0f172a;
        color:#e5e7eb;
        font-family:system-ui,sans-serif;
      }

      body{
        display:flex;
      }

      nav{
        background:#020617;
        padding:20px;
        flex:1;
        display:flex;
        flex-direction:column;
        gap:12px;
        border-right:1px solid #1e293b;
      }

      nav a{
        background:#1e293b;
        color:#93c5fd;
        text-decoration:none;
        padding:10px 14px;
        border-radius:6px;
        transition:background 0.2s,color 0.2s;
      }

      nav a:hover{
        background:#2563eb;
        color:white;
      }

      main{
        padding:20px;
        flex:4;
        overflow:auto;
      }

      table{
        width:100%;
        border-collapse:collapse;
        background:#020617;
        border:1px solid #1e293b;
        border-radius:8px;
        overflow:hidden;
      }

      table td{
        padding:12px;
        border-bottom:1px solid #1e293b;
      }

      table tr:hover{
        background:#1e293b;
      }
    </style>
  </head>
  <body>
    <?php
      // Hide PHP errors only
      ini_set('display_errors', 0);
      error_reporting(0);

      // Primero me conecto a la base de datos
        $host = "localhost";
        $user = "tiendaonlinedamdaw";
        $pass = "Tiendaonlinedamdaw123$";
        $db   = "tiendaonlinedamdaw";

        $conexion = new mysqli($host, $user, $pass, $db);
    ?>

    <nav>
    <?php
      // Ahora lo que quiero es un listado de las tablas en la base de datos
        $resultado = $conexion->query("
          SHOW TABLES;
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
        }
    ?>
    </nav>
    <main>
      <table>
      <?php
      // Y ahora creo los registros de la tabla
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
    </main>
  </body>
</html>
