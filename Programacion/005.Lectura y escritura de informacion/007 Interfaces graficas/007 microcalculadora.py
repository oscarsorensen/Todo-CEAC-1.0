import tkinter as tk


ventana = tk.Tk() #crea una ventana called Name Space.

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular")
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado:")
resultado.pack(padx=10,pady=10)

ventana.mainloop() #no te salgas
