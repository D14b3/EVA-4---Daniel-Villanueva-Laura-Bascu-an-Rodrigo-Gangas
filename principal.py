from conexion import Conexion
from personaje import Personaje
from arma import Arma
from raza import Raza
from habilidad import Habilidad

Conexion.getConnection()

Habilidad().crearHabilidad()
Habilidad().crearHabilidad()
Raza().crearRaza()
Personaje().crearPj()
Arma().crearArma()


Habilidad().elegirHabilidad()
Raza().elegirRaza()
Personaje().elegirArma()