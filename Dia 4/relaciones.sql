CREATE TABLE vacunaciones(
   id INT PRIMARY KEY AUTO_INCREMENT,
   nombre VARCHAR(100) UNIQUE NOT NULL,
   estado BOOL DEFAULT  TRUE,
   fecha_vencimiento DATE,
   PROCEDENCIA ENUM('USA','CHINA','RUSIA','UK'),
   lote VARCHAR(10)
   
);

CREATE TABLE vacunatorio(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  latitud FLOAT,
  longitud FLOAT,
  direccion VARCHAR(200),
  horario_atencion VARCHAR(100)
);