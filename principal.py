from conexion import Conexion
from personaje import Personaje
from arma import Arma
from raza import Raza
from habilidad import Habilidad
from poder import Poder

Conexion.getConnection()


Poder().crearPoder()
Habilidad().crearHabilidad()
Habilidad().crearHabilidad()
Raza().crearRaza()
Personaje().crearPj()
Arma().crearArma()
mostrPersonaje().crearTabla()


Habilidad().elegirHabilidad()
Raza().elegirRaza()
Personaje().elegirArma()
Poder().elegirPoder()
