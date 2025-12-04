from flask import Flask, render_template 
import mysql.connector

###################################### MYSQL ##########################################
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="portafolioexamen"
)

# --- send tables ---
cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
    tablas.append(fila[0])

# --- send columns from one table ---
cursor2 = conexion.cursor()
cursor2.execute("SHOW COLUMNS IN piezasportafolio;")
columnas = []
filas2 = cursor2.fetchall()
for fila in filas2:
    columnas.append(fila[0])

# --- send content from piezasportafolio_clientes ---
cursor3 = conexion.cursor()
cursor3.execute("SELECT * FROM piezasportafolio_clientes;")
contenido = cursor3.fetchall()

###################################### MYSQL ##########################################

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template(
        "backoffice.html",
        mis_tablas=tablas,
        mis_columnas=columnas,
        mi_contenido=contenido
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
