"""
En este ejercicio se integra todo el trabajo previo realizado en las asignaturas de Bases de Datos, Programación y Lenguajes de Marcas para crear una aplicación web funcional.
La finalidad es construir un pequeño portafolio digital que muestre las piezas o proyectos almacenados en la base de datos PortafolioDB, combinando la lógica de servidor desarrollada en Python con Flask y el diseño visual en HTML y CSS.
De esta manera se demuestra cómo los diferentes componentes de un sistema web (base de datos, backend y frontend) pueden comunicarse entre sí para generar contenido dinámico en el navegador.

El proyecto comienza estableciendo una conexión con la base de datos PortafolioDB mediante la librería mysql.connector.
Dentro del archivo Python se define una aplicación Flask que contiene un endpoint principal (@app.route("/")).
Cuando se accede a esa ruta, el programa ejecuta una consulta SQL sobre la vista pieza_con_categoria, que combina la información de las tablas Pieza y Categoria.
Los resultados obtenidos se guardan en una lista de filas y se recorren con un bucle for para generar dinámicamente etiquetas <article> dentro del cuerpo HTML.
La estructura HTML está dividida en tres zonas:

un encabezado estático que muestra los datos fijos del autor,

un cuerpo dinámico con los artículos generados desde la base de datos,

y un pie de página estático.
De esta forma, el código une la lógica de consulta con la presentación visual, reproduciendo el flujo completo de una aplicación web real.

"""
import mysql.connector
from flask import Flask

# Connect to MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="PortafolioDB"
)

cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")                           # Ruta principal
def holamundo():                          
    cursor.execute("SELECT * FROM pieza_con_categoria;")   # Obtener datos
    filas = cursor.fetchall()
    print(filas)                                # Mostrar en terminal

    # Inicio HTML
    cadena = ''' 
    <!doctype html>
<html lang="es">
  <head>
    <title>Examen</title>
    <meta charset="utf-8">
     <style>
      html {
        background: rgb(230, 230, 230);
        font-family: Cambria, Cochin, Georgia, 'Times New Roman', serif;
        font-size: 13px;
      }

      /* --- GRID LAYOUT FOR PAGE STRUCTURE --- */
      body {
        width: 750px;
        margin: auto;
        background: white;
        border-radius: 10px;
        padding: 20px;
        line-height: 1.6;
        display: grid;                         /* simple grid */
        grid-template-rows: auto 1fr auto;      /* header / main / footer */
        gap: 20px;
      }

      header, footer {
        text-align: center;
        border-bottom: 1px solid #ccc;
        padding-bottom: 10px;
      }

      header h1 {
        margin: 0;
        font-size: 24px;
      }

      header h2 {
        margin: 0;
        font-size: 14px;
        color: #555;
      }

      /* --- FLEXBOX FOR ARTICLES --- */
      main {
        display: flex;
        flex-direction: column;      /* articles stacked vertically */
        gap: 20px;
      }

      article {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 15px;
        display: flex;
        flex-direction: column;      /* content stacked inside */
        gap: 10px;
      }

      .info {
        display: flex;               /* author/date side by side */
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

    # Parte repetitiva
    # Parte repetitiva
    for fila in filas:
        cadena += f'''
          <article>
            <h3>{fila[0]}</h3>  <!-- titulo -->
            <div class="info">
              <p><strong>Autor:</strong> Oscar Sørensen</p>
              <p><strong>Fecha:</strong> 06/11/2025</p>
            </div>
            <img src="/static/example.jpg" alt="{fila[0]}">  <!-- imagen -->
            <p>{fila[1]}</p>  <!-- descripcion -->
            <p><strong>Categoría:</strong> {fila[2]}</p> <!-- categoria -->
          </article>
        '''


    # Final HTML
    cadena += ''' 
    </main>
    <footer>
      <p>(c) This is a copyrighted message</p>
      <p>Lenguajes de Marcas</p>
    </footer>
  </body>
</html>
  '''
    return cadena

if __name__ == "__main__":
    app.run(debug=True)


"""
La práctica muestra de manera clara cómo combinar conocimientos de distintas áreas para construir un proyecto web completo.
La conexión a MySQL, el uso de Flask y la plantilla HTML CSS trabajan conjuntamente para transformar datos almacenados en la base de datos en páginas visibles en el navegador.
Este ejercicio refleja el mismo proceso que se utiliza en entornos profesionales de desarrollo web, donde el backend y el frontend cooperan para ofrecer contenido dinámico y estructurado.
"""