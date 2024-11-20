CREATE DATABASE IF NOT EXISTS example;
USE example;

/*--------------- CREATE TABLE ReservationStatus ---------------*/
CREATE TABLE IF NOT EXISTS ReservationStatus(
	statusID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20) UNIQUE NOT NULL,
	description VARCHAR(100) DEFAULT ''
);

INSERT INTO ReservationStatus(name, description)
VALUES ('En espera', 'el cliente no ha confirmado');


INSERT INTO ReservationStatus(name)
VALUES ('confirmada');

INSERT INTO ReservationStatus(name)
VALUES ('Cancelada');


/*--------------- CREATE TABLE Block ---------------*/
CREATE TABLE IF NOT EXISTS Block(
	blockID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(10) UNIQUE NOT NULL,
	address VARCHAR(50) UNIQUE NOT NULL,
	levels INT,
	has_elevator BOOLEAN DEFAULT FALSE
);
/*--------------- CREATE TABLE Owner ---------------*/
CREATE TABLE IF NOT EXISTS Owner(
	ownerID INT PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	lastName VARCHAR(30) NOT NULL,
	birthday DATE
);

/*--------------- CREATE TABLE TypeCommonSpace ---------------*/
CREATE TABLE IF NOT EXISTS TypeCommonSpace(
	typeID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(300) NOT NULL
);

INSERT INTO TypeCommonSpace(name, description)
VALUES('Parques', 'Espacios comunes abiertos y con juegos para niños');

INSERT INTO TypeCommonSpace(name, description)
VALUES('Espacio Social', 'Espacios en donde se pueden hacer reuniones privadas');

INSERT INTO TypeCommonSpace(name, description)
VALUES('Espacio deportivo', 'Canchas, gimnasios o cualquier lugar para hacer deporte');


/*--------------- CREATE TABLE Service ---------------*/
CREATE TABLE IF NOT EXISTS Service(
	serviceID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	cost INT NOT NULL,
	description VARCHAR(300) DEFAULT ''
);


INSERT INTO Services(name, cost)
VALUES('plomeria', 10000);

INSERT INTO Services(name, cost, description)
VALUES('Alquiler Cancha', 20000, 'Alquiler de hora de una cancha deportiva de los espacios comunes');

/*---------- CREATE TABLE CommonSpaces ---------------*/
CREATE TABLE IF NOT EXISTS CommonSpace(
	commonSpaceID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	dimensions VARCHAR(30),
	descrption VARCHAR(300) NOT NULL,
	typeSpaceFK INT,
	FOREIGN KEY (typeSpaceFK) REFERENCES TypeCommonSpace(typeID)
);


/*---------- CREATE TABLE Apartment ---------------*/
CREATE TABLE IF NOT EXISTS Apartment(
	apartmentID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	area DECIMAL NOT NULL,
	rooms INT,
	blockFK INT,
	FOREIGN KEY (blockFK) REFERENCES Block(blockID)
);

/*---------- CREATE TABLE Resident ---------------*/
CREATE TABLE IF NOT EXISTS Resident(
	residentID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	phoneNumber VARCHAR(20),
	apartmentFK INT,
	FOREIGN KEY (apartmentFK) REFERENCES Apartment(apartmentID)
);

/*---------- CREATE TABLE ApartmentOwnerREL ---------------*/
CREATE TABLE IF NOT EXISTS ApartmentOwnerREL(
	apartmentFK INT NOT NULL,
	ownerFK INT NOT NULL,
	percentage DECIMAL NOT NULL,
	PRIMARY KEY(apartmentFK, ownerFK)
);

/*---------- CREATE TABLE Reservation ---------------*/
CREATE TABLE IF NOT EXISTS Reservation(
	reservationID INT AUTO_INCREMENT PRIMARY KEY,
	reservationDateTime TIMESTAMP NOT NULL,
	commonSpaceFK INT,
	apartmentFK INT,
	FOREIGN KEY (commonSpaceFK) REFERENCES CommonSpace(commonSpaceID),
	FOREIGN KEY (apartmentFK) REFERENCES Apartment(apartmentID)
);

/*---------- CREATE TABLE Payment ---------------*/
CREATE TABLE IF NOT EXISTS Payment(
	paymentID INT AUTO_INCREMENT PRIMARY KEY,
	paymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	deadline TIMESTAMP NOT NULL,
	serviceFK INT,
	apartmentFK INT,
	FOREIGN KEY (serviceFK) REFERENCES Service(serviceID),
	FOREIGN KEY (apartmentFK) REFERENCES Apartment(apartmentID)
);

/*---------- CREATE TABLE HistoricalReservation ---------------*/
CREATE TABLE IF NOT EXISTS HistoricalReservation(
	historicalID INT AUTO_INCREMENT PRIMARY KEY,
	statusFK INT NOT NULL,
	reservationFK INT NOT NULL,
	actionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE HistoricalReservation ADD UNIQUE `unique_reservation` (statusFK, reservationFK);


/*---------- CREATE TABLE Balance ---------------*/
CREATE TABLE IF NOT EXISTS Balance(
	balanceID INT AUTO_INCREMENT PRIMARY KEY,
	paymentFK INT NOT NULL,
	reservationFK INT NOT NULL,
	mora DECIMAL DEFAULT 0.0
);

ALTER TABLE Balance ADD UNIQUE `unique_balance` (paymentFK, reservationFK);




