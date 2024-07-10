import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

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

    

    def elegirArma(self) -> None:
        system('cls')
        sql = "SELECT * FROM ARMA"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        idarma = input('Indique el id del arma a elegir: ')
        while not idarma.isdigit():
            idarma = input('Error, Indique el id del arma a elegir: ')
        sql = "SELECT * FROM arma WHERE idArma = %s"
        self.mysql.cursor.execute(sql,int(idarma))
        result = self.mysql.cursor.fetchone()
        if result:
            sql = "UPDATE `personaje` SET idArma=%s WHERE `idPersonaje`=%s"
            self.mysql.cursor.execute(sql, (int(idarma), Personaje.idpj))
            self.mysql.connection.commit()
        else:
            print('ID Invalido')
            time.sleep(2)
            Arma().elegirArma()

    def modificarArma(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, A.nombre FROM PERSONAJE P 
        INNER JOIN Arma A ON P.idArma = A.idArma"""
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Arma']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del personaje a modificar: ')
        sql = "SELECT * FROM ARMA"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
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
        time.sleep(3)