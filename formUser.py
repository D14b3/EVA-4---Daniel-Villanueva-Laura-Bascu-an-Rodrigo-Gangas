from beautifultable import BeautifulTable

def crear_formulario_usuario():
    table = BeautifulTable()

    # Agregamos las columnas del formulario
    table.column_headers = ["Campo", "Valor"]

    # Agregamos las filas del formulario
    table.append_row(["Nombre", ""])
    table.append_row(["Apellido", ""])
    table.append_row(["Correo electrónico", ""])
    table.append_row(["Contraseña", ""])
    table.append_row(["Confirmar contraseña", ""])

    # Mostramos el formulario en la consola
    print(table)

if __name__ == "__main__":
    crear_formulario_usuario()
