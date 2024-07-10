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

INSERT INTO GameMaster(nombre, pwd) VALUES ('admin', 'admin')