import mysql.connector 
from flask import Flask
import json

conexion = mysql.connector.connect(
  host="localhost",
  user="tiendaclase",
  password="nykode123",
  database="tiendaclase"
)                                         
app = Flask(__name__)

@app.route("/clientes") #da denne her rute er /clientes, giver terminalen ikke den rigtige rute. Add selv /clientes i browseren
def inicio():
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM clientes;")  

    filas = cursor.fetchall()
    return json.dumps(filas)

if __name__ == "__main__":
    app.run(debug=True, port=5050) 

# http://localhost:5050/clientes
