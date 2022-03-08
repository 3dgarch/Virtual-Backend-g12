# crear una clase Persona en la cual se guarden su nombre. fecha_nacimiento,
# nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno

class persona:
    def __init__(self, nombre, fec_nac, dni, nacionalidad):
        self.nombre = nombre
        self.fec_nac = fec_nac
        self.nacionalidad = nacionalidad
        self.dni = dni
    def saludar(self):
        print("hola, me llamo {}".format(self.nombre))


class Alumno(persona):
    def __init__(self, nombre, fec_nac, dni, nacionalidad, cursos):
        
