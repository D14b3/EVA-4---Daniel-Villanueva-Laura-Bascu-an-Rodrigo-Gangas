import pymysql
from conexion import Conexion
from os import system
import time
from beautifultable import BeautifulTable
from personaje import Personaje

class Habilidad():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def crearHabilidad(self) -> None:
        system('cls')
        nombre = input('Indique el nombre de la habilidad: ')
        desc = input(f'Indique la descripcion de {nombre}: ')
        sql = "INSERT INTO habilidad (nombre, descripcion) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, desc))
        self.mysql.connection.commit()
        sql = "SELECT * FROM `habilidad` WHERE `nombre`=%s"
        self.mysql.cursor.execute(sql, (nombre))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)

    def elegirHabilidad(self) -> None:
        system('cls')
        sql = "SELECT * FROM habilidad"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id1 = input('Indique el id de la primera habilidad a elegir: ')
        while not id1.isdigit():
            id1 = input('Error, Indique el id de la primera habilidad a agregar: ')
        sql = "SELECT * FROM habilidad WHERE idHabilidad = %s"
        self.mysql.cursor.execute(sql,int(id1))
        result = self.mysql.cursor.fetchone()
        if result:
            sql = "UPDATE `personaje` SET idHabilidad1=%s WHERE `idPersonaje`=%s"
            self.mysql.cursor.execute(sql, (int(id1), Personaje.idpj))
            self.mysql.connection.commit()

            system('cls')
            sql = "SELECT * FROM habilidad"
            self.mysql.cursor.execute(sql)
            resultados = self.mysql.cursor.fetchall()
            table = BeautifulTable()
            table.columns.header = ['ID', 'Nombre', 'Descripcion']
            for fila in resultados:
                table.rows.append(fila)
            print(table)
            id2 = input('Indique el id de la segunda habilidad a elegir: ')
            while not id2.isdigit():
                id2 = input('Error, Indique el id de la segunda habilidad a elegir: ')
            while id1 == id2:
                print('La segunda habilidad no puede ser igual que la primera')
                id2 = input('Indique el id de la segunda habilidad a elegir: ')
                while not id2.isdigit():
                    id2 = input('Error, Indique el id de la segunda habilidad a agregar: ')

            sql = "SELECT * FROM habilidad WHERE idHabilidad = %s"
            self.mysql.cursor.execute(sql,int(id2))
            result = self.mysql.cursor.fetchone()
            if result:
                sql = "UPDATE `personaje` SET idHabilidad2=%s WHERE `idPersonaje`=%s"
                self.mysql.cursor.execute(sql, (int(id2), Personaje.idpj))
                self.mysql.connection.commit()
                time.sleep(5)
            else:
                print('ID Invalido, se reinicia la seleccion de habilidades.')
                Habilidad().elegirHabilidad()
                time.sleep(2)
        else:
            print('ID Invalido')
            Habilidad().elegirHabilidad()
            time.sleep(2)


    def modificarHabilidad1(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, H.nombre FROM PERSONAJE P 
        INNER JOIN Habilidad H ON P.idHabilidad1 = H.idHabilidad
        """
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Habilidad']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la habilidad a modificar: ')
        sql = "SELECT * FROM HABILIDAD"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la habilidad a agregar: ')
        sql = "UPDATE `personaje` SET idHabilidad1=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idHabilidad1 FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(2)

    def modificarHabilidad2(self) -> None:
        system('cls')
        sql = """SELECT P.idPersonaje, P.nombrePersonaje, H.nombre FROM PERSONAJE P 
        INNER JOIN Habilidad H ON P.idHabilidad2 = H.idHabilidad
        """
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nombre Habilidad']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la habilidad a modificar: ')
        sql = "SELECT * FROM HABILIDAD"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Descripcion']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id de la habilidad a agregar: ')
        sql = "UPDATE `personaje` SET idHabilidad2=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado, idHabilidad2 FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(2)