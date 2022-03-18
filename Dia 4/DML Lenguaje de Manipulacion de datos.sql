USE prueba;
-- Sub parte del sql:
-- DML: Data Manipulacion Language (lenguage de manipulacion de datos)
-- se utiliza para la manipulacion de la informacion dentro de una dabe de datos
-- INSERT, SELECT ,UPDATE, DELETE
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					 ('EDUARDO','73645245','DNI',true);
                     
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
                     ('estefani', '18354664', 'DNI', true);
                     


-- SELECT: es el comando que sirve para visualizar la informacion de una determinada tabla o table
-- SELECT: col1, col2,...FROM tabla;

SELECT NOMBRE, DOCUMENTO from clientes;

-- si queremos observar todas las columnas de esta tabla(s)
SELECT *FROM clientes;

SELECT * FROM clientes WHERE documento = '73645245' AND (nombre = 'Eduardo' OR nombre = 'Estefani');

-- seleccionar a todas las personas que tiene DNI y que su estado sea true
SELECT * FROM clientes WHERE tipo_docuemnto = 'DNI' AND estado = true;


-- LIKE en columnas de string para hacer una similitud y ademas usarenos los '%' para indicar si no se sabe en que parte exactamente esta la letra o letras
SELECT * FROM clientes WHERE nombre LIKE 'EDU%';


-- UPDATE sirve para actualizar uno o varios registros de una determinada tabla
-- UPDATE table SET col=nuevo_valor,.....WHERE col=val; 
UPDATE clientes SET nombre = 'Ramiro', documento = '33333568' WHERE id = 1 AND nombre = 'EDUARDO';


-- Modo seguro > es el modo que nos impide hacer actualizaciones (UPDATE) y eliminaciones (DELETE) sin usar
-- una col que sea indice (o PK)
-- otra forma de acceder mediante el Wokbench es en el menu Edit > Preferencias > SQL Editor y al final estara opcion modificar
-- Para desactivar el modo seguro:
SET SQL_SAFE_UPDATES = false;

-- DELETE sirve para eliminar REGISTROS de una determinada tabla
DELETE FROM clientes WHERE id = 1;


SELECT * FROM clientes;
                    
                     