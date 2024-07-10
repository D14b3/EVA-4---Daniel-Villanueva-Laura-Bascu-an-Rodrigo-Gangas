DROP DATABASE IF EXISTS rol;
CREATE DATABASE IF NOT EXISTS rol;
USE ROL;
SET GLOBAL FOREIGN_KEY_CHECKS=0;

CREATE TABLE Jugador (
    idJugador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    pwd VARCHAR(25) NOT NULL
);

CREATE TABLE GameMaster (
    idGM INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    pwd VARCHAR(25) NOT NULL
);

CREATE TABLE Raza(
    idRaza INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE Habilidad (
    idHabilidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE Equipo (
    idEquipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE Poder (
    idPoder INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE Arma(
    idArma INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE Personaje (
    idPersonaje INT AUTO_INCREMENT PRIMARY KEY,
    nombrePersonaje VARCHAR(25) NOT NULL,
    nivel INT NOT NULL,
    estado VARCHAR(25) NOT NULL,
    idGM INT,
    idJugador INT,
    idHabilidad1 INT,
    idHabilidad2 INT,
    idEquipo INT,
    idArma INT,
    idPoder INT,
    idRaza INT,
    FOREIGN KEY (idGM) REFERENCES GameMaster(idGM),
    FOREIGN KEY(idArma) REFERENCES Arma(idArma),
    FOREIGN KEY (idJugador) REFERENCES Jugador(idJugador),
    FOREIGN KEY (idHabilidad1) REFERENCES Habilidad(idHabilidad),
    FOREIGN KEY (idHabilidad2) REFERENCES Habilidad(idHabilidad),
    FOREIGN KEY (idEquipo) REFERENCES Equipo(idEquipo),
    FOREIGN KEY (idPoder) REFERENCES Poder(idPoder),
    FOREIGN KEY (idRaza) REFERENCES Raza(idRaza)
);

INSERT INTO GameMaster(nombre, pwd) VALUES ('admin', 'admin');
INSERT INTO Arma(nombre, descripcion) VALUES ('Espada de Luz','Una espada larga con una hoja que irradia una luz intensa y cálida');
INSERT INTO Arma(nombre, descripcion) VALUES ('Martillo de la Tormenta', 'Un martillo macizo con un mango de acero y una cabeza forjada con trozos de relámpagos capturados');
INSERT INTO Arma(nombre, descripcion) VALUES ('Arco de la Luna', 'Un arco elegante hecho de madera de ébano y adornado con runas lunares brillantes');

INSERT INTO Equipo(nombre, descripcion) VALUES ('Armadura del Dragón','Una armadura completa hecha de escamas de dragón plateado');
INSERT INTO Equipo(nombre, descripcion) VALUES ('Anillo de la Llama','Un anillo forjado con un fragmento de un meteorito que arde eternamente');
INSERT INTO Equipo(nombre, descripcion) VALUES ('Botas de la Velocidad','Botas de cuero negro imbuidas con magia de velocidad y silencio');

INSERT INTO Habilidad(nombre, descripcion) VALUES ('Flechas de Hielo', 'Encanta flechas o proyectiles con poderes de hielo, congelando a los enemigos al impactar');
INSERT INTO Habilidad(nombre, descripcion) VALUES ('Cura Curativa', 'Canaliza energía positiva para curar heridas de los aliados cercanos durante un periodo de tiempo');
INSERT INTO Habilidad(nombre, descripcion) VALUES ('Teleportación Rápida', 'Se traslada instantáneamente a un lugar visible a distancia corta, escapando del peligro o alcanzando posiciones estratégicas');
INSERT INTO Habilidad(nombre, descripcion) VALUES ('Tormenta Eléctrica', 'Invoca una tormenta de rayos que golpea a los enemigos con descargas eléctricas, causando daño continuo y aturdiendo a los objetivos');

INSERT INTO Poder(nombre, descripcion) VALUES ('Eclipse Total', 'Sumerge el área circundante en una oscuridad total, cegando a los enemigos y reduciendo su capacidad de atacar y defenderse durante un período prolongado');
INSERT INTO Poder(nombre, descripcion) VALUES ('Avalancha de Tierra', 'Hace que el suelo tiemble y se agriete, provocando una avalancha de rocas y tierra que aplasta a los enemigos y bloquea el paso en un área específica');
INSERT INTO Poder(nombre, descripcion) VALUES ('Furia Divina', 'Invoca la ira de los dioses para lanzar un rayo divino que purifica el mal, eliminando a los enemigos malignos y restaurando la paz en la zona afectada');

INSERT INTO Raza(nombre, descripcion) VALUES ('Humanos', 'Versátiles y adaptables, los humanos son conocidos por su diversidad cultural, habilidades aprendidas rápidamente y capacidades para liderar y formar alianzas');
INSERT INTO Raza(nombre, descripcion) VALUES ('Elfos', 'Elegantes y longevos, los elfos poseen una conexión innata con la naturaleza y la magia. Son conocidos por su gracia, agilidad y habilidades en el arco y la magia arcana');
INSERT INTO Raza(nombre, descripcion) VALUES ('Orcos', 'Fuertes y feroces, los orcos son guerreros natos con una cultura centrada en la fuerza y la lucha. Poseen una gran resistencia física y habilidades en combate cuerpo a cuerpo');
