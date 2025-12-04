import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

tk.Label(marco,text="Introduce el nombre del cliente:").pack(padx=10, pady=10)



marco.pack(padx=10, pady=10)

ventana.mainloop()