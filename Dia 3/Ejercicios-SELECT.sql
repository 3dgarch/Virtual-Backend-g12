-- INSERTA DATA
USE prueba;

INSERT INTO vacunas(nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
				   ('PFIZER', true, '2022-08-16', 'usa', '123JKL'),
                   ('SINOPHARM', true, '2022-10-10', 'china', 'vxcvxc'),
                   ('MODERNA', true, '2022-09-14', 'usa', 'zxczxc'),
                   ('SPUTNIK', false, '2022-10-04', 'rusia', 'ghjkhjfg');
ALTER TABLE vacunatorios ADD COLUMN direccion VARCHAR(100) AFTER longitud;                   
                   
INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, imagen, vacuna_id) VALUES
					     ('Camino Real', 14.121, -21.121, 'AV girasol 115', 'LUN-VIE 07:00 - 15:00', NULL, 1),
                         ('Hosp Gnral', 17.521, -11.1891, 'AV Circunvalacion s/n', 'LUN-VIE 07:00 - 15:00', 'hOSPITAL.JPG', 2),
                         ('Posta Cerro Azul', 11.258, -67.447, 'AAHH Los Querubines lote 3 MZ j', 'LUN-SAB 07:00 - 15:00', 'Foto01.png', 1),
                         ('Estadio Los Palitos', 24.121, -21.121, 'Calle Espinosa 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'Esto001.jpg', 3),
                         ('Plaza Del Amor Real', 4.116, -21.121, 'AV De Los Herues s/n', 'LUN-VIE 07:00 - 15:00', NULL, 1);


-- 1. Mostrar los nombres de las vacunas
SELECT nombre FROM vacunas;

-- 2. Mostrar las vacunas que sean de procedencia usa
SELECT * FROM vacunas WHERE procedencia = 'usa';

-- 3. Mostar las vacunas que no sean de procedencia usa
SELECT * FROM vacunas WHERE procedencia != 'usa';

-- 4. Mostrar las vacunas que en su lote tengan los digitos 'xc'
SELECT * FROM vacunas WHERE lote LIKE '%xc%' ;

-- 5. Mostar todos los vacunatorios que tengan horario de atencion los dias miercoles
SELECT * FROM  vacunatorios WHERE horario_atencion LIKE '%MIE%' OR horario_atencion LIKE '%LUN-VIE%' OR horario_atencion like '%lun-sab%';

-- 6. Mostar todos los vacunatorios que tengan la vacuna_id 1 pero que tengan foto
SELECT * FROM vacunatorios WHERE vacuba_id = 1 AND imagen IS NOT NULL;
