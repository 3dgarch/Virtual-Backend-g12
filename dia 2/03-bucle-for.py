# en cada iteracion de la lista notas tendremos su valor y lo almacenaremos en una variable llamada nota
# el mismo funcionamiento se da para cualquier coleccion de datos(lista, tupla, diccionario, conjuntos)
#

notas = [10, 20, 16, 8, 6, 1]
for nota in notas:
    print(nota)

# creamos un bucle manual para una iteracion hasta el limite definido en el range
for numero in range(10):
    print(numero)

# si colocamos dos parametros el primero sifnificara el numero inicial y el segundo el tope
for numero in range(5, 10):
    print(numero)

# si colocamos dos parametros el primero significara el numero inicial, el segundo el tope y el tercero sera de cuanto en cuanto hara la incrementacion odecrementacion
# empezara en 5, hasta <10 y en cada ciclo incrementara en 2 unidades
for numero in range(5, 10, 2):
    print(numero)

    # imprimir los 3 valores iniciales de notas
    notas = [10, 20, 16, 8, 6, 1]

    for nota in notas[:3]:
        print(nota)


aprobados = ['Pedro','Eduardo', 'Maria', 'Fatima']

for aprobado in aprobados:
    if (aprobado == 'Pedro'):
        print('pedro esta aprobado')
        break

else:
    print('Termino de ejecutarse el for')
print('termino de ejecutarse el for')



productos = ['Manzanas','Peras','Tallarines','Tazas']
busqueda = input('Ingrese el producto a buscar: ')

for producto in productos:
    if producto == busqueda:
        print('El producto si esta en la tienda')
        break
else:
    print('No se encontro el producto')        