"""
En esta actividad, creo una aplicación web sencilla utilizando Flask como servidor, HTML como lenguaje de presentación y JSON como fuente de datos.
El objetivo es mostrar mi información personal en forma de currículum vitae (CV), integrando los conocimientos de programación web adquiridos en el curso Proyecto Intermodular.
Esto demuestra cómo un archivo JSON puede servir como base de datos local, cuyos valores se envían dinámicamente a una plantilla HTML utilizando Flask.

Primero se define un archivo curriculum.json que contiene los datos personales, la experiencia, la formación y los hobbies del alumno.
A continuación, el script curriculum.py abre este archivo con Python, lo interpreta usando la librería json y lo pasa a una plantilla HTML mediante la función render_template().
En la carpeta templates, el archivo curriculum.html utiliza las etiquetas Jinja2 ({{variable}}) para insertar dinámicamente la información en la página.
Por último, al ejecutar el servidor Flask, el usuario puede visualizar su currículum visitando la dirección http://127.0.0.1:5000/.

"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def curriculum():
    f = open("curriculum.json", "r", encoding="utf-8")
    datos = json.load(f)
    f.close()
    personales = datos["datos personales"]
    return render_template("curriculum.html",
        nombre=personales["nombre"],
        apellidos=personales["apellidos"],
        email=personales["email"],
        telefono=personales["telefono"],
        direccion=personales["direccion"],
        codigo_postal=personales["codigo_postal"],
        experiencia=datos["experiencia"],
        formacion=datos["formacion"],
        hobbies=datos["hobbies"]
    )

if __name__ == "__main__":
    app.run(debug=True)



"""
La práctica demuestra cómo combinar Python, Flask y HTML para generar contenido web dinámico a partir de un archivo JSON.
Este ejercicio permite comprender la comunicación entre el backend y el frontend, y sirve como base para desarrollar aplicaciones más complejas, como portafolios o blogs personales.
"""