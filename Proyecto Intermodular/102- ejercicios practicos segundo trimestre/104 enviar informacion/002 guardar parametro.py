from flask import Flask, request # Toma parametros para la url


app = Flask(__name__)

@app.route('/')
def inicio():
    nombre = request.args.get('nombre')  # Obtener el parámetro 'nombre' de la URL
    print(nombre)
    return "Mira ele la consola si ha pasado algo"

if __name__ == '__main__':
    app.run(debug=True, port=5050)

#http://127.0.0.1:5050/?nombre=Oscar%Sorensen
#%20 = espacio (en url)