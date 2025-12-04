
#importamos libreria
import sqlite3

#nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

#creamos un cursor
cursor = conexion.cursor()




#ejecutamos una sentencia
cursor.execute('''
               insert into clientes values(
                 NULL, 'Jorge','Garcia Lopez','oscar@gmail.com'  
               );
               
               ''')

#Lanzamos la peticion
conecion.commit