Contexto

En esta unidad, hemos estado explorando las interfaces gráficas en Python utilizando la biblioteca tkinter. A través de ejercicios prácticos, hemos aprendido cómo crear ventanas, botones y etiquetas, así como cómo manejar eventos para interactuar con el usuario. Hoy, vamos a incorporar nuestros hobbies favoritos: cocinar y ir al gimnasio, en nuestro ejercicio de interfaz gráfica.

Enunciado paso a paso

Crea la ventana principal: Utiliza tkinter para crear una ventana principal donde podrás mostrar los resultados de nuestras actividades.
Añade campos de entrada: Crea dos campos de entrada (Entry) para que el usuario pueda ingresar números, como por ejemplo, los minutos que ha estado en el gimnasio o los kilómetros recorridos al correr.
Botón para calcular: Añade un botón que, cuando se pulse, calcule y muestre la suma de los dos valores ingresados. Por ejemplo, si el usuario ha corrido 5 km y estuvo en el gimnasio durante 40 minutos, el botón mostrará "Total: 45".
Etiqueta para mostrar resultados: Utiliza una etiqueta (Label) para mostrar el resultado de la suma.
Restricciones

Solo puedes usar los conceptos permitidos en la lista blanca.
No uses funciones o métodos que no se hayan enseñado en clase.
Evita utilizar librerías externas o estructuras de datos avanzadas.
Criterios de evaluación

Introducción y contextualización (25%): El ejercicio debe incorporar correctamente los hobbies del usuario en el contexto.
Desarrollo técnico correcto y preciso (25%): El código debe seguir las estructuras y métodos explicados en clase, sin errores sintácticos o lógicos.
Aplicación práctica con ejemplo claro (25%): El ejercicio debe mostrar la creación de una interfaz gráfica funcional que realice cálculos simples basados en los datos ingresados por el usuario.
Cierre/Conclusión enlazando con la unidad (25%): El ejercicio debe finalizar mostrando cómo se ha aplicado lo aprendido en clase y cómo se integra en un contexto real del hobby del usuario.
Instrucciones de salida

El alumnado debe completar este apartado.

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

