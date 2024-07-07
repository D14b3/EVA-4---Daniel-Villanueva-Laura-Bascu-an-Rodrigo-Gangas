import beautifultable as bs

# Lista vacía para almacenar los personajes
personajes = []

# Función para agregar personajes a la lista
def agregar_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    descripcion = input("Ingrese la descripción del personaje: ")
    personaje = {"nombre": nombre, "descripcion": descripcion}
    personajes.append(personaje)

# Función para generar la tabla
def generar_tabla(personajes):
    table = bs.BeautifulTable()
    table.columns.header = ["Nombre", "Descripción"]
    for personaje in personajes:
        table.rows.append([personaje["nombre"], personaje["descripcion"]])
    return table

# Creamos un menú para elegir la opción de agregar personajes o generar la tabla
while True:
    print("Menú:")
    print("1. Agregar personaje")
    print("2. Generar tabla de personajes")
    print("3. Salir")
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        agregar_personaje()
    elif opcion == "2":
        if len(personajes) == 0:
            print("No hay personajes agregados. Agregue personajes primero.")
        else:
            tabla = generar_tabla(personajes)
            print(tabla)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
