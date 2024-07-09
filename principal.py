from conexion import Conexion
from os import system
from personaje import Personaje
from arma import Arma
from raza import Raza
from habilidad import Habilidad
from poder import Poder
from mostrPersonaje import listaPersonaje

Conexion.getConnection()


Poder().crearPoder()
Habilidad().crearHabilidad()
Habilidad().crearHabilidad()
Raza().crearRaza()
Personaje().crearPj()
Arma().crearArma()
listaPersonaje().crearTabla()


Habilidad().elegirHabilidad()
Raza().elegirRaza()
Personaje().elegirArma()
Poder().elegirPoder()
