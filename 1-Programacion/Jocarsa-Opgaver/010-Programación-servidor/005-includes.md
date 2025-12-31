
En este ejercicio, trabajo con páginas PHP que tienen la misma estructura utilizando archivos de cabecera y pie de página. Creo una nueva página llamada mi_gymnasio.php, reutilizo los archivos cabecera.php y pie.php existentes y añado un nuevo enlace de navegación que llamo "Gimnasio". De esta manera practico la reutilización de código, los enlaces de navegación y la organización de la página.

 Creé el archivo mi_gymnasio.php y utilicé include("cabecera.php") e include("pie.php") para que la página compartiera el mismo diseño que las demás páginas. En el contenido principal añadí el texto necesario: "Aquí solo pongo el contenido de la página del gimnasio". A continuación, actualicé el menú dentro de cabecera.php y añadí un enlace funcional a mi_gymnasio.php con el nombre "Gimnasio". Por último, el título de la página se actualizó a "Jose Vicente Carratala – Mi Gimnasio", tal y como indicaba la tarea. En una situación real, por supuesto, utilizaría mi propio nombre.

# ---------- cabecera.php ----------

<!doctype html>
<html>
  <head>
  	<title>Jose Vicente Carratala - Mi Gimnasio</title>
    <meta charset="utf-8" lang="en">
  </head>
  <body>
    <header>
      <h1>Entranadores Oscar Sjorman Sorensen y Jocarsa</h1>
      <nav>
        <a href="index.php">Inicio</a>
        <a href="mi_gymnasio.php">Gimnasio</a>
        <a href="contacto.php"> Contrata a este entrenador tan bueno</a>
      </nav>
    </header>
    <main>

# ---------- pie.php ----------
    </main>
    <footer>
      (c) Oscar Sorensen
    </footer>
  </body>
</html>

# ---------- mi_gymnasio.php ----------
<?php include("cabecera.php"); ?>
<p>Aquí solo pongo el contenido de la página del gimnasio</p>
<?php include("pie.php"); ?>

# ---------- index.php ----------
<?php include("cabecera.php"); ?>
<p>Bienvenido a la página principal</p>
<?php include("pie.php"); ?>
# ---------- ----------

El código funciona correctamente porque se crea la nueva página, el enlace de navegación funciona y el contenido solo se muestra en la página del gimnasio, al tiempo que se siguen reutilizando el encabezado y el pie de página comunes. Este es un ejercicio que podría implementar fácilmente en un escenario real, si quisiera crear una página web.