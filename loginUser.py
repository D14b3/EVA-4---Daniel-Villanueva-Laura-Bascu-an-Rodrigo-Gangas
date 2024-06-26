from beautifultable import BeautifulTable

def crear_formulario_login():
    table = BeautifulTable()

    # Agregamos las columnas del formulario
    table.column_headers = ["Campo", "Valor"]

    # Agregamos las filas del formulario
    table.append_row(["Correo electrónico", ""])
    table.append_row(["Contraseña", ""])

    # Mostramos el formulario en la consola
    print("Formulario de Login")
    print(table)

    # Pedimos al usuario que ingrese sus credenciales
    correo_electronico = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")

    # Verificamos las credenciales (en un sistema real, se debería verificar en una base de datos)
    if correo_electronico == "usuario@example.com" and contrasena == "password":
        print("Login exitoso!")
    else:
        print("Credenciales incorrectas. Intente nuevamente.")
        
if __name__ == "__main__":
    crear_formulario_login()

def crear_formulario_recuperar_contrasena():

    table = BeautifulTable()

    # Agregamos las columnas del formulario
    table.column_headers = ["Campo", "Valor"]

    # Agregamos las filas del formulario
    table.append_row(["Correo electrónico", ""])

    # Mostramos el formulario en la consola
    print("Formulario de Recuperación de Contraseña")
    print(table)

    # Pedimos al usuario que ingrese su correo electrónico
    correo_electronico = input("Ingrese su correo electrónico: ")

    # Verificamos si el correo electrónico existe (en un sistema real, se debería verificar en una base de datos)
    if correo_electronico == "usuario@example.com":
        print("Correo electrónico encontrado. Se enviará un enlace de recuperación de contraseña a su correo electrónico.")

    else:
        print("Correo electrónico no encontrado. Intente nuevamente.")

    # Opción para enviar un enlace de recuperación de contraseña
        print("\n¿Desea enviar un enlace de recuperación de contraseña a su correo electrónico? (s/n)")
        respuesta = input("> ")
    
    if  respuesta.lower() == "s":
        print("Enlace de recuperación de contraseña enviado con éxito.")

    else:
        print("Operación cancelada.")

if __name__ == "__main__":
    crear_formulario_recuperar_contrasena()
