import pymysql
from conexion import Conexion
from os import system
import time

class Raza():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearRaza(self) -> None:
        system('cls')
        nombre = input('Indique el nombre de la raza: ')
        desc = input(f'Indique la descripcion de {nombre}: ')
        sql = "INSERT INTO raza (nombre, descripcion) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, desc))
        self.mysql.connection.commit()
        sql = "SELECT * FROM `raza` WHERE `nombre`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)

    def elegirRaza(self) -> None:
        system('cls')
        id = input('Indique la raza a elegir: ')
        idpj = input('Indique el id del personaje: ')
        sql = "UPDATE `personaje` SET idRaza=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(idpj)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT * FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (idpj))
        result = self.mysql.cursor.fetchone()

        print(result)
        time.sleep(5)