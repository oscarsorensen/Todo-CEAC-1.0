"""
En esta actividad trabajo con una base de datos empresarial que almacena la información de los clientes.
Para evitar la pérdida de datos, realizo copias de seguridad periódicas y automatizadas.
Este proceso garantiza la continuidad del sistema y refleja la importancia de la prevención, igual que mantener una rutina constante en el gimnasio.

Primero establezco la conexión con la base de datos empresarial mediante Python y la librería mysql.connector.
Después utilizo el comando mysqldump para generar una copia de seguridad completa.
Por último, programo el proceso con cron para que se ejecute automáticamente cada día a las 2 a. m.
"""

-- Conexión a la base de datos usando Python
import mysql.connector

-- Datos de conexión
host = "localhost"
user = "usuarioempresarial"
password = "usuarioempresarial"
database = "empresarial"

-- Establecemos la conexión
conexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

-- Crear una carpeta en el escritorio para almacenar las copias de seguridad
mysqldump -u usuarioempresarial -p empresarial > copia_de_seguridad_empresarial.sql
crontab -e

-- Agregar la siguiente línea para programar una copia de seguridad diaria a las 2 AM
0 2 * * * mysqldump -u usuarioempresarial -p'usuarioempresarial' empresarial > /ruta/donde/quieras/almacenar/copia_de_seguridad_empresarial.sql

"""
Realizar y programar copias de seguridad asegura la protección de los datos empresariales y la fiabilidad del sistema.
Gracias a estas tareas, la base de datos se mantiene estable, segura y preparada ante cualquier incidencia.
Este trabajo demuestra la importancia de aplicar hábitos regulares y técnicos en la gestión de información.
"""