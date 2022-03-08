# DFU
#Funciones
# almacenara un bloque de codigo con su comportamiento y solamente se ejecutara cuando este sea invocado(llamado)


# Al momneto de llamar a la funcion  tenemos que pasarle el mismo numerode parametros que hemos definido
import re


def sumar(numero1, numero2):
    print('se realiizara la sumatoria')
    print(numero1 + numero2)

sumar(5 , 7)


def nombre(x):
    '''funcion que recibe un string y loimprime por consola: )'''
    print(x)
nombre('Eduarco')

#mostrara la documentacion dde la funcion si es que hay
print(nombre.__doc__)


#  ahora, tambien ´podriamos definir funciones que ejecuten algo y que nos den una respuesta
usuario = []
def registrar(nombre, email, telefono):
    # aqui registramos el usuario
    usuario.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
    })

    return {
        'message': 'usuario registrado exitosamente',
        'usuario': usuario[0]
    },True,1


# si una funcion retorna mas de un valor (retornara una tupla) entonces podemos hacer dos cosas
# 1: si solamente declaramos una variable ahi se almacenara toda la tupla.
# 2: si queremos almacenar cada valor de la tupla en una variable podemos hacer una destructuracion de esa tupla declarando el mismo numero de variables que el numero de contenidos de la tuplas
resultado, estado_civil, nacionalidad = registrar('Eduardo', 'ederrivera@gmail.com', '123456789')

print(resultado)
print(estado_civil)
print(nacionalidad)


# si nosotros creamos una funcion que opcional reciba ciertos parametros estos parametros opcionales siempre deben de ir al final, primero los requeridos y luego los opcionales
productos=[]
def registrar_productos(nombre, precio, estado=True, almacen='almacen del cercado'):
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen': almacen
    })
    return 'producto agregado exitosamente'
# siempre tenemos que pasar obligatoriamente los parametros que no tienen valores por defecto
registrar_productos('tomates', 4.50)
registrar_productos('apio', 1.40, False)
registrar_productos('cebolla', 5.30, True, 'Almacen nuevo mercado')
# otra forma de pasar parametros 
registrar_productos(almacen='almacen de la costa', nombre='pesacado tilapia', precio=2.50)



# Recibara un numero indeterminada de parametros en los cuales los almanecera en una tupla
# Puede recibir un numero indeterminado de parametros y estos pueden ser de diferentes tipos
def alumnos(clase,*args):
    print(args)

alumnos('Eduardo','nahia','pedro','mario','jean carlos')
alumnos('roxana','luis','joshua','daany')
alumnos('juanito')
alumnos('martha',30, False, 'juan',1.5)



#Kwargs > Keyword argument
# si la funcion queremos recibir un numero ilimitado de argumentos pero estos deben de tener su nombre de parametro con su valor entonces usaremos los kwargs y estos se almacenaran en un diccionario
def ingresarProductos(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('el usuario quiere agregar un producto con el nombre')
    if(kwargs.get('cantidad')):
        print('El usuario quiere ingresar la cantidad del producto')

ingresarProductos(nombre='Manzana', precio=2.40, estado=True, pais_procedencia='peru') 
ingresarProductos(tamanio='grande', cantidad=100, nombre='pera de agua')


#recursividad
# es utilizar la funcion dentro de la misma funcion

def saludar_n_veces(limite):
    if(limite == 0):
        return'llege al limite'
    print('saludar')
    saludar_n_veces(limite-1)
    
resultado = saludar_n_veces(10)    
print(resultado)


# FACTORIAL DE 5
# 5! = 5*4*3*2*1 = 120
def factorial(limite):
    if limite == 0:
        return 1
    return limite * factorial(limite-1)

resultado = factorial(5)    
print(resultado)