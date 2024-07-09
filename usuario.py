from conexion import Conexion
import re
import time

class Usuario():
    def __init__(self) -> None:
        Conexion.getConnection()
        self.__mysql = Conexion()
        self.__idJugador = 0
        self.__idGM = 0

    @property
    def mysql(self):
        return self.__mysql
    
    @property
    def idJugador(self):
        return self.__idJugador
    
    @property
    def idGM(self):
        return self.__idGM
    
    def registro(self) -> None:
        nombre = input('Indique el nombre de usuario: ')
        while len(nombre) <= 2:
            print('El nombre debe contener al menos 3 caracteres')
            nombre = input('Indique el nombre de usuario: ')
        pwd = input('Indique la clave: ')
        clave = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{3,}')
        while not clave.match(pwd):
            print('La clave debe contener al menos 6 caracteres, mayuscula, minuscula y un numero.')
            pwd = input('Indique la clave: ')
        sql = "INSERT INTO `jugador` (`nombre`, `pwd`) VALUES (%s, %s)"
        self.mysql.cursor.execute(sql, (nombre, pwd))
        self.mysql.connection.commit()
        print(f'Usuario {nombre} creado con exito')
        time.sleep(3)

    def login(self) -> None:
        nombre = input('Indique el nombre de usuario: ')
        sql = "SELECT * FROM jugador WHERE nombre = %s"
        self.mysql.cursor.execute(sql, nombre)
        resultado = self.mysql.cursor.fetchone()
        if not resultado:
            print('Usuario no encontrado')
            Usuario().login()
        clave = input('Indique la clave: ')
        pwd = resultado[2]
        while pwd != clave:
            print('Clave incorrecta.')
            clave = input('Indique la clave: ')
        Usuario.idJugador = resultado[0]
        print(f'Sesion iniciada como {resultado[1]}')
        time.sleep(3)

    def logingm(self) -> None:
        nombre = input('Indique el nombre de usuario: ')
        sql = "SELECT * FROM gamemaster WHERE nombre = %s"
        self.mysql.cursor.execute(sql, nombre)
        resultado = self.mysql.cursor.fetchone()
        if not resultado:
            print('Usuario no encontrado')
            Usuario().logingm()
        clave = input('Indique la clave: ')
        pwd = resultado[2]
        while pwd != clave:
            print('Clave incorrecta.')
            clave = input('Indique la clave: ')
        Usuario.idGM = resultado[0]
        print(f'Sesion iniciada como {resultado[1]}')
        time.sleep(3)