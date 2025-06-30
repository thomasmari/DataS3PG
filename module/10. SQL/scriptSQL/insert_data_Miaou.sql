-- LEVEL 0
-- Insertion de données dans la table UTILISATEUR
INSERT INTO utilisateur(user_name,user_mail,user_password,user_role,user_status) 
VALUES 
	('Arthur','le_graal@gmail.com','12345','user',FALSE),
	('Lancelot','lancelot@gmail.com','12344','user',FALSE),
	('Merlin','LaMagie@gmail.com','1234','cartograph',FALSE),
	('Guenievre','guenievre@gmail.com','12345','user',FALSE),
	('Dame du Lac','ddl@gmail.com','1234','cartograph',FALSE),
	('Alice', 'alice@example.com', 'password123', 'admin', TRUE),
	('Bob', 'bob@example.com', 'secure456', 'user', TRUE),
	('Charlie', 'charlie@example.com', 'pass789', 'user', FALSE);

-- Insertion de données dans la table POINTGPS

INSERT INTO POLYGON (poly_name, poly_description, id_creator) VALUES
('Q_Hoche', 'Quartier Hoche',(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Dame du Lac'));
INSERT INTO pointgps (latitude, longitude, next_id, id_polygon) VALUES (5.7250, 45.1830, NULL, (SELECT max(id_polygon) FROM polygon)) ;
INSERT INTO pointgps (latitude, longitude, next_id, id_polygon) 
VALUES 
	(5.7250, 45.1830, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7280, 45.1830, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7295, 45.1835, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7290, 45.1858, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7264, 45.1858, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7245, 45.1850, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7245, 45.1835,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon));

INSERT INTO POLYGON (poly_name, poly_description, id_creator) VALUES
('Q_PPM', 'Parc Paul Mistral',(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Merlin'));
INSERT INTO pointgps (latitude, longitude, next_id, id_polygon) VALUES (5.7368, 45.1829, NULL, (SELECT max(id_polygon) FROM polygon)) ;
INSERT INTO pointgps (latitude, longitude, next_id, id_polygon) 
VALUES 
	(5.7384, 45.1845, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7388, 45.1862, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7379, 45.1874, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7364, 45.1880, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7348, 45.1881, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7333, 45.1873, (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7327, 45.1861,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7329, 45.1849,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7343, 45.1837,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7358, 45.1832,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon)),
  	(5.7368, 45.1829,  (SELECT max(id_point) FROM pointgps), (SELECT max(id_polygon) FROM polygon));
-- (SELECT IDENT_CURRENT(pointgps))
-- DECLARE @pida SERIAL = (SELECT IDENT_CURRENT(pointgps))
-- INSERT INTO pointgps (latitude, longitude) VALUES (5.7250, 45.1830) ;
-- DECLARE @pidb SERIAL = SELECT IDENT_CURRENT(pointgps)
-- INSERT INTO ligne(id_polygone,id_point_a,id_point_b) VALUES (IDENT_CURRENT(polygon), @pida,@pidb) ;

INSERT INTO pointgps (latitude, longitude, next_id, id_polygon) VALUES 
(45.1883, 5.7240,NULL,NULL), --pt1 
(45.1893, 5.7348,NULL,NULL), --pt2
(45.2200, 5.3942,NULL,NULL), --pv1
(45.1845, 5.7350,NULL,NULL); --pv2

-- Insertion de données dans la table POI
INSERT INTO POI (type_poi, is_valid, id_point, id_creator,description) VALUES
('Parking Trotinette', FALSE, 
	(SELECT id_point FROM pointgps WHERE latitude = 45.1883), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Alice'),
	'Parking Trot 1'),
('Parking Trotinette', FALSE, 
	(SELECT id_point FROM pointgps WHERE latitude = 45.1893), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Alice'),
	'Parking Trot 2'),
('Parking Vélo', FALSE, 
	(SELECT id_point FROM pointgps WHERE latitude = 45.1883), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Bob'),
	'Parking VELO 1'),
('Parking Vélo', FALSE, 
	(SELECT id_point FROM pointgps WHERE latitude = 45.1893), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Bob'),
	'Parking VELO 2');--,	
--('Parking Trottinette', FALSE, 2, 2),
--('Point de charge', TRUE, 3, 3);

-- Insertion de données dans la table POI
INSERT INTO point_de_charge (type_charge, has_pump, id_poi) VALUES
('Rapide', TRUE, (SELECT id_poi FROM poi WHERE description = 'Parking Trot 1')),
('Lent', FALSE,	(SELECT id_poi FROM poi WHERE description = 'Parking Trot 2')) ;
