import tkinter as tk
from tkinter import messagebox

# Función para manejar el envío del formulario
def enviar_formulario():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    email = entry_email.get()
    contraseña = entry_contraseña.get()
    
    if nombre and apellido and email and contraseña:
        messagebox.showinfo("Información", "Formulario enviado correctamente")
        # Aquí se puede añadir el código para manejar los datos del formulario,
        # como guardarlos en una base de datos o enviarlos a un servidor.
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Nuevo Usuario")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Email:").grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(ventana)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contraseña:").grid(row=3, column=0, padx=10, pady=10)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.grid(row=3, column=1, padx=10, pady=10)

# Botón de envío
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
boton_enviar.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
