nombre = 'Eduardo'

print(nombre)
# concatenacion (juntar) varios valores
print('el nombre es: ',nombre,'del usuario')


estado_civil = 'viudo'

# si queremosusar el metodo format tenemos que coincidir el mismo numero de veces que colocamos el {} con la cantidad de variables
print('lapersona {} es {}'.format(nombre, estado_civil))

print('{1} es una persona {0}'.format(estado_civil, nombre))