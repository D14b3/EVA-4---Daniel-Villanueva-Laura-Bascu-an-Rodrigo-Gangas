import pymysql.cursors

def CrearPj():
    nombre = input('Indique el nombre del personaje')
    raza = input(f'Indique la raza de {nombre}')
    nivel = 1
    estado = 'vivo'
    
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 database='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `personaje` (`nombrePersonaje`, `raza`, `nivel`, `estado`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, raza, nivel, estado))
            
            connection.commit()
            
            with connection.cursor() as cursor:
                
                sql = "SELECT * FROM `personaje` WHERE `nombrePersonaje`=%s"
                cursor.execute(sql, (nombre))
                result = cursor.fetchone()
                print(result)