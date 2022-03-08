# Herencia > extraer informacion de una clase  padre

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def saludar(self):
        return 'hola soy {}'.format(self.nombre)

# alumno a heredado todos los atributos y metodos (comportamiento) de la clase padre
class Alumno(usuario):
    def __init__(self, nobre, apellido, correo, padres):
        # super() > sirve para mandar a llamar a la cabeza de la cual estamos haciendo la herencia para no volver a escribir la misma logica
        super() .__init__(nobre, apellido, correo)
        self.padres = padres