
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="clientes"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

filas = cursor.fetchall()

print(filas)