import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)  # Limpiar campo de texto después de agregar
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar los datos
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("GUI APLICACION ")

# Cambiar el color de fondo de la ventana
ventana.config(bg="#FFFF00")  # Color amarillo

# Etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="ɪɴɢʀᴇꜱᴇ ᴜɴ ᴅᴀᴛᴏ ʏ ᴘʀᴇꜱɪᴏɴᴇ ᴀɢʀᴇɢᴀʀ:", bg="#00FFFF")
etiqueta.pack(pady=10)

# Campo de texto para ingresar datos
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón para agregar datos (color de fondo celeste y texto blanco)
boton_agregar = tk.Button(ventana, text="ᴀɢʀᴇɢᴀʀ", command=agregar_dato, bg="#00FFFF", fg="black")
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Botón para limpiar la lista (color de fondo celeste  y texto blanco)
boton_limpiar = tk.Button(ventana, text="ʟɪᴍᴘɪᴀʀ", command=limpiar_lista, bg="#00FFFF", fg="black")
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()