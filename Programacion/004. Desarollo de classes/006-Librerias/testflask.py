
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''

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
            <article>
                <h3>Titulo de articulo</h3>
                <time>2025-10-16</time>
                <p>Oscar Sorensen</p>
                <p>Este es el contenido de un articulo ficticio</p>
            </article>

        </main>

    <footer>
        (c)2025 Oscar Sorensen
    </footer>

    </body>

'''

#ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)
