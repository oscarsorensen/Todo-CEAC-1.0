from flask import Flask, render_template 

app = Flask(__name__)

mi_nombre = "Oscar" #Needed to pass the variable to the template. Without actually putting the Nombre, the code doesnt run.

@app.route('/')
def variable():
    return render_template("variable.html", nombre=mi_nombre)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
