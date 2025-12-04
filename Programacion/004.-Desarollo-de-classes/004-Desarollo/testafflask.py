

#sudo apt install python3-flask
#pip install flask - windows

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
    
        <!doctype html>
        <html>
            <head>
                <title></title>
                <style>
                    h1{color: red;}
                </style>
            </head>
            <body>
                <h1>Esto es HTML a tope de power</h1>
                '''
    for dia in range (1, 31):
        cadena += '<div>'+str(dia)+'</div>'
    
    cadena += '''
            </body>
        </html>
    '''
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True) 