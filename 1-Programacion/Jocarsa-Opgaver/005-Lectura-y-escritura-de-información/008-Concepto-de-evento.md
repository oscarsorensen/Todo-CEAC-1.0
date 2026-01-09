
En este ejercicio, creo una pequeña aplicación relacionada con ir al gimnasio. Utilizo el gimnasio porque hace que la tarea sea más personal. La aplicación sirve para registrar las sesiones de entrenamiento en el gimnasio de mis amigos mediante una interfaz gráfica. Lo hago de forma sencilla utilizando Python con Tkinter y una base de datos MySQL.

Utilizo Tkinter para crear una interfaz gráfica sencilla con etiquetas, campos de entrada y un botón. El usuario puede introducir el nombre, los apellidos y la fecha de entrenamiento. Al pulsar el botón «Registrar», se ejecuta una función que inserta los datos en la base de datos MySQL que he creado. Para ello, utilizo un conector MySQL.

# ---------- Enunciado paso a paso ----------
- Crea la interfaz gráfica, Implementa la funcionalidad de inserción, Prueba tu aplicación
import tkinter as tk
import mysql.connector

conexion = mysql.connector.connect(host="localhost",user="personaltrainor",password="personaltrainor123$",database="gimnasio_info")

cursor = conexion.cursor()
ventana = tk.Tk()

-  Función para registrar la información del cliente. Esto funciona con la base de datos.
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

- Todo funciona correctamente en tkinter. La base de datos también funciona correctamente y guardan los datos. 

Con este ejercicio, utilizo lo que hemos aprendido en clase sobre Tkinter y las conexiones a bases de datos en Python. El programa muestra cómo una interfaz gráfica puede interactuar con una base de datos para almacenar datos reales relacionados con el gimnasio. Esto me ayuda a comprender mejor cómo se pueden utilizar las aplicaciones de Python en situaciones de la vida real.