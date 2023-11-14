CREATE DATABASE IF NOT EXISTS aerienne;

USE aerienne;

CREATE TABLE pilote (
	numpil varchar(255) NOT NULL PRIMARY KEY,
	nompil varchar(255) NOT NULL,
	adr varchar(255) NOT NULL,
	sal int NOT NULL
);

CREATE TABLE avion (
	numav varchar(255) NOT NULL PRIMARY KEY,
	nomav varchar(255) NOT NULL,
	cap int NOT NULL
);

CREATE TABLE vol (
	numvol varchar(255) NOT NULL,
	numpil varchar(255),
	numav varchar(255),
	ville_dep varchar(255) NOT NULL,
	ville_arr varchar(255) NOT NULL,
	h_dep TIME NOT NULL,
	h_arr TIME NOT NULL,
	CONSTRAINT FK_Numpil FOREIGN KEY (numpil)
	REFERENCES pilote(numpil),
	CONSTRAINT FK_Numav FOREIGN KEY (numav)
	REFERENCES avion(numav)
);

INSERT INTO pilote (numpil, nompil, adr, sal)
VALUES 
	('P0001', 'Dupont', 'Lyon', 3000),
	('P0002', 'Simon', 'Paris', 3500),
	('P0003', 'François', 'MARSEILLE', 3800),
	('P0004', 'André', 'Nice', 2500),
	('P0005', 'Arthur', 'Lille', 2400),
	('P0006', 'Mathieu', 'Nantes', 3900),
	('P0007', 'Bruno', 'Lyon', 3000);

-- Insert data into the avion table
INSERT INTO avion (numav, nomav, cap)
VALUES 
	('A0001', 'Boeing 747', 420),
	('A0002', 'Airbus 320', 300),
	('A0003', 'Airbus 300', 280),
	('A0004', 'Boeing 737', 250),
	('A0005', 'A0005', 120),
	('A0006', 'Boeing 747', 410);

INSERT INTO vol (numvol, numpil, numav, ville_dep, ville_arr, h_dep, h_arr)
VALUES 
	('V0001', 'P0002', 'A0001', 'Paris', 'San Francisco', '10:00', '09:30'),
	('V0002', 'P0001', 'A0003', 'Londres', 'Moscou', '10:30', '17:00'),
	('V0003', 'P0003', 'A0002', 'Berlin', 'Madrid', '11:15', '18:00'),
	('V0004', 'P0006', 'A0004', 'Londres', 'Madrid', '06:20', '09:30'),
	('V0005', 'P0005', 'A0006', 'Bruxelles', 'Rome', '10:00', '15:10'),
	('V0006', 'P0001', 'A0005', 'Berlin', 'Amsterdam', '14:30', '17:00'),
	('V0007', 'P0002', 'A0001', 'Paris', 'Bruxelles', '18:00', '20:00'),
	('V0008', 'P0003', 'A0001', 'New York', 'Paris', '03:00', '21:30'),
	('V0009', 'P0006', 'A0004', 'Paris', 'Bruxelles', '06:00', '07:00'),
	('V00010', 'P0004', 'A0002', 'Berlin', 'Madrid', '08:00', '11:00');

SELECT numpil,nompil FROM pilote;
-- +--------+-----------+
-- | numpil | nompil    |
-- +--------+-----------+
-- | P0001  | Dupont    |
-- | P0002  | Simon     |
-- | P0003  | François  |
-- | P0004  | André     |
-- | P0005  | Arthur    |
-- | P0006  | Mathieu   |
-- | P0007  | Bruno     |
-- +--------+-----------+

SELECT DISTINCT ville_dep FROM vol;
-- +-----------+
-- | ville_dep |
-- +-----------+
-- | Paris     |
-- | Londres   |
-- | Berlin    |
-- | Bruxelles |
-- | New York  |
-- +-----------+

SELECT nompil FROM pilote WHERE adr = 'Marseille';
-- +-----------+
-- | nompil    |
-- +-----------+
-- | François  |
-- +-----------+

SELECT nompil,adr FROM pilote WHERE sal < 3000;
-- +--------+-------+
-- | nompil | adr   |
-- +--------+-------+
-- | André  | Nice  |
-- | Arthur | Lille |
-- +--------+-------+

SELECT nompil FROM pilote WHERE adr = NULL;
-- Empty set (0,00 sec)

SELECT * from avion WHERE nomav = 'Boeing 747' OR nomav = 'Boeing 737';
-- +-------+------------+-----+
-- | numav | nomav      | cap |
-- +-------+------------+-----+
-- | A0001 | Boeing 747 | 420 |
-- | A0004 | Boeing 737 | 250 |
-- | A0006 | Boeing 747 | 410 |
-- +-------+------------+-----+

SELECT nompil from pilote where sal < 3900 AND sal > 2500;
-- +-----------+
-- | nompil    |
-- +-----------+
-- | Dupont    |
-- | Simon     |
-- | François  |
-- | Bruno     |
-- +-----------+

SELECT cap from avion where nomav LIKE '%Airbus%';
-- +-----+
-- | cap |
-- +-----+
-- | 300 |
-- | 280 |
-- +-----+

SELECT * FROM vol WHERE ville_dep = 'Bruxelles' AND ville_arr = 'Paris';
-- Empty set (0,00 sec)

SELECT AVG(sal) AS salaire_moyen FROM pilote;
-- +---------------+
-- | salaire_moyen |
-- +---------------+
-- |     3157.1429 |
-- +---------------+
