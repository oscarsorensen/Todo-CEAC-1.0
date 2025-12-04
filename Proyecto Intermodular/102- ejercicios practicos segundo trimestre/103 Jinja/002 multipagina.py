from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/sobremi') #for at komme til sobremi, tilføleg /sobremi i url'en
def sobremi():
    return render_template("sobremi.html")

@app.route('/contacto') #for at komme til contacto, tilføleg /contacto i url'en
def contacto():
    return render_template("contacto.html")

if __name__ == '__main__':
    app.run(debug=True)
