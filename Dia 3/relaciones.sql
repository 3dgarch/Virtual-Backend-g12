CREATE TABLE vacunaciones(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) UNIQUE NOT NULL,
  estado BOOL DEFAULT TRUE,
  fecha_vencimiento DATE,
  procedencia ENUM('USA','CHINA','RUSIA','UK'),
  lote VARCHAR(10)
);


CREATE TABLE vacunatorio(
 id INT PRIMARY KEY AUTO_INCREMENT,
 nombre VARCHAR(100) NOT NULL,
 latitud FLOAT,
 longitud FLOAT,
 horario_atencion VARCHAR(100)
);

