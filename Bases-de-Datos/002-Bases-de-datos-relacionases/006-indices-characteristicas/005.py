

#importamos libreria
import sqlite3

#nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

#creamos un cursor
cursor = conexion.cursor()

cursor.execute('''
    create table if not exists "clientes"(
       
    "Identificador" integer,
    "nombre" text,
    "description" text,
    "precio" text,
    primary key("Identificador" AUTOINCREMENT)
          
    );
''')


#ejecutamos una sentencia
cursor.execute('''
               insert into clientes values(
                 NULL, 'Jorge','Garcia Lopez','oscar@gmail.com'  
               );
               
               ''')

#Lanzamos la peticion
conexion.commit()