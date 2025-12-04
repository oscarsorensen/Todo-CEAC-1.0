
#Dette virker kun med cv.json og cv.html i samme "raiz" mappen. Altsa i Todo-CEAC mappen. Flyt de to filer og kør scriptet igen.
from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def cv():
    with open("cv.json", encoding="utf-8") as f:
        data = json.load(f)
    dp = data["datos_personales"]
    
    with open ("cv.html", encoding="utf-8") as f:
        html = f.read()
        
    return render_template_string(html, **dp)

if __name__ == "__main__":
    app.run(debug=True)