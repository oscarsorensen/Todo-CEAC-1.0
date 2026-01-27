<?php
	session_start(); 

  if(!isset($_SESSION['idioma'])){

  	$_SESSION['idioma'] = 'es';
  }

  if(isset($_GET['idioma'])){
  
  	$_SESSION['idioma'] = $_GET['idioma'];
  }
	$idioma['es']['inicio'] = "Inicio";
  $idioma['es']['sobremi'] = "Sobre mi";
  $idioma['es']['proyectos'] = "Proyectos";
  $idioma['es']['contacto'] = "Contacto";
  
  $idioma['en']['inicio'] = "Home";
  $idioma['en']['sobremi'] = "About me";
  $idioma['en']['proyectos'] = "Projects";
  $idioma['en']['contacto'] = "Contact";
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Multi idioma</title>
    <meta charset="utf-8">

    <style>
    	body,html{padding:0px;margin:0px;font-family:sans-serif;}
    	header{display:flex;background:black;color:white;
      justify-content:space-between;align-items:center;}
      header a{text-decoration:none;color:inherit;margin:0px 10px;}
      h1{font-size:20px;}
      select{background:none;border:none;}
    </style>

  </head>
  <body>
  	<header>
      <h1>Oscar Sorensen</h1>
      <nav>
        <a href=""><?= $idioma[$_SESSION['idioma']]['inicio'] ?></a>
        <a href=""><?= $idioma[$_SESSION['idioma']]['sobremi'] ?></a>
        <a href=""><?= $idioma[$_SESSION['idioma']]['proyectos'] ?></a>
        <a href=""><?= $idioma[$_SESSION['idioma']]['contacto'] ?></a>
      </nav>

      <select>
        <option value="es" <?php if($_SESSION['idioma'] == 'es'){echo ' selected ';} ?>>🇪🇸</option>
        <option value="en" <?php if($_SESSION['idioma'] == 'en'){echo ' selected ';} ?>>🇬🇧</option>
      </select>
      
    </header>
  </body>
  <script>
  	let selector = document.querySelector("select") // Selecciono el select
    selector.onchange = function(){	// Cuando cambie el selector
    	window.location = "?idioma="+this.value	// Recargo y le paso el idioma en la url
    }
  </script>
</html>