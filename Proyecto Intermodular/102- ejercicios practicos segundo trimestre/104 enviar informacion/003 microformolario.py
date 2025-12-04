from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/envio")
def envio():
    nombre = request.args.get("nombre")
    apellidos = request.args.get("apellidos")
    return "nombre: " + nombre + " apellidos: " + apellidos

if __name__ == "__main__":
    app.run(debug=True, port=5050)