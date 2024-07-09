import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

class Equipo():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearEquipo(self) -> None:
        system('cls')
        nombre = input('Indique el nombre del equipo: ')
        desc = input(f'Indique la descripcion de {nombre}: ')
        sql = "INSERT INTO equipo (nombre, descripcion) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, desc))
        self.mysql.connection.commit()
        sql = "SELECT * FROM `equipo` WHERE `nombre`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)

    def elegirEquipo(self) -> None:
        system('cls')
        sql = "SELECT * FROM equipo"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del equipo a elegir: ')
        while not id.isdigit():
            id = input('Error, Indique el id del equipo a elegir: ')
        sql = "SELECT * FROM equipo WHERE idEquipo = %s"
        self.mysql.cursor.execute(sql,int(id))
        result = self.mysql.cursor.fetchone()
        if result:
            sql = "UPDATE `personaje` SET idEquipo=%s WHERE `idPersonaje`=%s"
            self.mysql.cursor.execute(sql, (int(id), Personaje.idpj))
            self.mysql.connection.commit()
            time.sleep(2)
        else:
            print('ID Invalido')
            Equipo().elegirEquipo()

    
    def modificarEquipo(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, E.nombre FROM PERSONAJE P 
        INNER JOIN Equipo E ON P.idEquipo = E.idEquipo"""
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Equipo']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del equipo a modificar: ')
        sql = "SELECT * FROM EQUIPO"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del equipo a agregar: ')
        sql = "UPDATE `personaje` SET idEquipo=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idEquipo FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(2)