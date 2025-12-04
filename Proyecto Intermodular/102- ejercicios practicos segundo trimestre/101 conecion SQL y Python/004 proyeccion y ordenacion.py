
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="clientes"
)

cursor = conexion.cursor()
cursor.execute("""
select
nombre as "Nombre del cliente",
apellido as "Apellido del cliente"
edad as "Edad del cliente"
from clientes
order by edad desc;
""")

filas = cursor.fetchall()

print(filas)