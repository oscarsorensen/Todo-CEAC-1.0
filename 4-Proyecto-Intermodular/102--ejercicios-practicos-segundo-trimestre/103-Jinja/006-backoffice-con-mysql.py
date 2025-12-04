from flask import Flask, render_template 
import mysql.connector

################### MYSQL #######################
#connecting to a databse i used for an exam. the important thing is to show the tables in "a" database- not the database.
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="portafolioexamen"
)
print("Conexion OK:", conexion.is_connected())


cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
    tablas.append(fila[0])
################### MYSQL #######################

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("backoffice.html", mis_tablas=tablas)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

