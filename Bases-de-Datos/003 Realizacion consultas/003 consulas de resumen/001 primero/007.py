import mysql.connector 

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clientes"
)
                                    
  
cursor = conexion.cursor() 
cursor.execute("""
   select 
    round(avg(edad))
from clientes;            

""")  

filas = cursor.fetchall()

print(filas)