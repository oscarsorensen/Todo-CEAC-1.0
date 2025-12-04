

#importamos libreria
import sqlite3

#nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

#creamos un cursor
cursor = conexion.cursor()


#ejecutamos una sentencia
cursor.execute('''
             select * from clientes;
               
               ''')

filas = cursor.fetchall()

for fila in filas:
    print(fila)

#Lanzamos la peticion
conexion.commit()