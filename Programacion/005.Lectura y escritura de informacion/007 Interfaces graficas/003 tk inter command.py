
import tkinter as tk

def accion():
    print("Me has pulsado")

ventana = tk.Tk() #crea una ventana called Name Space.

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10) #crea un boton en la ventana

ventana.mainloop() #no te salgas