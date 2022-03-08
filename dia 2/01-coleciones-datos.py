# colecion de datos es una variable que puede almacenar varios valores

# Listas (list)
# ordenadas y que puede ser modificadas
        

nombre = ['pedro', 'luis', 'danny','Cesar', 'Magaly']

combinada = ['Eduardo', 82 , False , 15.8, [1, 2, 3]]

#las listas siempre empiezan en la posicion 0
print(nombre[0])

# Cuando hacemos el uso de valores negativos en una lista internamente python le dara vuelta
print(nombre[-2])

# pop() > remueve el ultimo elemnto de la lista y se puede almacenar en otra variable
resultado = nombre.pop()
print(resultado)
print(nombre)


# append() > ingresa un nuevo elemnto a la ultima posicion de la lista
nombre.append('juana')

# elimina el contenido de una posicion de la lista  pero no lo podemos almacenar en otra variable
del nombre[0]
print(nombre)


 # clear() > limpia toda la lista y la deja como nueva

nombre.clear()
print(nombre)

  
        # -1 <3
# Indicar una sub seleccion de la lista        

print(combinada[1:3])



# indicando el contenido de la lista y esto es muy util para una copia de la lista sinusar su misma posicion de memoria
y = combinada
x = combinada[:]

print(id(x))
print(id(combinada))
print(id(y))

#desde el inicio hasta <2
print(combinada[:2])
# desde la posicion 2 hasta el final
print(combinada[2:])


meses_dscto = ['enero', 'marzo', 'julio']
mes = 'septiembre'
mes2 = 'enero'

# indicara si el valor no se encuentra dentro de la lista
print(mes not in meses_dscto)
# indicara si el valor se encuentra en la listas
print(mes2 in meses_dscto)


# si hacemos una sumatoria en las listas se combinaran en la cual la segunda ira despues de la  primera
seccion_a = ['Roxana', 'Juan']
seccion_b = ['julieta', 'Martin']
print(seccion_a + seccion_b) 

# sirve para esperar un dato ingrsado por el usuario
dato = input('ingresa tu nombre: ')
print(dato)


#tuplas
# muy similar a la ista a execpcion que no se puede modificar
cursos = ('backend', 'frontend', 1, True)

print(cursos)
print(cursos[0])
# desde la posicion 0 hasta < 2
print(cursos[0:2])


variada = (1, 2, 3 , [4, 5, 6])

variada[3][0] = 'hola'

print(variada)
print('2' in variada)

# creamos una nueva lista a raiz de una tupla llamando a la clase list en la cual en el constructor de esa clase le pasas los valos que contendra la nueva lista
variada_lista = list(variada)
# no se puede crear una lista a raiz de otra lista eso lanzara un error, solo se puede crear una lista
#mediante su contructor mediante una tupla
list((1,2,3)) # [1,2,3]

print(variada_lista)

# para ver la cantidad de elemntos que conforman una tupla o una lista
#NOTA: la longitud siempre sera la cantidad de elemntos y esta siempre empezara en 1 mientras que la posicion siempre empezara en 0, es por eso que siempre longitud = posicion + 1
print(len(variada))


# conjuntos
# coleccion de datos DESORDENADA, una vez que se crea ya no se accedera a las posiciones de sus elemntos
estaciones = ['verano', 'otonio', 'primavera', 'invierno']
print(estaciones)

print('invierno' in estaciones)
# se agrega de forma aleatoria
estaciones.add('otro')
# pop() > quita el ultimo elemnto de la coleccion de datos (list, tuplas, set)
estacion = estaciones.pop()
print(estacion)

# Diccionarios
# una coleccion de datos DESORDENADA pero cada elemento obedece a una lave definida

persona={
    'nombre' : 'Eduardo',
    'apellido' : 'de rivero',
    'correo' : 'ederivero@gmail.com'

}

# hacemos la busqueda de una determinada llave y si no la encuentra nos retornara opcionalmente none
print(persona.get('apellido', 'no hay no existe'))


print(persona.keys())
# devuelve todas los contenidos de mi diccionario
print(persona.values())
# devuelve todas los elemntos y su contenido en forma de tuplas dentro de una lista
print(persona.items())

# si definimos  una llave que no existe, la creara, caso contrario modificara su valor
persona['edad'] = 28
#NOTA: si la llave no es exactamente igual creara una nueva (tiene que coincidir minus y mayus)
persona['nombre'] = 'ximena'
print(persona)

# eliminar una llave de un diccionario
persona.pop('apellido')





