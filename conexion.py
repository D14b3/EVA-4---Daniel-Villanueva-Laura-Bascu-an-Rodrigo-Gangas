import pymysql
import time

class Conexion:
    connection = None
    cursor = None

    def __init__(self):
        pass

    @classmethod
    def getConnection(cls):
        try:
            if cls.connection is None or not cls.connection.open:
                cls.connection = pymysql.connect(host='localhost', port=3306, user='root', password='', db='rol')
                cls.cursor = cls.connection.cursor()

            else:
                None
        except pymysql.Error as e:
            print(f'Error al establecer la conexión: {e}')
            return None

    @classmethod
    def closeConnection(cls):
        try:
            if cls.connection is not None:
                if cls.connection.open:
                    cls.connection.close()
                    print('Se cerró la conexión.')
                else:
                    print('La conexión no está abierta.')
            else:
                print('No hay ninguna conexión establecida.')
        except pymysql.Error as e:
            print(f'Error al cerrar la conexión: {e}')
        finally:
            cls.connection = None
            cls.cursor = None