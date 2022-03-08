# un error es una mala ejecucion del codigo que hara mi proyecto o script deje de funcionar
# en puthon tenemos varios errores para los diferentes sucesos:

try:
    valor = int(input('ingresa un numero'))
    print(valor)

except ValueError:
    # Entrara a este except cuando el error sea de tipo TypeError   
    print('Error al convertir un string a un numero') 
except Exception as error:
    # capturara el error causante impidiendo que el programa deje de funcionar
    # solamente ingresara cuando tengamos un error
    print('oops algo salio mal intentalo nuevamente')    



print('yo finalizo correctamente')






# bucle

while True:
    try:
        valor = int(input('ingresa un numero'))
        break
    except:
        print('valor incorrecto, solo pueden ser numeros')
print(valor)    



try:
    resultado = 1/1
except:
    print('hubo unerror')    
else:
    # el else en el caso de los try-except se ejecutara si nunca ingreso a un except, osea si el funcionamiento fue el esperado sin errores
    print('yo soy el else')    
finally:
    # ingresara si el try   fue exitoso o no , osea si del mismo ingreso o algun except o no

    print('yo me ejecutare si todo  fue bien y fue mal')    