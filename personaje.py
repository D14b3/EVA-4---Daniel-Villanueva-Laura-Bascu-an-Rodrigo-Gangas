import pymysql
from conexion import Conexion
from os import system
import time
from usuario import Usuario
from beautifultable import BeautifulTable


class Personaje():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()
        self.__idpj = 0

    @property
    def idpj(self):
        return self.__idpj

    @property
    def mysql(self):
        return self.__mysql
    
    def crearPj(self) -> None:
        from poder import Poder
        from raza import Raza
        from habilidad import Habilidad
        from arma import Arma
        from equipo import Equipo
        system('cls')
        nombre = input('Indique el nombre del personaje: ')
        nivel = 1
        estado = 'vivo'
        idJugador = Usuario.idJugador
        idGM = 1

        sql = "INSERT INTO `personaje` (`nombrePersonaje`, `nivel`, `estado`, `idJugador`, `idGM`) VALUES (%s, %s, %s, %s, %s)"
        self.mysql.cursor.execute(sql, (nombre, nivel, estado, idJugador, idGM))
        self.mysql.connection.commit()

        sql = 'SELECT * FROM personaje WHERE nombrePersonaje = %s'
        self.mysql.cursor.execute(sql, nombre)
        resultado = self.mysql.cursor.fetchone()
        Personaje.idpj = resultado[0]
        Arma().elegirArma()
        Raza().elegirRaza()
        Poder().elegirPoder()
        Habilidad().elegirHabilidad()
        Equipo().elegirEquipo()
        



    def mostrarPjs(self) -> None:
        system('cls')
        sql = """SELECT P.nombrePersonaje, P.nivel, P.estado, H1.nombre, H2.nombre, E.nombre, A.nombre, PO.nombre, R.nombre FROM PERSONAJE P 
        INNER JOIN HABILIDAD H1 ON P.idHabilidad1 = H1.idHabilidad 
        INNER JOIN HABILIDAD H2 ON P.idHabilidad2 = H2.idHabilidad
        INNER JOIN EQUIPO E ON P.idEquipo = E.idEquipo
        INNER JOIN ARMA A ON P.idArma = A.idArma
        INNER JOIN PODER PO ON P.idPoder = PO.idPoder
        INNER JOIN RAZA R ON P.idRaza = R.idRaza
        WHERE idJugador = %s"""
        self.mysql.cursor.execute(sql, Usuario.idJugador)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['Nombre', 'Nivel', 'Estado', 'Habilidad 1', 'Habilidad 2', 'Equipo', 'Arma', 'Poder', 'Raza']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        time.sleep(3)

    

    def mostrarPjsGM(self) -> None:
        system('cls')
        sql = 'SELECT idJugador, nombre FROM jugador'
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre de usuario']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del usuario: ')
        while not id.isdigit():
            id = input('Indique el id del usuario: ')
        sql = 'SELECT * FROM personaje WHERE idJugador = %s'
        self.mysql.cursor.execute(sql, int(id))
        resultados = self.mysql.cursor.fetchall()
        print('idPersonaje | nombrePersonaje | nivel | estado | idGM | idJugador | idHabilidad1 | idHabilidad2 | idEquipo | idArma | idPoder | idRaza')
        for fila in resultados:
            print(fila)
        time.sleep(5)

    def modificarNivel(self) -> None:
        system('cls')
        sql = "SELECT idPersonaje, nombrePersonaje, nivel FROM PERSONAJE"
        self.mysql.cursor.execute(sql)
        resultados = self.mysql.cursor.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ID', 'Nombre', 'Nivel']
        for fila in resultados:
            table.rows.append(fila)
        print(table)
        id = input('Indique el id del personaje a modificar: ')
        while not id.isdigit():
            id = input('Error. Indique el id del usuario: ')
        nivel = input('Indique el nivel nuevo: ')
        while not nivel.isdigit():
            nivel = input('Error. Indique el nivel nuevo: ')
        sql = "UPDATE `personaje` SET nivel=%s WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(nivel), int(id)))
        self.mysql.connection.commit()
        registrosModificados = self.mysql.cursor.rowcount
        print(f'Registros modificados: {registrosModificados}')
        sql = "SELECT nombrePersonaje, nivel, estado FROM `personaje` WHERE `idPersonaje`=%s"
        self.mysql.cursor.execute(sql, (int(id)))
        result = self.mysql.cursor.fetchone()
        print(result)
        time.sleep(5)