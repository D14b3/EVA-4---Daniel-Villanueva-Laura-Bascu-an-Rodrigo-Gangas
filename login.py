import tkinter as tk
from tkinter import messagebox

# Función para manejar el inicio de sesión
def iniciar_sesion():
    email = entry_email.get()
    contraseña = entry_contraseña.get()
    
    # Aquí puedes agregar la lógica para verificar las credenciales del usuario,
    # por ejemplo, comprobándolas contra una base de datos.
    if email == "usuario@example.com" and contraseña == "1234":
        messagebox.showinfo("Inicio de sesión exitoso", "Bienvenido, has iniciado sesión correctamente")
    else:
        messagebox.showerror("Error de inicio de sesión", "Correo electrónico o contraseña incorrectos")

# Función para abrir la ventana de recuperación de contraseña
def abrir_recuperar_contraseña():
    ventana_recuperar = tk.Toplevel(ventana)
    ventana_recuperar.title("Recuperar Contraseña")

    tk.Label(ventana_recuperar, text="Email:").grid(row=0, column=0, padx=10, pady=10)
    entry_recuperar_email = tk.Entry(ventana_recuperar)
    entry_recuperar_email.grid(row=0, column=1, padx=10, pady=10)

    def recuperar_contraseña():
        email = entry_recuperar_email.get()
        
        # Aquí puedes agregar la lógica para manejar la recuperación de la contraseña,
        # como enviar un correo electrónico de recuperación.
        if email:
            messagebox.showinfo("Recuperación de Contraseña", "Se ha enviado un enlace de recuperación a tu correo electrónico.")
            # Aquí puedes añadir el código para enviar el correo de recuperación
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa tu correo electrónico.")
    
    boton_recuperar = tk.Button(ventana_recuperar, text="Recuperar Contraseña", command=recuperar_contraseña)
    boton_recuperar.grid(row=1, column=0, columnspan=2, pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Inicio de Sesión")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Email:").grid(row=0, column=0, padx=10, pady=10)
entry_email = tk.Entry(ventana)
entry_email.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

# Botón de inicio de sesión
boton_iniciar = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar.grid(row=2, column=0, columnspan=2, pady=10)

# Botón para abrir el formulario de recuperación de contraseña
boton_olvido = tk.Button(ventana, text="Olvidé mi Contraseña", command=abrir_recuperar_contraseña)
boton_olvido.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
