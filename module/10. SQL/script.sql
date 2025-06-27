SELECT * FROM demandes ;
SELECT * FROM poi ;
SELECT * FROM point_de_charge ;
SELECT * FROM pointgps ;
SELECT * FROM polygon ;
SELECT * FROM utilisateur ;


UPDATE utilisateur 
SET user_status = TRUE
WHERE
user_name = 'thomas';

SELECT * FROM pointgps WHERE TRUE;
SELECT id_point FROM pointgps WHERE latitude = 48.8566;
(SELECT id_user FROM UTILISATEUR WHERE user_name = 'Alice');






