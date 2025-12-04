from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    ########### ESTE ES UN BLOQUE
    cadena = '''

<!doctype html>
<html lang="es">
    <head>
        <title>OscarBLOG</title>
        <meta charset="UTF-8">
        <style>
            body{background:steelblue;color:steelblue;font-family:sans-serif;}
            header,main,footer{background:white;padding: 20px;margin:auto;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>
    </head>
    <body>
        <header><h1>OscarBLOG</h1></header>
        <main>
        '''
    ############OTRO BLOQUE
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
            <article>
                <h3>'''+linea['titulo']+'''</h3>
                <time>'''+linea['fecha']+'''</time>
                <p>'''+linea['autor']+'''</p>
                <p>'''+linea['contenido']+'''</p>
            </article>
        '''
    ######## ESTO ES OTRO BLOQUE
    cadena += '''
        </main>
        <footer>
            (c)2025 Oscar Sorensen
        </footer>
    </body>
</html>
    '''
    ######NO OS OLVIDEIS DE RETURN
    return cadena
if __name__ == "__main__":
    aplicacion.run(debug=True)
