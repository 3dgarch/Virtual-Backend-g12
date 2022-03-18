-- INSERTAR DATA
use prueba;
insert into vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) values
					('PFIZER', true,'2022-04-16','USA','123jkl'),
                    ('SINOPHARM',true,'2022-10-10','CHINA','vxcvxc'),
                    ('MODERNA',true,'2022-09-14','USA','zxczxc'),
                    ('SPUTKIN',false,'2022-10-04','RUSIA','jejffer');

insert into vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);    
                        
                        
                        
                        
                        
                        
-- Mostrar todos los nombres de las vacunas
 select nombre from vacunas;
-- mostrar las vacunas que sean de procedencia USA
 select * from vacunas where procedncia = 'uUSE';
-- mostrar las vacunas que no sean de procedencia USA
 select * from vacunas where procedencia != 'USE'
                        
                        