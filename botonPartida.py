from beautifultable import BeautifulTable

def crear_menu_inicio():
    table = BeautifulTable()

    # Agregamos las columnas del menú
    table.column_headers = ["Opción", "Descripción"]

    # Agregamos las filas del menú
    table.append_row(["Iniciar Partida", "Comienza una nueva partida"])
    table.append_row(["Salir", "Cierra el programa"])

    # Mostramos el menú en la consola
    print("Menú de Inicio")
    print(table)

    # Pedimos al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Iniciar partida
        print("Iniciando partida...")
  
    elif opcion == "2":
        # Salir
        print("Adiós!")
        exit()
    else:
        print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    crear_menu_inicio()
