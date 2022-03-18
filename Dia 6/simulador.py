# FACTORY
from faker import Faker
from faker.providers import internet, person

fake = Faker()

# le agregamos un provider adicional a nuestro faker para que ahora pueda utilizar los tradicionales y los de internet
fake.add_provider({internet, person})

# usando el providor de person hacer que me imprima un nombre, ape_pat, ape_mat, correo (internet), num_telefonico (phone_number)

#print(fake.name())

def generar_alumnos(limite):

    for persona in range(100): 
     nombre = fake.first_name()
     apePat = fake.last_name()
     apeMat = fake.last_name()
     correo = fake.ascii_free_email()

     # utilzando faker agregar un numero aleatorio entre 911111111 hasta 999999999

     telefono = fake.bothify(text='9########')
 
     sql = '''
     INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES

                          ('%s', '%s', '%s', '%s', '%s'); ''' % (nombre, apePat, apeMat, correo, telefono)

     # version nueva
     #'''INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emer) VALUES
     #                       ('{}', '{}', '{}', '{}', '{}');'''.format(nombre, apePat, apeMat, correo, telefono)                          

     print(sql)                          


def generar_niveles():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['sotano', 'primer piso', 'segundo piso', 'tercer piso']
    niveles = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto']

    for nivel in niveles:

        pos_secciones = fake.random_int(min=2, max=3)
        for posicion in range(0, pos_secciones):
            pos_ubicacion = fake.random_int(min=0, max=3)
            seccion = secciones[posicion]
            ubicacion = ubicaciones[pos_ubicacion]
            nombre = nivel
            sql = '''INSERT INTO niveles (seccion, ubicacion, nombre) values
                                   ('%s', '%s', '%s');''' % (seccion, ubicacion, nombre)

            print(sql)    
generar_niveles()                                           