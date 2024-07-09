import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

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
        time.sleep(3)

    def elegirRaza(self) -> None:
        system('cls')
        sql = "SELECT * FROM raza"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique la raza a elegir: ')
        while not id.isdigit():
            id = input('Error, Indique el id de la raza a agregar: ')
        sql = "SELECT * FROM raza WHERE idRaza = %s"
        self.mysql.cursor.execute(sql,int(id))
        result = self.mysql.cursor.fetchone()
        if result:
            sql = "UPDATE `personaje` SET idRaza=%s WHERE `idPersonaje`=%s"
            self.mysql.cursor.execute(sql, (int(id), Personaje.idpj))
            self.mysql.connection.commit()
        else:
            print('ID Invalido')
            time.sleep(2)
            Raza().elegirRaza()


    def modificarRaza(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, R.nombre FROM PERSONAJE P 
        INNER JOIN Raza R ON P.idRaza = R.idRaza"""
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Raza']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la raza a modificar: ')
        sql = "SELECT * FROM RAZA"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la raza a agregar: ')
        sql = "UPDATE `personaje` SET idRaza=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idRaza FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)