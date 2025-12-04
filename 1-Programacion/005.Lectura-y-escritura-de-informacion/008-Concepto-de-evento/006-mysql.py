import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam2",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    1,
    "12345678A",
    "Jose Vicente",
    "Carratala Sanchis",
    "info@jocarsa.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()