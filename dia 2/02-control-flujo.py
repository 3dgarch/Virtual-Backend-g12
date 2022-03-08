# IF - ELSE
# python al no utizar llaves para definir bloque de un comportamiento diferente tenemos que utilizar trabulaciones (TAB)

edad = int(input('ingresa tu edad'))

if(edad > 18):
    print('la persona es mayor de edad')
elif edad > 15:
    print('puedes ingresar a la preparatoria')
else:
    print('la persona es menor de edad')     
print('finalizo el programa')   


# PRACTICA: validar si un numero (ingresos de una persona) ingresado por teclado es: 
# * mayor a 500: idicar que no recibe el bono yanapay
# * entre 500 y 250: indicar que si recibe el bono
# * es menor que 250: indicar que recibe el bono y un balon de gas

ingresos = int(input('ingresa tu sueldo'))

if (ingresos > 500):
    print('no recibe el bono Yanapay')
elif ingresos <= 500 and ingresos >= 250:
    print('recibe el bono Yanapay')
else:
    print('recibe el bono y un balon de gas')
print('finalizo el programa')