"""
Simple fitness GUI with visible Entry boxes
"""

import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

def calcular():
    try:
        valor1 = entrada1.get()
        valor2 = entrada2.get()

        if valor1 == "" or valor2 == "":
            resultado.config(text="Por favor rellena ambos campos.")
        else:
            total = int(valor1) + int(valor2)
            resultado.config(text="Total de actividad: " + str(total))
    except ValueError:
        resultado.config(text="Introduce solo números.")

ventana = tk.Tk()
ventana.title("App Fitness")
ventana.geometry("300x250")  # force a clear window size

# Campo 1
label1 = tk.Label(ventana, text="Minutos en el gimnasio:")
label1.pack(pady=(15, 5))
entrada1 = tk.Entry(ventana, width=25, bg="white", borderwidth=2)
entrada1.pack(pady=5)

# Campo 2
label2 = tk.Label(ventana, text="Kilómetros corridos:")
label2.pack(pady=5)
entrada2 = tk.Entry(ventana, width=25, bg="white", borderwidth=2)
entrada2.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="Total de actividad: ")
resultado.pack(pady=10)

ventana.mainloop()

