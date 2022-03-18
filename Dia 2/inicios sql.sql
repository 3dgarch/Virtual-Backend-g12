# SQL > Structured Query Language
# un registro es un conjunto de datos y un dato es un valor que por si solo no dice nada
# por buenas practicas su nombre debe ser en singular

CREATE DATABASE prueba;

# Para indicar que BD vamos a utilizar usamos el comando USE
USE prueba;

CREATE TABLE clientes(
   # Ahora definimos las columnas pertenecientes a esta tabla
   # Debe haber al menos una columna por tabla es decir no puede existir una  tabla sin columnas
   # nombre_col  tipo_dato  [config adic.]
   # Primary key : me permitira identificar este registro con otros en relacion a sus tablas adyecentes
   
   id INT  AUTO_INCREMENT PRIMARY KEY,
   
   # CHAR(n) > creara una columna que siempre ocupara n  espacios de caracteres
   # VARCHAR(n) > crea una columna que podra tener comomaximo n caracteres y ocupara solamente el espacio que necesita
   # TEXT > reservara el espacio dinamico segun sea necesario para el valor de esa column pero no tendra limite
   nombre VARCHAR(50) NOT NULL,
   
   # UNIQUE: > significa que nose puede repetir este valor una vez ingresado en un registro
   documento VARCHAR(10) UNIQUE,
   
   # ENUM > sera dependiendo de los posibles valores su tipo de dato
   tipo_documento ENUM('C.E','DNI','RUC','PASAPORTE','C.M','OTRO'),
   
   # BOOL > podra ser true o false 
   estado BOOL
   
   
);