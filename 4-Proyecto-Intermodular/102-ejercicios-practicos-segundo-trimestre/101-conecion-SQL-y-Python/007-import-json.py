
import mysql.connector
import json

conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="clientes"
)

cursor = conexion.cursor(dicctionary=True) # Aquí se especifica que el cursor devuelva diccionarios
cursor.execute("""
select
nombre as "Nombre del cliente",
apellido as "Apellido del cliente"
edad as "Edad del cliente"
from clientes
order by edad desc;
""")

filas = cursor.fetchall()
resultado_json = json.dumps(filas, ensure_ascii=False, indent=2)
print(resultado_json)