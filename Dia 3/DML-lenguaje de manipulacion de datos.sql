USE prueba;
-- Sub parte de SQL: 
-- DML: Manipulacion Language (lenguaje de manipulacion de datos)
-- Se utiliza para la manipulacion de la informacion dentro de una base de datos
-- INSERT, SELECT, UPDATE, DELETE
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					 ('Eduardo','12345678','DNI', true); 
                     
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES    
					('Estefani','15923642','RUC', true),
                    ('Fabian','95434254','DNI', false);

-- SELECT: es el comando que sirve para visualizar la informacion de una determinada tabla o tablas
-- SELECT col1, col2... from tabla;

SELECT nombre, documento FROM clientes;

-- si queremos observar todas las columnas de esta tabla(s)
SELECT * FROM clientes;

-- si queremos hacer un filtro de datos
-- al usar parentecis en una condicional hara que esas condiciones internas se ejecuten primero para  luego recien el resultado se compare con la condicion externa
SELECT * FROM clientes WHERE documento = '73500746' AND (nombre = 'Eduardo' OR nombre = 'Estefani');

-- Seleccionar a todas las persona que tienen DNI y que su estado sea true
SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = true;

-- LIKE > en columnas String para hacer una similitud y ademas usamos usaremos los '%' para indicar si no se sabe en que parte exactamnete esta la letra
SELECT * FROM clientes WHERE nombre LIKE 'Fabi%';

-- UPDATE > sirve para actualizar uno o varios registros de una determnada tabla
UPDATE clientes SET nombre = 'Ramiro', documento = '3333568' WHERE id = 1;

-- DELETE > sirve para eliminar registros de una determinada tabla
DELETE FROM clientes WHERE ID = 1;






