#importo librerias flask para creer webs
from flask import Flask, render_template #cargar archivos html
import json

#creo nueva aplicacion 
app = Flask(__name__)

#escucho la ruta raiz
@app.route('/')
def inicio():
    #y renderia el archivo index.html
    return render_template("index.html")

#si este archivo no es una libreria y es el principal
if __name__ == '__main__':
    #pon el marca en marcha el servidor
    app.run(debug=True)
