"""
En este proyecto uno los conocimientos de tres asignaturas: Bases de Datos, Programación y Lenguajes de Marcas,
para crear una pequeña aplicación web completa que muestra datos reales guardados en MySQL.

El objetivo principal es desarrollar un portafolio digital donde las piezas se vean de forma dinámica en el navegador.
Para conseguirlo, utilizo Flask como servidor web en Python, una base de datos MySQL llamada portafolioexamen
y una estructura HTML con CSS interno para el diseño visual.
El resultado final enseña cómo el backend y el frontend trabajan juntos para generar contenido dinámico.
"""

import mysql.connector
from flask import Flask # Importar Flask. Flask is 

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="portafolioexamen"
)

cursor = conexion.cursor()

# Configuración de la aplicación Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    """
    Consulta los datos desde la vista creada en la base de datos
    y genera dinámicamente la página HTML.
    """
    cursor.execute("SELECT title, descripcion, categoria_nombre FROM piezasportafolio_con_categoriasportafolio;")
    filas = cursor.fetchall()

    # ------------------- INICIO HTML -------------------
    html = '''
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>Portafolio Digital - Proyecto Intermodular</title>
        <style>
          html {
            background: rgb(230,230,230);
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 14px;
          }
          body {
            width: 750px;
            margin: auto;
            background: white;
            border-radius: 10px;
            padding: 20px;
            line-height: 1.6;
          }
          header, footer {
            text-align: center;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
            margin-bottom: 20px;
          }
          header h1 { margin: 0; font-size: 24px; }
          header h2 { margin: 0; font-size: 14px; color: #555; }
          article {
            border-top: 1px solid #ccc;
            padding-top: 10px;
            margin-top: 20px;
          }
          article img {
            width: 100%;
            border-radius: 6px;
          }
          article h3 { margin-bottom: 5px; }
          article p { text-align: justify; }
          footer {
            border-top: 1px solid #ccc;
            font-size: 12px;
            color: #666;
          }
        </style>
      </head>
      <body>
        <header>
          <h1>Portafolio Digital de Oscar Sørensen</h1>
          <h2>Proyecto Intermodular I — CEAC DAW/DAM</h2>
        </header>
        <main>
    '''

    # ------------------- BLOQUES DINÁMICOS -------------------
    for fila in filas:
        html += f'''
          <article>
            <h3>{fila[0]}</h3>
            <p><strong>Categoría:</strong> {fila[2]}</p>
            <p>{fila[1]}</p>
            <img src="/static/example.jpg" alt="{fila[0]}">
          </article>
        '''

    # ------------------- FINAL HTML -------------------
    html += '''
        </main>
        <footer>
          <p>Proyecto Intermodular I — Lenguajes de Marcas y Programación</p>
          <p>Oscar Sørensen — 2025</p>
        </footer>
      </body>
    </html>
    '''
    return html


# Ejecución principal
if __name__ == "__main__":
    app.run(debug=True, port=5050) # Ejecutar en puerto 5050 para evitar conflictos

"""
Este proyecto demuestra de forma práctica la unión de todas las materias estudiadas durante el trimestre.
La base de datos MySQL, el código en Python con Flask y la estructura HTML con CSS trabajan de manera conjunta
para crear una aplicación web real que muestra contenido dinámico.
El resultado final refleja todo el proceso de desarrollo web: desde la gestión de los datos hasta su presentación visual.
"""
