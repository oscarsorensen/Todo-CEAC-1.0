<!doctype html>
<html>
	<head>
        <style>
            	body,html{width:100%;height:100%;padding:0px;margin:0px;}
                body{display:flex;align-items:center;justify-content:center;background: lightgray; flex-direction:column;}
                header,footer,main{
                    width:400px;padding:20px;background:white;text-align:center;}
                form{display:flex;flex-direction:column; gap:10px;}
                input{padding:10px;}
        </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
        <form action="?" method="POST">
            <label for="pregunta">Escribe tu pregunta:</label>
            <input type="text" name="pregunta" id="pregunta">
            <label for="respuesta">Escribe tu respuesta:</label>
            <input type="text" name="respuesta" id="respuesta">
            <input type="submit">
        </form>
    </main>
    <footer>
        (c) Oscar Sorensen 2025
        <?php
      	echo $_POST['pregunta'];
        echo "<br>";
        echo $_POST['respuesta'];
      ?>
    </footer>
  </body>
</html>