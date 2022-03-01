#esto es un  comentario y sirve para dar conexto de que se hace,  se hizo o se hara
#TODO: logica para este controlador



#variables de texto
nombre = 'edgar'
apellido = 'chavez'


# si queremos tener un texto que pueda contener saltos de linea
description = """hola amigos:
como estan?
yo muy bien jeje"""


print(description)

# variables numericas
year = 2022

# type() => mostrara que tipo de variable es
print(type(year))

# en python None = null 
especialidad = None

# en python no hace validacion del tipo de dato primario (si la varible 'nace' siendo
# String) normal se puede cambiar su tipo a otro (boolean, int, float, array, etc...)
# en python no existe las constantes
dni = [123456]
dni = 'perano'
dni = False

# id() > dara la ubicacion de esa ubicacion en relacion a la memoria del dispositivo
print(id(dni))

# mas de una variable en una sola linea
mes, dia = "febrary",  28

# del > elimina la variable de la memoria
del mes