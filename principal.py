from conexion import Conexion
from personaje import Personaje
from arma import Arma
from raza import Raza
from habilidad import Habilidad
from poder import Poder
from usuario import Usuario
from equipo import Equipo
from estado import Estado
from beautifultable import BeautifulTable
import time
from os import system

while Usuario().idJugador == 0 and Usuario().idGM == 0:
    table3 = BeautifulTable()
    table3.columns.header = ['Prototipo de Juego de Rol']
    table3.rows.append(['1. Iniciar Sesion'])
    table3.rows.append(['2. Iniciar Sesion GM'])
    table3.rows.append(['3. Registrarse'])
    table3.rows.append(['4. Cerrar'])
    table3.columns.alignment = BeautifulTable.ALIGN_LEFT
    system('cls')
    i = input(f'{table3}\n> ')
    if not i.isdigit() or int(i) < 1 or int(i) > 4:
        system('cls')
        i = input(f'{table3}\n> ')
    elif i == '1':
        system('cls')
        Usuario().login()
    elif i == '2':
        system('cls')
        Usuario().logingm()
    elif i == '3':
        system('cls')
        Usuario().registro()
    elif i == '4':
        system('cls')
        quit()

while Usuario().idJugador != 0 and Usuario().idGM == 0:
    table2 = BeautifulTable()
    table2.columns.header = ['Menu Jugador']
    table2.rows.append(['1. Crear personaje'])
    table2.rows.append(['2. Ver lista de personajes'])
    table2.rows.append(['3. Cerrar'])
    table2.columns.alignment = BeautifulTable.ALIGN_LEFT
    system('cls')
    i = input(f'{table2}\n> ')
    if not i.isdigit() or int(i) < 1 or int(i) > 3:
        system('cls')
        i = input(f'{table2}\n> ')
    
    elif i == '1':
        system('cls')
        Personaje().crearPj()
    elif i == '2':
        system('cls')
        Personaje().mostrarPjs()
    elif i == '3':
        quit()

while Usuario().idGM != 0 and Usuario().idJugador == 0:
    table1 = BeautifulTable()
    table1.columns.header = ['Menu Game Master']
    table1.rows.append(['1. Ver Lista de Personajes'])
    table1.rows.append(['2. Crear Arma'])
    table1.rows.append(['3. Crear Equipo'])
    table1.rows.append(['4. Crear Habilidad'])
    table1.rows.append(['5. Crear Poder'])
    table1.rows.append(['6. Crear Raza'])
    table1.rows.append(['7. Modificar Arma'])
    table1.rows.append(['8. Modificar Equipo'])
    table1.rows.append(['9. Modificar Habilidad1'])
    table1.rows.append(['10. Modificar Habilidad2'])
    table1.rows.append(['11. Modificar Poder'])
    table1.rows.append(['12. Modificar Raza'])
    table1.rows.append(['13. Modificar Nivel'])
    table1.rows.append(['14. Modificar Estado'])
    table1.rows.append(['15. Cerrar'])
    table1.columns.alignment = BeautifulTable.ALIGN_LEFT
    system('cls')
    i = input(f'{table1}\n> ')
    if not i.isdigit() or int(i) < 1 or int(i) > 15:
        system('cls')
        i = input(f'{table1}\n> ')
    
    elif i == '1':
        system('cls')
        Personaje().mostrarPjsGM()
    elif i == '2':
        system('cls')
        Arma().crearArma()
    elif i == '3':
        system('cls')
        Equipo().crearEquipo()
    elif i == '4':
        system('cls')
        Habilidad().crearHabilidad()
    elif i == '5':
        system('cls')
        Poder().crearPoder()
    elif i == '6':
        system('cls')
        Raza().crearRaza()
    elif i == '7':
        system('cls')
        Arma().modificarArma()
    elif i == '8':
        system('cls')
        Equipo().modificarEquipo()
    elif i == '9':
        system('cls')
        Habilidad().modificarHabilidad1()
    elif i == '10':
        system('cls')
        Habilidad().modificarHabilidad2()
    elif i == '11':
        system('cls')
        Poder().modificarPoder()
    elif i == '12':
        system('cls')
        Raza().modificarRaza()
    elif i == '13':
        system('cls')
        Personaje().modificarNivel()
    elif i == '14':
        system('cls')
        Estado().modificarEstado()
    elif i == '15':
        system('cls')
        quit()
