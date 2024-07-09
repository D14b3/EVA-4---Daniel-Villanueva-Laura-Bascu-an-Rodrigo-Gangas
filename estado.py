import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

class Estado():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def modificarEstado(self) -> None:
        system('cls')
        sql = "SELECT idpersonaje, nombrepersonaje, nivel, estado FROM personaje"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nivel', 'Estado']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del personaje a modificar: ')
        estado = input('Indique el nuevo estado del personaje: ')
        sql = "UPDATE `personaje` SET estado=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (estado, int(id)))
        self.mysql.connection.commit()
        sql = "SELECT idpersonaje, nombrepersonaje, nivel, estado FROM personaje WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, int(id))
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nivel', 'Estado']
        result = self.mysql.cursor.fetchone()
        table.rows.append(result)
        print(table)
        time.sleep(2)