En este ejercicio trabajé con Flask, HTML y JavaScript para practicar cómo leer datos de un archivo JSON utilizando la función fetch. Lo hemos hecho muchas veces en clase y tenía mi localhost listo, así que no fue complicado.  La tarea es similar a una situación real en la que necesitamos cargar información desde un servidor, como datos de usuarios, información curricular o cualquier otra información externa que deba aparecer en una página web.

 Creé un archivo JSON con la información personal proporcionada y lo coloqué dentro de la carpeta del proyecto Flask. Luego tomé el index.html y utilicé fetch para solicitar el archivo JSON. Cuando se recibió la respuesta JSON, la convertí en un objeto utilizando .json() y luego inserté los valores dentro de los elementos HTML utilizando innerText. Finalmente, Flask renderiza la página HTML.

# ---------- curriculum.json ----------
{
  "nombre": "Jose Vicente",
  "apellidos": "Carratalá Sanchis",
  "correo": "info@jocarsa.com"
}


# ---------- index.html (Esto estaba dentro /templates) ----------
<!doctype html>
<html lang="es">
  <head>
    <title>Plantilla fetch</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1 id="nombre"></h1>
    <h2 id="apellidos"></h2>
    <h3 id="correo"></h3>
<!--cambio fetch("static/curriculum.json" a fetch("static/curriculum/curriculum.json") para clarificar)
-->
    <script>
        fetch("static/curriculum/curriculum.json") 
        .then(function(respuesta){
          return respuesta.json();
        })
        .then(function(datos){
          document.getElementById('nombre').innerText = datos.nombre;
          document.getElementById('apellidos').innerText = datos.apellidos;
          document.getElementById('correo').innerText = datos.correo;
        });
    </script>
  </body>
</html>


# ---------- microservidor.py ----------
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)


# ---------- Desde servidor Flask ----------
todo funciona correctamente

Este ejercicio me ayudó a practicar cómo una página web puede comunicarse con archivos externos y cómo se pueden cargar datos de forma dinámica. Esto es mucho más fácil que escribir todo manualmente. Muestra directamente lo que hemos aprendido en clase: trabajar con Flask, organizar correctamente un proyecto web y utilizar JavaScript para interactuar con datos.