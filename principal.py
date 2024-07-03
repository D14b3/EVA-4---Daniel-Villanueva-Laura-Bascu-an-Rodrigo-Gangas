from conexion import Conexion
from personaje import Personaje
from arma import Arma
Conexion.getConnection()

Personaje().crearPj()
Arma().crearArma()
Personaje().agregarArmaPj()