# mientras que
numero = 0
while numero < 10:
    # pass > sirve para indicar dentro de un bloque de codigo que aun nohemos definido la logica
    #que no haga pero que no de  error 
    pass
    print(numero)
    numero += 1
else:
    print('el while termino bien')

# En relacion a los siguientes numeros indicar cuantos son pares y cuantos son impares
# PRIMERO CON FOR
numeros = [1,5,16,28,234,67,29]


par, impar = 0, 0
for numero in numeros:
    if numero % 2 == 0 :
        # la division entre dos me da un residuo 0 osea par
        par += 1
    else:
        impar += 1
print('hay {} numeros pares'.format(par))
print('hay {} numeros impares'.format(impar))



# AHORA WHILE
posicion = 0
par, impar = 0, 0

while posicion < len(numeros):
    if numeros[posicion] % 2 == 0:
       par += 1
    else:
        impar += 1
    posicion += 1
print('hay {} numeros pares'.format(par))
print('hay {} numeros impares'.format(impar))


