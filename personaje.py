import pymysql
from conexion import Conexion
from os import system
import time

class Personaje():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearPj(self) -> None:
        system('cls')
        nombre = input('Indique el nombre del personaje: ')
  
        nivel = 1
        estado = 'vivo'

        sql = "INSERT INTO `personaje` (`nombrePersonaje`, `nivel`, `estado`) VALUES (%s, %s, %s)"
        self.mysql.cursor.execute(sql, (nombre, nivel, estado))
        self.mysql.connection.commit()
        sql = "SELECT idPersonaje, nombrePersonaje, nivel, estado FROM `personaje` WHERE `nombrePersonaje`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)


    def elegirArma(self) -> None:
        system('cls')
        id = input('Indique el id del personaje a modificar: ')
        idarma = input('Indique el id del arma a agregar: ')
        sql = "UPDATE `personaje` SET idArma=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(idarma), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idArma, idRaza FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)
