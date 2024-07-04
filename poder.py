import pymysql
from conexion import Conexion
from os import system
import time

class Poder():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearPoder(self) -> None:
        system('cls')
        nombre = input('Indique el nombre del poder: ')
        desc = input(f'Indique la descripcion de {nombre}: ')
        sql = "INSERT INTO poder (nombre, descripcion) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, desc))
        self.mysql.connection.commit()
        sql = "SELECT * FROM `poder` WHERE `nombre`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)

    def elegirPoder(self) -> None:
        system('cls')
        id = input('Indique el poder a elegir: ')
        idpj = input('Indique el id del personaje: ')
        sql = "UPDATE `personaje` SET idPoder=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(idpj)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT * FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (idpj))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)