import pymysql
from conexion import Conexion
from os import system
import time

class Arma():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearArma(self) -> None:
        system('cls')
        nombre = input('Indique el nombre del arma: ')
        desc = input(f'Indique la descripcion de {nombre}: ')

        sql = "INSERT INTO arma (nombre, descripcion) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, desc))
        self.mysql.connection.commit()
        sql = "SELECT idArma, nombre, descripcion FROM `arma` WHERE `nombre`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)