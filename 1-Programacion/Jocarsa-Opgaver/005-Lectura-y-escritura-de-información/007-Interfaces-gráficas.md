En este ejercicio trabajo con tkinter y Python. Utilizo un contexto sencillo relacionado con el fitness, combinando ir al gimnasio y correr, tal y como pide la tarea. Como estos también son mis hobbies, la tarea resulta más realista. 

 Creo una ventana con tkinter y añado dos campos de entrada donde el usuario puede introducir números. También añado un botón que activa una función cuando se pulsa. La función lee los valores de los campos de entrada, los suma y actualiza una etiqueta con el resultado. Solo utilizo los elementos básicos de tkinter que hemos aprendido en clase.


# ---------- Enunciado paso a paso ----------

import tkinter as tk

def calcular():
    minutos_gym = float(entrada_gym.get())
    km_correr = float(entrada_correr.get())
    total = minutos_gym + km_correr
    resultado.config(text="Total: " + str(total))

ventana = tk.Tk()
ventana.title("Actividad Fitness")

label1 = tk.Label(text="Minutos en el gimnasio")
label1.pack(padx=10, pady=5)

entrada_gym = tk.Entry()
entrada_gym.pack(padx=10, pady=5)

label2 = tk.Label(text="Kilometros corridos")
label2.pack(padx=10, pady=5)

entrada_correr = tk.Entry()
entrada_correr.pack(padx=10, pady=5)

boton = tk.Button(text="Calcular", command=calcular)
boton.pack(padx=10, pady=10)

resultado = tk.Label(text="Total:")
resultado.pack(padx=10, pady=10)

ventana.mainloop()


Este ejercicio muestra cómo se puede utilizar tkinter para crear una interfaz gráfica sencilla con la que el usuario puede interactuar. Utilizo lo que hemos aprendido en clase para el ejemplo realista del fitness, lo que hace que el uso de botones, campos de entrada y etiquetas sea más claro y práctico.