
-- Insertion de données dans la table UTILISATEUR
INSERT INTO utilisateur(user_name,user_mail,user_password,user_role,user_status) 
VALUES 
	('Arthur','le_graal@gmail.com','12345','user',FALSE),
	('Lancelot','lancelot@gmail.com','12344','user',FALSE),
	('Merlin','LaMagie@gmail.com','1234','user',FALSE),
	('Guenievre','guenievre@gmail.com','12345','user',FALSE),
	('Dame du Lac','ddl@gmail.com','1234','cartograph',FALSE);

INSERT INTO UTILISATEUR (user_name, user_mail, user_password, user_role, user_status) VALUES
('Alice', 'alice@example.com', 'password123', 'admin', TRUE),
('Bob', 'bob@example.com', 'secure456', 'user', TRUE),
('Charlie', 'charlie@example.com', 'pass789', 'user', FALSE);

-- Insertion de données dans la table POINTGPS
INSERT INTO pointgps (latitude, longitude) VALUES
(48.8566, 2.3522),   -- Paris
(43.6047, 1.4442),   -- Toulouse
(45.7640, 4.8357);   -- Lyon

-- Insertion de données dans la table POLYGON
INSERT INTO POLYGON (poly_name, poly_description, id_creator) VALUES
('Zone A', 'Zone urbaine dense',(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Dame du Lac')),
('Zone B', 'Parc naturel régional', (SELECT id_user FROM UTILISATEUR WHERE user_name = 'Merlin'));

-- Insertion de données dans la table POI
INSERT INTO POI (type_poi, is_valid, id_point, id_creator,id_validator) VALUES
('Parking Vélo', 
	TRUE, 
	(SELECT id_point FROM pointgps WHERE latitude = 48.8566), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Alice'),
	NULL),
('Parking Trotinette', 
	TRUE, 
	(SELECT id_point FROM pointgps WHERE latitude = 43.6047), 
	(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Merlin'),
	NULL);--,	
--('Parking Trottinette', FALSE, 2, 2),
--('Point de charge', TRUE, 3, 3);
