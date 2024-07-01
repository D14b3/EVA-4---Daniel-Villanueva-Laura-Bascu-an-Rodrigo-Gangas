import pymysql.cursors
import pymysql
from conexion import Conexion


class Personaje():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearPj(self)-> None:
        nombre = input('Indique el nombre del personaje: ')
        raza = input(f'Indique la raza de {nombre}: ')
        nivel = 1
        estado = 'vivo'

        sql = "INSERT INTO `personaje` (`nombrePersonaje`, `raza`, `nivel`, `estado`) VALUES (%s, %s, %s, %s)"
        self.mysql.cursor.execute(sql, (nombre, raza, nivel, estado))
        self.mysql.connection.commit()
        sql = "SELECT nombrePersonaje, raza, nivel, estado FROM `personaje` WHERE `nombrePersonaje`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)