En este ejercicio utilicé Flask para practicar cómo un servidor web puede leer parámetros de la URL y de un formulario. Es útil en situaciones reales como sistemas de inicio de sesión, formularios de búsqueda o cualquier sitio web que necesite la intervención del usuario.


Creé (utilicé el código proporcionado y lo modifiqué) un servidor Flask y primero comprobé que funcionaba correctamente. Luego lo modifiqué para que pudiera recibir un parámetro llamado «nombre» de la URL utilizando request.args.get(). Después de eso, hice que el programa también recibiera «apellidos» y devolviera un mensaje al navegador utilizando una cadena f que muestra los valores recibidos. El servidor imprime los parámetros en la consola y también los muestra al usuario, por lo que puedo ver fácilmente que Flask está leyendo y manejando los datos correctamente.

# ---------- 1-3 ----------

# ---------- 002-cojo parametro.py ----------


from flask import Flask, request 

app = Flask(__name__)

@app.route("/")
def inicio():
  nombre = request.args.get("nombre")
  print(nombre)
  return "Mira en la consola si ha pasado algo"

if __name__ == "__main__":
  app.run(debug=True)


# ---------- 4 ----------

# ---------- 003-microformulario.py ----------

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("index.html")

@app.route("/envio")
def envio():
  nombre = request.args.get("nombre")
  apellidos = request.args.get("apellidos")
  print(nombre, apellidos)
  return f"Hola {nombre} {apellidos}, tus datos han sido recibidos correctamente"

if __name__ == "__main__":
  app.run(debug=True)


# Devuelvo un mensaje en HTML utilizando una f-string en Python. f"Hola {nombre} {apellidos}..." me permito insertar directamente el valor de las variables dentro del texto. 


Este ejercicio me ayudó a comprender mejor cómo Flask gestiona los parámetros y cómo los datos viajan desde el navegador al servidor. Ahora puedo ver claramente cómo se utiliza esto en aplicaciones web reales cuando los usuarios envían información. En general, fue un buen ejercicio que me ayudó a repasar algunas cosas que había olvidado un poco.