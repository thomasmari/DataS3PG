DROP TABLE IF EXISTS 	point_de_charge, demandes ; -- level 4
DROP TABLE IF EXISTS 	poi; --level 3
DROP TABLE IF EXISTS 	pointgps; --level 2
DROP TABLE IF EXISTS  	polygon; --level 1
DROP TABLE IF EXISTS  	utilisateur; --level 0

CREATE TABLE utilisateur ( -- level 0
id_user SERIAL PRIMARY KEY,
user_name VARCHAR(20) NOT NULL,
user_mail VARCHAR(20) NOT NULL UNIQUE,
user_password VARCHAR(20) NOT NULL,
user_role VARCHAR(20) NOT NULL,
user_status BOOLEAN NOT NULL
);

CREATE TABLE polygon ( -- level 1
id_polygon SERIAL PRIMARY KEY,
poly_name VARCHAR(20) UNIQUE,
poly_description VARCHAR(100),
id_creator SERIAL,
CONSTRAINT fk_polygon
  FOREIGN KEY(id_creator)
	REFERENCES UTILISATEUR(id_user)
);

CREATE TABLE pointgps ( -- level 2
id_point SERIAL PRIMARY KEY,
latitude FLOAT NOT NULL,
longitude FLOAT NOT NULL,
next_id INT,
id_polygon INT,
CONSTRAINT fk_id_poly
  FOREIGN KEY(id_polygon)
	REFERENCES polygon(id_polygon)
);

-- ALTER TABLE pointgps 
-- ALTER COLUMN next_id 
-- DROP NOT NULL;

-- ALTER TABLE pointgps 
-- ALTER COLUMN id_polygon 
-- DROP NOT NULL;

CREATE TABLE poi (	-- level 3
id_poi SERIAL PRIMARY KEY,
type_poi VARCHAR(20) NOT NULL,
is_valid BOOLEAN NOT NULL,
id_point SERIAL,
description VARCHAR(100),
CONSTRAINT fk_poi_1
  FOREIGN KEY(id_point)
	REFERENCES POINTGPS(id_point),
id_creator SERIAL,
CONSTRAINT fk_poi_2
  FOREIGN KEY(id_creator)
	REFERENCES UTILISATEUR(id_user),
id_validator INT DEFAULT NULL,
CONSTRAINT fk_poi_3
  FOREIGN KEY(id_validator)
	REFERENCES UTILISATEUR(id_user)
);

CREATE TABLE point_de_charge ( -- level 4
type_charge VARCHAR(6) NOT NULL,
has_pump BOOLEAN NOT NULL,
id_poi SERIAL,
CONSTRAINT fk_pdc
  FOREIGN KEY(id_poi)
	REFERENCES poi(id_poi)
);

CREATE TABLE demandes ( -- level 2
id_poi SERIAL, --FK
id_user SERIAL, --FK
type_poi VARCHAR(20) NOT NULL,
id_point SERIAL, --FK
date DATE NOT NULL,
CONSTRAINT fk_demande_1
  FOREIGN KEY(id_poi)
	REFERENCES POI(id_poi),
CONSTRAINT fk_demande_2
  FOREIGN KEY(id_user)
	REFERENCES UTILISATEUR(id_user),
CONSTRAINT fk_demande_3
  FOREIGN KEY(id_point)
	REFERENCES POINTGPS(id_point)
);


-- CREATE TABLE lignes ( -- level 2
-- id_polygon SERIAL NOT NULL,
-- id_point_a SERIAL NOT NULL,
-- id_point_b SERIAL NOT NULL,
-- CONSTRAINT fk_lignes_pa
--   FOREIGN KEY(id_point_a)
-- 	REFERENCES pointgps(id_point),
-- CONSTRAINT fk_lignes_pb
--   FOREIGN KEY(id_point_b)
-- 	REFERENCES pointgps(id_point)
-- );





