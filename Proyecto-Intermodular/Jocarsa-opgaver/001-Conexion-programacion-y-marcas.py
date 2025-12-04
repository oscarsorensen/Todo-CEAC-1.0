"""
Flask es un microframework de Python. Me permite crear aplicaciones web de forma rápida y sencilla. En este ejercicio, lo utilizo para generar contenido HTML dinámico desde el servidor, simulando una página que muestra los 30 días de un mes. Este ejercicio conecta la programación backend (Python/Flask) con la visualización frontend (HTML y DOM).

El programa comienza importando la librería flask y creando una instancia de la aplicación con Flask(__name__).
A través del decorador @aplicacion.route("/") se define una ruta principal que responde a las solicitudes del navegador.
Dentro de la función raiz(), se construye una cadena HTML que incluye estructura básica (<!doctype html>, <html>, <head>, <body>) y estilos CSS internos.
Mediante un bucle for de Python, se generan de forma dinámica los 30 días del mes con elementos <div>.
Finalmente, la función devuelve toda la cadena HTML al navegador.
El bloque if __name__ == "__main__": permite ejecutar el servidor local en modo debug, mostrando automáticamente los cambios en tiempo real.

"""

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>Días del mes</title>
        <meta charset="utf-8">
        <style>
          body { font-family: sans-serif; background: #f0f0f0; text-align: center; }
          h1 { color: red; }
          div { 
            display: inline-block; 
            margin: 5px; 
            padding: 10px; 
            background: white; 
            border-radius: 6px; 
            box-shadow: 0 0 3px rgba(0,0,0,0.3);
          }
        </style>
      </head>
      <body>
        <h1>Esto es HTML a tope de power</h1>
    '''
    for dia in range(1, 31):
        cadena += f'<div>{dia}</div>'

    cadena += '''
      </body>
    </html>
    '''
    return cadena


if __name__ == "__main__":
    aplicacion.run(debug=True)

"""
Este ejercicio me ayuda a comprender el flujo completo entre el servidor y el cliente utilizando Flask y HTML dinámico.
Esta técnica constituye la base para crear aplicaciones web más complejas, en las que los datos se muestran o actualizan en tiempo real, reforzando la conexión entre el backend de Python y la interfaz visual del usuario.
"""