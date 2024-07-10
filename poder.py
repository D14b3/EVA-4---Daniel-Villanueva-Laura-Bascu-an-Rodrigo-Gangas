import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

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
        sql = "SELECT * FROM poder"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del poder a elegir: ')
        while not id.isdigit():
            id = input('Error, Indique el id del poder a agregar: ')
        sql = "SELECT * FROM poder WHERE idPoder = %s"
        self.mysql.cursor.execute(sql,int(id))
        result = self.mysql.cursor.fetchone()
        if result:
            sql = "UPDATE `personaje` SET idPoder=%s WHERE `idPersonaje`=%s"
            self.mysql.cursor.execute(sql, (int(id), Personaje.idpj))
            self.mysql.connection.commit()
        else:
            print('ID Invalido')            
            time.sleep(2)
            Poder().elegirPoder()

    def modificarPoder(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, PO.nombre FROM PERSONAJE P 
        INNER JOIN Poder PO ON P.idPoder = PO.idPoder"""
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Poder']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del poder a modificar: ')
        sql = "SELECT * FROM PODER"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del poder a agregar: ')
        sql = "UPDATE `personaje` SET idPoder=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idPoder FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)