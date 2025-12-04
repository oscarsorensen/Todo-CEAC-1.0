




import sqlite3


conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor()

nombre = input("Introduce el nombre")
apellidos = input("Introduce el apellidos")
email = input("Introduce el email")



cursor.execute("""
               insert into clientes values(
                 NULL, '""" + nombre + """','""" + apellidos + """','""" + email + """'
               );
               """)


conexion.commit()

cursor.execute(
    '''select * from clientes;'''
)

filas = cursor.fetchall()

for fila in filas:
    print(fila)
