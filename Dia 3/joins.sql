-- Joins
-- es la manera de ingresar desde una tabla hacia otra mediante una col en comun

USE prueba;

-- el uso de los joins solamente se podra realizar en el bloque de FROM
-- Devuelveme todas las columnas de la tabla vacunatorios haciendome una interseccion con la tabla vacunas en la que sea igual su col 
-- (vacunatorios)vacuna_id = (vacunas)id
SELECT * 
FROM vacunatorios INNER JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 1 ;

-- LEFT JOIN
-- Traera todo el contenido de la tabla de la izquierda y adicionalmente el contenido de interseccion con la tabla de la derecha
SELECT *
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

-- RIGHT JOIN
-- traera todo el contenido de la tabla de la derecha y adicionalmente el contenido de la interseccion con la tabla de la izquierda
select *
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;



-- FULL OUTER JOIN
-- traera toda la informacion tanto de la tabla de la izquierda como de la derecha y opcionalmente si hay alguna interseccion lo hara sino no importa
SELECT *
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id UNION
SELECT *
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;


INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, imagen, vacuna_id) VALUES
                         ('Posta Jose Galvez', '14.26598', '32.2569', 'AV. El Sol', 'LUN-VIE 15:00 22:00',null,null );
                         



-- EJERCICIO
-- 1. Devolver todos los vacunatorios en los cuales la vacuna sea sinopharm y su horario de atencion sea de LUN-VIE
SELECT *
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'sinopharm' AND horario_atencion LIKE '%LUN-VIE%';

-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latirud -5.00 y 10.00 IN()
SELECT vacunas.nombre
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE latitud IN (-5.00, 10.00);

-- 3.  Devolver todas las vacunas que no tengan vacunatorio y solamene su procedencia y nombre
SELECT procedencia, vacunas.nombre
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;
                          

