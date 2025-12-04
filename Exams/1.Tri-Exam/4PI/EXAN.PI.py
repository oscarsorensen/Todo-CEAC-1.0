"""
En este proyecto uno los conocimientos de tres asignaturas: Bases de Datos, Programación y Lenguajes de Marcas,
para crear una pequeña aplicación web completa que muestra datos reales guardados en MySQL.

El objetivo principal es desarrollar un portafolio digital donde las piezas se vean de forma dinámica en el navegador.
Para conseguirlo, utilizo Flask como servidor web en Python, y mi base de datos desde del Base de Datos examen, portafolioexamen.
Esta base de datos está conectada a mi aplicación CRUD en Python del examen de Programación.

Tambien uso una estructura HTML con CSS interno para el diseño visual. El código HTML y CSS demuestra mi capacidad para crear un diseño limpio y organizado utilizando técnicas modernas de diseño web, como grid y flexbox. Este código proviene del examen de lenguajes de marcas.
Para que las fotos funcionen, creo una carpeta llamada «static» en el mismo directorio que este archivo Python y coloco allí una imagen llamada example.jpg. Esa es la forma más fácil de servir archivos estáticos con Flask.
El resultado final enseña cómo el backend y el frontend trabajan juntos para generar contenido dinámico.


Mientras realizaba esta tarea, utilicé mi aplicación CRUD del examen de programación para demostrar en directo la conexión con la base de datos y que todo funcionaba correctamente. Allí generé el quinto artículo en la base de datos para que, cuando se ejecute esta aplicación web, muestre cinco artículos en lugar de cuatro.
"""


import mysql.connector
from flask import Flask # Importar Flask.

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

#ruta de apertura para la página principal
@app.route("/")
def inicio():
    """
    Consulta los datos desde la vista creada en la base de datos
    y genera dinámicamente la página HTML.
    Podemos ver cómo se modifican los artículos del examen de lenguas de marcas y, de repente, utilizar la información del examen de base de datos.
    """
    cursor.execute("SELECT title, descripcion, categoria_nombre FROM piezasportafolio_con_categoriasportafolio;")
    filas = cursor.fetchall()

    # ------------------- INICIO HTML -------------------
    html = '''
    <!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Oscars Blog</title>
    <style>
      html {
        background: rgb(230, 230, 230);
        font-family: Cambria, Cochin, Georgia, 'Times New Roman', serif;
        font-size: 14px;
      }

      /* --- GRID LAYOUT FOR PAGE STRUCTURE --- */
      body {
        width: 900px;
        margin: auto;
        background: white;
        border-radius: 10px;
        padding: 40px;
        line-height: 1.6;
        display: grid;                         /* simple grid */
        grid-template-rows: auto 1fr auto;      /* header / main / footer */
        gap: 20px;
      }

      header, footer {
        text-align: center;
        border-bottom: 3px solid #ccc;
        padding-bottom: 10px;
      }

      header h1 {
        margin: 0;
        font-size: 30px;

      }

      header h2 {
        margin: 0;
        font-size: 20px;
        color: #555;
      }

      /* --- FLEXBOX FOR ARTICLES --- */
      main {
        display: flex;
        flex-direction: column;      /* artículos apilados verticalmente. Esto demuestra que sé cómo usar flex en una dirección.. */
        gap: 20px;
      }

      article {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 15px;
        display: flex;
        flex-direction: column;      /* contenido apilado en el interior. Esto demuestra que sé cómo utilizar flex en otra dirección. */
        gap: 10px;
      }

      .info {
        display: flex;               /* autor/fecha lado a lado */
        justify-content: space-between;
        font-size: 12px;
        color: #666;
      }

      article img {
        width: 100%;
        border-radius: 6px;
      }

      footer {
        border-top: 1px solid #ccc;
        margin-top: 10px;
        font-size: 12px;
        color: #666;
        text-align: center;
      }
      
    </style>
  </head>

  <body>
    <header>
      <h1>Oscars Blog</h1>
      <h2>My mail - oscar.soerensen@alu.ceacfp.es</h2>
    </header>
    <main>
    '''

    # ------------------- BLOQUES DINÁMICOS -------------------
    for fila in filas:
        html += f'''
          <article>
            <h3>{fila[0]}</h3> <!-- Título desde la base de datos -->
            <p>{fila[1]}</p> <!-- Descripción desde la base de datos -->
            <p><strong>Categoría:</strong> {fila[2]}</p> <!-- Categoría desde la base de datos -->
            <img src="/static/example.jpg" alt="{fila[0]}"> <!-- Imagen de ejemplo -->
          </article>
        '''
#Podemos ver cómo estos artefactos se modifican a partir del examen de lenguajes de marcado y, de repente, utilizan la información del examen de la base de datos. Utilizan títulos, descripciones y nombres de categorías de la vista de la base de datos creada en el examen de la base de datos. Esto demuestra que están correctamente conectados a la base de datos y que nuestra conexión con mySql funciona correctamente.

    # ------------------- FINAL HTML -------------------
    html += '''
    </main>
    <footer>
      <p>Lenguajes de Marcas - ahora Proyecto Intermodular— Examen Trimestral 1 - CEAC 2025</p>
      <p>Oscar Sørensen</p>
    </footer>
  </body>
</html>
    '''
    return html


# Ejecución principal
if __name__ == "__main__":
    app.run(debug=True, port=5050) # Ejecutar en puerto 5050 para evitar conflictos. Antes usué el 5000, y me causó algunos problemas.

"""
Este proyecto demuestra de forma práctica la unión de todas las materias estudiadas durante el trimestre.
La base de datos MySQL, el código en Python con Flask y la estructura HTML con CSS trabajan de manera conjunta
para crear una aplicación web real que muestra contenido dinámico.
El resultado final refleja todo el proceso de desarrollo web: desde la gestión de los datos hasta su presentación visual.

En definitiva, esto demuestra que soy capaz de crear un mini-full stack tras solo un trimestre estudiando estas materias. Ahora puedo crear bases de datos sencillas, organizarlas como quiera y conectarlas a una aplicación backend. Puedo crear programas CRUD sencillos que interactúan con estas bases de datos, y puedo conectar estas bases de datos a una aplicación web dinámica que muestra los datos de forma clara y organizada utilizando HTML y CSS.
Puedo ver fácilmente cómo estas habilidades serán útiles en situaciones reales, y estoy deseando aprender técnicas más avanzadas en el futuro.
"""
