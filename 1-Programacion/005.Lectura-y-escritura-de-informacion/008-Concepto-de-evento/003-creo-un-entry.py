
import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

#using dninie, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el dninie del cliente:").pack(padx=10, pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10, pady=10)

#using nombre, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10, pady=10)

#using apellidos, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el apellidos del cliente:").pack(padx=10, pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10, pady=10)

#using email, because its in our database in SQL. Thats what we are linking to know.
tk.Label(marco,text="Introduce el email del cliente:").pack(padx=10, pady=10)
email = tk.Entry(marco)
email.pack(padx=10, pady=10)

#all of these arent actually linked to the database yet, but they will be soon i think. Right now its just for show and data.

marco.pack(padx=10, pady=10)

ventana.mainloop()