"""
Flask es un microframework de Python que se utiliza para crear aplicaciones web de forma rápida y sencilla.
En este ejercicio, utilizo Flask junto con el módulo JSON para crear un servidor de blogs sencillo.
El objetivo es cargar los datos de los artículos desde un archivo JSON y mostrarlos dinámicamente en formato HTML.

El programa comienza importando las bibliotecas necesarias: Flask y json.
A continuación, se crea una instancia de la aplicación Flask con Flask(__name__).
Se define una ruta principal (@app.route("/") para gestionar las solicitudes del navegador.
Dentro de la función de ruta, el programa abre y lee blog.json, cargando su contenido en una lista Python con json.load().
Mediante un bucle for, crea dinámicamente una cadena HTML para cada artículo, insertando su título, fecha, autor y contenido.
Por último, la página HTML completa se devuelve al navegador utilizando render_template_string().

"""

# Importo las librerías necesarias: Flask para el servidor web y json para leer los artículos
from flask import Flask, render_template_string
import json



#todo este es de la tarea
app = Flask(__name__)

@app.route("/")
def raiz():
    # Carga los artículos desde el archivo JSON
    with open("blog.json", "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)
    
    # Genera el HTML dinámico con los artículos
    cadena = '''
    <!doctype html>
    <html lang="es">
      <head>
        <title>JOCARSAblog</title>
        <meta charset="utf-8">
        <style>
          body { background: steelblue; color: steelblue; font-family: sans-serif; }
          header, main, footer { background: white; padding: 20px; margin: auto; width: 600px; }
          header, footer { text-align: center; }
          main { color: black; }
          article { border-bottom: 1px solid #ccc; margin-bottom: 15px; padding-bottom: 10px; }
          h3 { margin-bottom: 5px; }
          time, p { margin: 3px 0; }
        </style>
      </head>
      <body>
        <header><h1>JOCARSAblog</h1></header>
        <main>
    '''
    
    for linea in contenido:
        cadena += f'''
          <article>
            <h3>{linea['titulo']}</h3>
            <time>{linea['fecha']}</time>
            <p><strong>{linea['autor']}</strong></p>
            <p>{linea['contenido']}</p>
          </article>
        '''
    
    cadena += '''
        </main>
        <footer>(c)2025 Jose Vicente Carratalá</footer>
      </body>
    </html>
    '''
    
    return render_template_string(cadena)

if __name__ == "__main__":
    app.run(debug=True)

"""
Este ejercicio muestra cómo se puede utilizar Flask en situaciones reales, como la gestión de un blog de fitness o cocina en el que los artículos, rutinas o recetas se almacenan en formato JSON y se muestran automáticamente en una página web.
Conecta la programación del backend con una interfaz visual, demostrando cómo los datos de contextos cotidianos pueden transformarse en un sitio web funcional y dinámico.
"""