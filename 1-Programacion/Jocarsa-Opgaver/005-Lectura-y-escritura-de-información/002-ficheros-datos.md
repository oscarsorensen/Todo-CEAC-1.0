<!doctype html>
<html lang='es'>
  <head>
    <title>JOCARSAblog</title>
    <meta charset='utf-8'>
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
    </style>
  </head>
  <body>
    <header><h1>JOCARSAblog</h1></header>
    <main>
      <article>
        <h2>Primer artículo</h2>
        <p><em>2025-10-16 - Jose Vicente Carratala</em></p>
        <p>Este es el contenido del primer artículo</p>
      </article>
      <article>
        <h2>Segundo artículo</h2>
        <p><em>2025-10-17 - Jose Vicente Carratala</em></p>
        <p>Este es el contenido del segundo artículo</p>
      </article>
    </main>
    <footer>(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>

[
    {
      "titulo": "Primer artículo",
      "fecha": "2025-10-16",
      "autor": "Jose Vicente Carratala",
      "contenido": "Este es el contenido del primer artículo"
    },
    {
      "titulo": "Segundo artículo",
      "fecha": "2025-10-17",
      "autor": "Jose Vicente Carratala",
      "contenido": "Este es el contenido del segundo artículo"
    }
  ]


  """En esta actividad aplico los conocimientos de lectura y escritura de información en Python utilizando el formato JSON para los datos y HTML para la presentación.
El contexto se centra en José Vicente, un programador al que le apasiona el gimnasio y la cocina saludable, que desea crear un blog sencillo donde compartir sus recetas y rutinas de entrenamiento.
A través de este ejercicio aprendo a conectar el manejo de ficheros con una aplicación práctica cercana a la programación web, transformando datos estructurados en una página visible en el navegador."""

"""El programa utiliza la librería estándar json para abrir y cargar el archivo blog.json mediante json.load(), convirtiendo su contenido en una lista de diccionarios.
Después, el script abre el archivo blog.html en modo escritura y genera la estructura completa de una página web con etiquetas HTML básicas.
Dentro del cuerpo de la página se recorre la lista contenido_blog con un bucle for, escribiendo para cada artículo su título, fecha, autor y contenido dentro de un bloque <article>.
El código finaliza cerrando correctamente el fichero y mostrando un mensaje de confirmación en la consola."""

import json

archivo_json = "blog.json" #this file is in "La Raiz del proyecto"
archivo_html = "blog.html" #this file is in  "La Raiz del proyecto"
contenido_blog = []

# Read JSON
f = open(archivo_json, "r", encoding="utf-8") # Open JSON file for reading. UTF-8 encoding to support special characters
contenido_blog = json.load(f) # Loading JSON content into the Python object
f.close()

# Writing HTML
f = open(archivo_html, "w", encoding="utf-8")

f.write("<!doctype html>\n")
f.write("<html lang='es'>\n")
f.write("  <head>\n")
f.write("    <title>JOCARSAblog</title>\n")
f.write("    <meta charset='utf-8'>\n")
f.write("    <style>\n")
f.write("      body{background:steelblue;color:steelblue;font-family:sans-serif;}\n")
f.write("    </style>\n")
f.write("  </head>\n")
f.write("  <body>\n")
f.write("    <header><h1>JOCARSAblog</h1></header>\n")
f.write("    <main>\n")

for articulo in contenido_blog: # Loop through articles
    f.write("      <article>\n")
    f.write("        <h2>" + articulo["titulo"] + "</h2>\n")
    f.write("        <p><em>" + articulo["fecha"] + " - " + articulo["autor"] + "</em></p>\n")
    f.write("        <p>" + articulo["contenido"] + "</p>\n")
    f.write("      </article>\n")

f.write("    </main>\n")
f.write("    <footer>(c)2025 Jose Vicente Carratalá</footer>\n")
f.write("  </body>\n")
f.write("</html>\n")
f.close()

print("Blog generado correctamente.")


"""Con este ejercicio he aprendido a leer información estructurada desde un archivo JSON y a transformarla en contenido HTML mediante la escritura de ficheros en Python.
Este proceso me ayuda a comprender cómo se combinan los datos y la presentación dentro de un mismo proyecto, un concepto que será fundamental para desarrollar aplicaciones web más completas en el Proyecto Intermodular, como un blog o gestor de contenidos personales."""