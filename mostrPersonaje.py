from os import system
import beautifultable as bs


# Lista vacía para almacenar los personajes
personajes = []

# Función para generar la tabla
def generar_tabla(self) -> None:
    system("cls")
    sql = "SELECT nombre, FROM personaje"
    self.mysql.cursor.execute(sql)
    resultados = self.mysql.cursor.fetchall()
    table = bs.BeautifulTable()
    table.columns.header = ["Nombre",]
    for resultado in resultados:
        table.rows.append([resultado[0]])
    print(table)

# Creamos un menú para elegir la opción de agregar personajes o generar la tabla
while True:
    print("Menú:")
    print("2. Generar tabla de personajes")
    print("3. Salir")
    opcion = input("Elija una opción: ")
    

    if opcion == "2":
        if len(personajes) == 0:
            print("No hay personajes agregados. Agregue personajes primero.")
        else:
            tabla = generar_tabla(personajes)
            print(tabla)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
