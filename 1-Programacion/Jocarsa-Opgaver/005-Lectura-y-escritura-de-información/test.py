import tkinter as tk
import mysql.connector

conexion = mysql.connector.connect(host="localhost",user="personaltrainor",password="personaltrainor123$",database="gimnasio_info")

cursor = conexion.cursor()
ventana = tk.Tk()

# Función para registrar la información del cliente. Esto funciona con la base de datos.
def registrar():
  cursor.execute('''
    INSERT INTO info
    VALUES(
      NULL,
      "'''+nombre.get()+'''",
      "'''+apellidos.get()+'''",
      "'''+fecha.get()+'''"
    );
  ''')
  conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)

tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)


tk.Label(marco,text="Introduce el fecha de entrenamiento").pack(padx=10,pady=10)
fecha = tk.Entry(marco)
fecha.pack(padx=10,pady=10)


tk.Button(marco,text="Registrar",command = registrar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)

ventana.mainloop()

# Todo funciona correctamente en tkinter. La base de datos también funciona correctamente y guardan los datos. 