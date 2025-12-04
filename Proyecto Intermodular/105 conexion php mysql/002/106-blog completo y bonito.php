<!doctype html>
<html>
	<head>
  </head>
  <body>
  	<header>
    	<h1>Oscar Sorensen</h1>
      <h2>Blog superinteresante de Oscar y no de Jose Vicente (totalmente)</h2>

      <style>

        body {
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f4f4f4;
        }
        header {
          background-color: #35424a;
          color: #ffffff;
          padding: 20px 0;
          text-align: center;
          border-bottom: 6px solid #000;
        }
        main {
          padding: 20px;
        }
        article {
          background-color: #ffffff;
          margin-bottom: 20px;
          padding: 15px;
          border-radius: 5px;
          box-shadow: 0 2px 5px rgba(0,0,0,1);
        }
        article h3 {
          margin-top: 5px;
        }
      </style>

    </header>
    <main>
      <?php

        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $db   = "blogphp";

        $conexion = new mysqli($host, $user, $pass, $db);

        $sql = "SELECT * FROM blog";

        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha'].'</time>
              <p>'.$fila['autor'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }

        $conexion->close();

      ?>
  </main>
  <footer>
  </footer>
  </body>
</html>