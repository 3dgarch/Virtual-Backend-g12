-- necesito un BD para almacenar los alumnos de mi colegio
-- el alumno con su informacion que seria nombre, ape_pat, ape_mat, correo, num_emergencia
-- cada seccion almacenar su nombre (A,B,C) y su ubicacion

CREATE DATABASE colegios;

USE colegios;

CREATE TABLE IF NOT EXISTS alumnos(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido_paterno VARCHAR(45),
  apellido_materno varchar(45),
  correo VARCHAR(45) UNIQUE,
  numero_emergencia VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS niveles(
  id INT PRIMARY KEY auto_increment,
  Sseccion VARCHAR(45) NOT NULL,
  ubicacion varchar(45),
  nombre varchar(45) not null
);
CREATE TABLE IF NOT EXISTS alumnos_niveles(
  id int primary key auto_increment,
  alumno_id int,
  nivel_id int,
  fecha_cursada year,
  foreign key(alumno_id) references alumnos(id),
  foreign key(nivel_id) references niveles(id)
);