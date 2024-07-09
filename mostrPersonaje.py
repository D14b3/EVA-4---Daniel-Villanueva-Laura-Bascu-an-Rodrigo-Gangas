import pymysql
from conexion import Conexion 
from os import system
import time
import beautifultable as bs


# Lista vacía para almacenar los personajes
personajes = []

class listaPersonaje():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

# Función para generar la tabla
def crearTabla(self) -> None:
    system("cls")
    sql = "SELECT nombre, FROM personaje"
    self.mysql.cursor.execute(sql)
    resultados = self.mysql.cursor.fetchall()
    table = bs.BeautifulTable()
    table.columns.header = ["Nombre",]
    for resultado in resultados:
        table.rows.append([resultado[0]])
    print(table)
    time.sleep(5)

# Menú para elegir la opción de agregar personajes o generar la tabla
while True:
    print("Menú:")
    print("2. Generar tabla de personajes")
    print("3. Salir")
    opcion = input("Elija una opción: ")
    
    if opcion == "2":
        if len(personajes) == 0:
            print("No hay personajes agregados. Agregue personajes primero.")
        else:
            tabla = crearTabla(personajes)
            print(tabla)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
