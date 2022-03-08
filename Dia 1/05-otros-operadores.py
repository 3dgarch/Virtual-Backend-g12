# operadores de comparacion
numero1, numero2 = 10, 20

#Igual que
print(numero1 == numero2)

# mayor que / menor igual quw
print(numero1 > numero2)
print(numero1 >= numero2)

# menor que / menor igual que
print(numero1 < numero2)
print(numero1 <= numero2)

# diferente de
print(numero1 != numero2)



# operadores logicos
print((10>5) and (10<20))
print((10>5) or (10<20))


# operadores de identidad
# is
# is not
# sirve para ver si estan apuntando a la misma direccion de memoria
verduras = ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo']
# NOTA: las colecciones de datos son variables mutables (que cuando cambia  su contenido este se vera reflejada en todas las copias de dicha variable)
verduras2[0] = 'peregil'
verduras[1] = 'manzana'


# El metodo copy() lo que hace es copia el contenido de la variable pero se guarda en una nueva posicion de memoria
verduras4 = verduras.copy()
verduras4[0] = 'huacatay'
print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print('la posicion de la variable verduras es: ',id(verduras))
print('la posicion de la variable verduras',id(verduras2))



nombre = 'eduardo'
nacionalidad = 'peruano'
nacionalidad = 'colombiano'

print(nombre == 'eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))
